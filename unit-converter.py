import streamlit as st

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
    }
    
    if conversion_type not in conversion_factors:
        return None
    
    factors = conversion_factors[conversion_type]
    if from_unit in factors and to_unit in factors:
        return value * (factors[from_unit] / factors[to_unit])
    return None

st.title("Unit Converter App")

conversion_types = ["Length", "Weight", "Time"]
conversion_type = st.radio("Select Conversion Type:", conversion_types)

unit_options = {
    "Length": ["millimeters", "centimeters", "meters", "kilometers"],
    "Weight": ["grams", "kilograms", "pounds"],
    "Time": ["seconds", "minutes", "hours"],
}

st.header(f"{conversion_type} Converter")

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit:", unit_options[conversion_type])
to_unit = st.selectbox("To Unit:", unit_options[conversion_type])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, conversion_type)
    if result is not None:
        st.success(f"Converted Value: {result:.4f} {to_unit}")
    else:
        st.error("Invalid conversion")

st.markdown("Developed by **Tanzeel Sarwar**")
