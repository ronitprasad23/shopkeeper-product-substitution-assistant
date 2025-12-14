from backend.graph import KnowledgeGraph

def build_graph():
    kg = KnowledgeGraph()

    # --- Dairy ---
    # Milk
    kg.add_product("milk_brandA_1l", "Brand A Whole Milk 1L", 2.50, False, "Milk", "Brand A", ["dairy", "whole_milk"])
    kg.add_product("milk_brandB_1l", "Brand B Whole Milk 1L", 2.40, True, "Milk", "Brand B", ["dairy", "whole_milk"])
    kg.add_product("milk_brandC_1l", "Brand C Whole Milk 1L", 3.00, True, "Milk", "Brand C", ["dairy", "whole_milk", "organic"])
    kg.add_product("milk_lactose_free_brandA", "Brand A Lactose Free Milk", 3.50, True, "Milk", "Brand A", ["dairy", "lactose_free"])
    
    # Yogurt
    kg.add_product("yogurt_brandA_strawberry", "Brand A Strawberry Yogurt", 1.00, True, "Yogurt", "Brand A", ["dairy", "fruit", "sugar"])
    kg.add_product("yogurt_brandB_strawberry", "Brand B Strawberry Yogurt", 0.90, True, "Yogurt", "Brand B", ["dairy", "fruit", "sugar"])
    kg.add_product("yogurt_brandA_plain", "Brand A Plain Yogurt", 1.00, False, "Yogurt", "Brand A", ["dairy", "plain", "sugar_free"])
    kg.add_product("yogurt_brandC_plain", "Brand C Greek Yogurt", 1.50, True, "Yogurt", "Brand C", ["dairy", "plain", "sugar_free", "high_protein"])

    # --- Snacks ---
    # Chips
    kg.add_product("chips_brandX_salt", "Brand X Salted Chips", 1.50, False, "Chips", "Brand X", ["snack", "salty", "vegan"])
    kg.add_product("chips_brandY_salt", "Brand Y Salted Chips", 1.40, True, "Chips", "Brand Y", ["snack", "salty", "vegan"])
    kg.add_product("chips_brandZ_spicy", "Brand Z Spicy Chips", 1.60, True, "Chips", "Brand Z", ["snack", "spicy", "vegan"])
    
    # Chocolate
    kg.add_product("choc_brandM_milk", "Brand M Milk Chocolate", 2.00, True, "Chocolate", "Brand M", ["snack", "sweet", "dairy"])
    kg.add_product("choc_brandN_dark", "Brand N Dark Chocolate", 2.50, True, "Chocolate", "Brand N", ["snack", "sweet", "vegan", "dark_chocolate"])

    # --- Beverages ---
    # Juice
    kg.add_product("juice_brandO_orange", "Brand O Orange Juice", 3.00, False, "Juice", "Brand O", ["beverage", "fruit", "vitamin_c"])
    kg.add_product("juice_brandP_orange", "Brand P Orange Juice", 2.80, True, "Juice", "Brand P", ["beverage", "fruit", "vitamin_c"])
    kg.add_product("juice_brandQ_apple", "Brand Q Apple Juice", 2.50, True, "Juice", "Brand Q", ["beverage", "fruit"])

    return kg
