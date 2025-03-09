import streamlit as st
import pandas as pd

def convert_units(value, from_unit, to_unit, conversion_type):
    conversion_factors = {
        "Length": {
            "millimeters": 0.001,
            "centimeters": 0.01,
            "meters": 1,
            "kilometers": 1000,
        },
        "Weight": {
            "grams": 1,
            "kilograms": 1000,
            "pounds": 453.592,
        },
        "Time": {
            "seconds": 1,
            "minutes": 60,
            "hours": 3600,
        },
        "Height": {
            "inches": 0.0254,
            "feet": 0.3048,
            "meters": 1,
        },
        "Temperature": {
            "Celsius": (lambda x: x, lambda x: x),
            "Fahrenheit": (lambda x: (x - 32) * 5/9, lambda x: x * 9/5 + 32),
            "Kelvin": (lambda x: x - 273.15, lambda x: x + 273.15),
        },
        "Area": {
            "square meters": 1,
            "square kilometers": 1e6,
            "square feet": 0.092903,
            "square miles": 2.59e6,
        },
        "Volume": {
            "liters": 1,
            "milliliters": 0.001,
            "cubic meters": 1000,
            "gallons": 3.785,
        },
    }
    
    if conversion_type not in conversion_factors:
        return None
    
    factors = conversion_factors[conversion_type]
    
    if conversion_type == "Temperature":
        if from_unit in factors and to_unit in factors:
            return factors[to_unit][1](factors[from_unit][0](value))
        return None
    
    if from_unit in factors and to_unit in factors:
        return value * (factors[from_unit] / factors[to_unit])
    return None

st.set_page_config(page_title="Unit Converter", page_icon="📏", layout="centered")
st.title("🌟 Advanced Unit Converter App")
st.markdown("---")

conversion_types = ["Length", "Temperature", "Area", "Volume", "Weight", "Time", "Height"]
conversion_type = st.radio("### Select Conversion Type:", conversion_types, horizontal=True)

unit_options = {
    "Length": ["millimeters", "centimeters", "meters", "kilometers"],
    "Weight": ["grams", "kilograms", "pounds"],
    "Time": ["seconds", "minutes", "hours"],
    "Height": ["inches", "feet", "meters"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Area": ["square meters", "square kilometers", "square feet", "square miles"],
    "Volume": ["liters", "milliliters", "cubic meters", "gallons"],
}

st.header(f"{conversion_type} Converter")
st.markdown("---")

col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
with col2:
    st.write("➡️")
with col3:
    from_unit = st.selectbox("From Unit:", unit_options[conversion_type])
    to_unit = st.selectbox("To Unit:", unit_options[conversion_type])

if st.button("🔄 Convert", use_container_width=True):
    result = convert_units(value, from_unit, to_unit, conversion_type)
    if result is not None:
        st.success(f"Converted Value: {result:.4f} {to_unit}")
    else:
        st.error("Invalid conversion")

st.markdown("---")
st.markdown("### 🚀 Developed by **Tanzeel Sarwar**")
