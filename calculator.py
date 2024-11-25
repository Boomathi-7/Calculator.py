import streamlit as st
import math

def calculate_square(numbers):
    return [f"{num}² = {num ** 2}" for num in numbers]

def calculate_cube(numbers):
    return [f"{num}³ = {num ** 3}" for num in numbers]

def calculate_square_root(numbers):
    return [
        f"√{num} = {math.sqrt(num)}" if num >= 0 else f"√{num} = Not defined (negative number)"
        for num in numbers
    ]

def calculate_cube_root(numbers):
    return [f"³√{num} = {math.copysign(abs(num) ** (1/3), num)}" for num in numbers]

def parse_numbers(input_text):
    try:
        return list(map(float, input_text.split(','))), None
    except ValueError:
        return None, "Error: Please enter valid numbers separated by commas."

st.title("Calculator")

st.header("Enter Numbers and Select Operation")
numbers_input = st.text_area("Enter the number:", value="")
operation = st.selectbox(
    "Select an operation to perform:",
    ["Square", "Cube", "Square Root", "Cube Root"]
)

if numbers_input:
    numbers, error = parse_numbers(numbers_input)
    
    if error:
        st.error(error)
    else:
        if operation == "Square":
            results = calculate_square(numbers)
        elif operation == "Cube":
            results = calculate_cube(numbers)
        elif operation == "Square Root":
            results = calculate_square_root(numbers)
        elif operation == "Cube Root":
            results = calculate_cube_root(numbers)

        st.header("Results")
        for result in results:
            st.write(result)
