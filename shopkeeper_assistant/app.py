import streamlit as st
from backend.data import build_graph
from backend.search import find_product, find_substitutes

# Page Config
st.set_page_config(page_title="Shopkeeper Assistant", page_icon="🛒", layout="wide")

# Initialize Graph
if 'kg' not in st.session_state:
    st.session_state.kg = build_graph()

kg = st.session_state.kg

# --- Sidebar Inputs ---
st.sidebar.header("Search Parameters")

# Get all products for the dropdown
all_products = [data['name'] for node, data in kg.graph.nodes(data=True) if data.get('type') == 'product']
selected_product_name = st.sidebar.selectbox("Select Product", all_products)

# Optional Inputs
max_price = st.sidebar.number_input("Max Price ($)", min_value=0.0, value=10.0, step=0.5)
preferred_brand = st.sidebar.text_input("Preferred Brand (Optional)")

# Get all unique attributes for tags
all_attributes = set()
for node, data in kg.graph.nodes(data=True):
    if data.get('type') == 'attribute':
        all_attributes.add(data['name'])
required_tags = st.sidebar.multiselect("Required Tags", sorted(list(all_attributes)))

# --- Main Content ---
st.title("🛒 Shopkeeper Product Substitution Assistant")

if st.sidebar.button("Find Product / Alternatives"):
    product_node = find_product(kg, selected_product_name)
    
    if not product_node:
        st.error("Product not found in database.")
    else:
        product_data = kg.get_node_data(product_node)
        
        # Display Requested Product
        st.subheader("Requested Product")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Name", product_data['name'])
        with col2:
            st.metric("Price", f"${product_data['price']:.2f}")
        with col3:
            status = "In Stock" if product_data['in_stock'] else "Out of Stock"
            st.metric("Status", status, delta_color="normal" if product_data['in_stock'] else "inverse")

        # Logic
        if product_data['in_stock']:
            st.success("✅ The requested product is available!")
        else:
            st.warning("⚠️ The requested product is currently out of stock.")
            st.divider()
            st.subheader("Suggested Alternatives")
            
            substitutes = find_substitutes(
                kg, 
                product_node, 
                max_price=max_price, 
                required_tags=required_tags,
                preferred_brand=preferred_brand if preferred_brand else None
            )
            
            if not substitutes:
                st.info("No suitable alternatives found matching your criteria.")
            else:
                for sub in substitutes:
                    with st.container():
                        c1, c2, c3 = st.columns([2, 1, 3])
                        with c1:
                            st.markdown(f"**{sub['name']}**")
                            st.caption(f"Brand: {sub['brand']}")
                        with c2:
                            st.markdown(f"**${sub['price']:.2f}**")
                        with c3:
                            st.markdown(f"💡 *{sub['explanation']}*")
                        st.divider()

# Footer
st.markdown("---")
st.caption("Powered by Knowledge Graph & Rule-Based Reasoning")
