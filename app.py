import streamlit as st
from openai import OpenAI

# Page setup
st.set_page_config(page_title="AI Cooking Assistant", layout="centered")

st.title("🍳 AI Cooking Assistant")
st.write("Enter a dish and number of people to get ingredients and cooking steps.")

# OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_recipe(dish, people):
    prompt = f"""
You are a professional cooking assistant.

Dish: {dish}
Number of people: {people}

Generate:
1. Ingredients with quantities adjusted for the number of people
2. Clear step-by-step cooking instructions

Use simple language.
No prices.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return response.choices[0].message.content

# Inputs
dish = st.text_input("Dish name", placeholder="e.g. Paneer Butter Masala")
people = st.number_input("Number of people", min_value=1, step=1)

# Button
if st.button("Get Recipe") and dish:
    with st.spinner("Generating recipe..."):
        recipe = generate_recipe(dish, people)

    st.subheader("📋 Recipe")
    st.write(recipe)

    st.subheader("🛒 Buy ingredients online")
    st.markdown("- https://blinkit.com")
    st.markdown("- https://www.swiggy.com/instamart")
    st.markdown("- https://www.zeptonow.com")
