from backend.data import build_graph
from backend.search import find_product, find_substitutes

def test_backend():
    print("Building Graph...")
    kg = build_graph()
    
    # Test 1: Exact Match (In Stock)
    print("\n--- Test 1: Exact Match (In Stock) ---")
    p_node = find_product(kg, "Brand B Whole Milk 1L")
    if p_node:
        print(f"Found: {kg.get_node_data(p_node)}")
    else:
        print("Product not found!")

    # Test 2: Substitution (Out of Stock)
    print("\n--- Test 2: Substitution (Out of Stock) ---")
    # "Brand A Whole Milk 1L" is out of stock in mock data
    p_node = find_product(kg, "Brand A Whole Milk 1L")
    if p_node:
        print(f"Original: {kg.get_node_data(p_node)}")
        subs = find_substitutes(kg, p_node, max_price=5.0, required_tags=["lactose_free"])
        print(f"Substitutes found: {len(subs)}")
        for s in subs:
            print(f" - {s['name']} (${s['price']}): {s['explanation']}")
    else:
        print("Original product not found!")

    # Test 3: No Match
    print("\n--- Test 3: No Match (Impossible Price) ---")
    p_node = find_product(kg, "Brand A Whole Milk 1L")
    subs = find_substitutes(kg, p_node, max_price=0.1)
    print(f"Substitutes found: {len(subs)}")

if __name__ == "__main__":
    test_backend()
