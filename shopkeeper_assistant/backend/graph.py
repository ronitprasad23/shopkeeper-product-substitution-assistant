import networkx as nx

class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_product(self, product_id, name, price, in_stock, category, brand, attributes):
        """
        Adds a product node and connects it to category, brand, and attributes.
        """
        self.graph.add_node(product_id, type='product', name=name, price=price, in_stock=in_stock)
        
        # Connect to Category
        if category:
            self.graph.add_node(category, type='category', name=category)
            self.graph.add_edge(product_id, category, relation='IS_A')
        
        # Connect to Brand
        if brand:
            self.graph.add_node(brand, type='brand', name=brand)
            self.graph.add_edge(product_id, brand, relation='HAS_BRAND')
        
        # Connect to Attributes
        for attr in attributes:
            self.graph.add_node(attr, type='attribute', name=attr)
            self.graph.add_edge(product_id, attr, relation='HAS_ATTRIBUTE')

    def get_product_node(self, product_name):
        """
        Finds a product node by name (case-insensitive).
        """
        for node, data in self.graph.nodes(data=True):
            if data.get('type') == 'product' and data.get('name').lower() == product_name.lower():
                return node
        return None

    def get_node_data(self, node):
        return self.graph.nodes[node]
