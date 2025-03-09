import streamlit as st

def convert_units(value, from_unit, to_unit, conversion_type):
    conversions = {
        "Length": {"millimeters": 0.001, 
                   "centimeters": 0.01, 
                   "meters": 1, 
                   "kilometers": 1000},
        "Weight": {"grams": 1, 
                   "kilograms": 1000, 
                   "pounds": 453.592},
        "Time": {"seconds": 1, 
                 "minutes": 60, 
                 "hours": 3600},
        "Height": {"inches": 0.0254, 
                   "feet": 0.3048, 
                   "meters": 1},
        "Temperature": {"Celsius": "C", 
                        "Fahrenheit": "F", 
                        "Kelvin": "K"},
        "Area": {"square meters": 1, 
                 "square kilometers": 1e6, 
                 "square feet": 0.092903, 
                 "square miles": 2.59e6},
        "Volume": {"liters": 1, 
                   "milliliters": 0.001, 
                   "cubic meters": 1000, 
                   "gallons": 3.785},
    }
    
    if conversion_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return None
    
    if from_unit in conversions[conversion_type] and to_unit in conversions[conversion_type]:
        return value * (conversions[conversion_type][from_unit] / conversions[conversion_type][to_unit])
    return None

st.title("Simple Unit Converter App")

conversion_types = ["Length", "Temperature", "Area", "Volume", "Weight", "Time", "Height"]
conversion_type = st.radio("Select Conversion Type:", conversion_types)

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

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit:", unit_options[conversion_type])
to_unit = st.selectbox("To Unit:", unit_options[conversion_type])

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, conversion_type)
    if result is not None:
        st.success(f"Converted Value: {result:.4f} {to_unit}")
    else:
        st.error("Invalid conversion")

st.markdown("Developed by **Iffat ul Fatima**")
