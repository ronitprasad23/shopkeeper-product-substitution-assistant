## 📌 Project Title

Shopkeeper Product Substitution Assistant

📖 Overview

This project is a Streamlit-based intelligent assistant that recommends suitable product substitutes when a requested product is unavailable. It uses a Knowledge Graph (KG) combined with rule-based reasoning to ensure explainable and constraint-aware recommendations.

## 🚀 Live App

🔗 Deployed Streamlit App:
https://shopkeeper-appuct-substitution-assistant-dhy4mt6or74k5n7chxnpz.streamlit.app/

## 🧑‍💻 How to Run Locally
git clone https://github.com/ronitprasad23/shopkeeper-product-substitution-assistant.git
cd shopkeeper-product-substitution-assistant
pip install -r requirements.txt
streamlit run app.py

🧠 Knowledge Graph (KG) Design
Nodes

Product

name

price

brand

in_stock

Attribute

tags (e.g., dairy, organic, low-fat)

Brand

Edges

HAS_ATTRIBUTE

BELONGS_TO_BRAND

SUBSTITUTABLE_WITH

The KG is built programmatically using NetworkX.

## 🔍 Search Method Used

Rule-filtered traversal over the Knowledge Graph

Candidate products are filtered by:

Stock availability

Price constraint

Required attribute tags

Preferred brand (optional)

⚙️ Rule-Based Explanation Mechanism

Each recommendation includes a human-readable explanation, such as:

“Matches required attributes”

“Within budget”

“Same brand preferred”

Rules are implemented inside find_substitutes().

🧩 Constraint Handling

Hard constraints

Must be in stock

Must be ≤ max price

Must contain required tags

Soft constraints

Preferred brand (ranking boost)