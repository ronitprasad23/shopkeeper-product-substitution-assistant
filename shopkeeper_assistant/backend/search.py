import networkx as nx

def find_product(kg, product_name):
    """
    Finds a product node by name.
    """
    return kg.get_product_node(product_name)

def find_substitutes(kg, product_node, max_price=None, required_tags=None, preferred_brand=None):
    """
    Finds substitutes for a given product node based on constraints.
    Returns a list of dictionaries with product details and explanation.
    """
    if required_tags is None:
        required_tags = []
    
    graph = kg.graph
    product_data = graph.nodes[product_node]
    
    # 1. Identify Category
    category_node = None
    original_brand = None
    
    for neighbor in graph.neighbors(product_node):
        edge_data = graph.get_edge_data(product_node, neighbor)
        if edge_data.get('relation') == 'IS_A':
            category_node = neighbor
        elif edge_data.get('relation') == 'HAS_BRAND':
            original_brand = neighbor

    if not category_node:
        return [] # Should not happen if data is consistent

    # 2. Find Candidates (Siblings in the same category)
    candidates = []
    for neighbor in graph.neighbors(category_node):
        edge_data = graph.get_edge_data(neighbor, category_node) # Direction might not matter for undirected, but logic holds
        if graph.nodes[neighbor].get('type') == 'product' and neighbor != product_node:
            candidates.append(neighbor)

    # 3. Filter and Score Candidates
    valid_substitutes = []
    
    for cand in candidates:
        cand_data = graph.nodes[cand]
        
        # Filter: In Stock
        if not cand_data.get('in_stock'):
            continue
            
        # Filter: Max Price
        if max_price is not None and cand_data.get('price') > max_price:
            continue
            
        # Filter: Required Tags
        cand_tags = set()
        cand_brand = None
        for neighbor in graph.neighbors(cand):
            edge_data = graph.get_edge_data(cand, neighbor)
            if edge_data.get('relation') == 'HAS_ATTRIBUTE':
                cand_tags.add(graph.nodes[neighbor].get('name'))
            elif edge_data.get('relation') == 'HAS_BRAND':
                cand_brand = neighbor
        
        if not set(required_tags).issubset(cand_tags):
            continue

        # Scoring & Explanation
        score = 0
        explanations = []
        
        # Rule: Same Category (Implicit by search method)
        explanations.append(f"Same category: {category_node}")
        
        # Rule: Brand Match
        if preferred_brand:
             if cand_brand == preferred_brand:
                score += 2
                explanations.append(f"Matches preferred brand: {preferred_brand}")
        elif original_brand and cand_brand == original_brand:
            score += 1
            explanations.append("Same brand as original")
        else:
            explanations.append("Different brand")

        # Rule: Price
        if cand_data.get('price') < product_data.get('price'):
            score += 1
            explanations.append("Cheaper option")
        elif cand_data.get('price') == product_data.get('price'):
            explanations.append("Same price")
            
        # Rule: Tags
        if required_tags:
            explanations.append(f"Matches tags: {', '.join(required_tags)}")

        valid_substitutes.append({
            'id': cand,
            'name': cand_data.get('name'),
            'price': cand_data.get('price'),
            'brand': cand_brand,
            'score': score,
            'explanation': "; ".join(explanations)
        })

    # Sort by score (descending) then price (ascending)
    valid_substitutes.sort(key=lambda x: (-x['score'], x['price']))
    
    return valid_substitutes[:3]
