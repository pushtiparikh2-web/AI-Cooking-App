import streamlit as st

st.set_page_config(page_title="AI Cooking Assistant", layout="centered")

st.title("🍳 AI Cooking Assistant (Free Version)")
st.write("Enter a dish and number of people to get ingredients and cooking steps.")

# ----- Recipe Database (FREE, NO AI) -----

RECIPES = {
    "veg handi": {
        "ingredients": {
            "Mixed vegetables (cups)": 1,
            "Onion": 1,
            "Tomato": 1,
            "Butter (tbsp)": 1,
            "Cream (tbsp)": 1,
            "Spices (tbsp)": 0.5
        },
        "steps": [
            "Heat butter in a pan.",
            "Add chopped onions and sauté until golden.",
            "Add tomatoes and cook till soft.",
            "Add spices and mix well.",
            "Add mixed vegetables and cook for 5–7 minutes.",
            "Add cream, simmer for 3 minutes and serve hot."
        ]
    },
    "paneer butter masala": {
        "ingredients": {
            "Paneer (grams)": 100,
            "Onion": 1,
            "Tomato": 2,
            "Butter (tbsp)": 1,
            "Cream (tbsp)": 1,
            "Spices (tbsp)": 0.5
        },
        "steps": [
            "Heat butter in a pan.",
            "Add onions and sauté.",
            "Add tomato puree and cook well.",
            "Add spices and butter.",
            "Add paneer cubes and cream.",
            "Simmer for 5 minutes and serve."
        ]
    }
}

# ----- UI -----

dish = st.text_input("Dish name", placeholder="e.g. Veg Handi")
people = st.number_input("Number of people", min_value=1, step=1)

if st.button("Get Recipe") and dish:
    key = dish.strip().lower()

    if key not in RECIPES:
        st.error("Recipe not found. Try: Veg Handi or Paneer Butter Masala")
    else:
        recipe = RECIPES[key]

        st.subheader("🧺 Ingredients")
        for item, qty in recipe["ingredients"].items():
            st.write(f"- {item}: {qty * people}")

        st.subheader("👩‍🍳 Cooking Steps")
        for i, step in enumerate(recipe["steps"], start=1):
            st.write(f"{i}. {step}")

        st.subheader("🛒 Buy ingredients online")
        st.markdown("- https://blinkit.com")
        st.markdown("- https://www.swiggy.com/instamart")
        st.markdown("- https://www.zeptonow.com")
