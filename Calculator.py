import streamlit as st
import os

# header
st.header("Calculator Suhu - Streamlit", divider='rainbow')

# variable input 
suhu = st.number_input(label="Masukan Suhu : ".upper())

# column 2
col1, col2 = st.columns(2)

# option
with col1:
    option = st.selectbox(
       "**Convert From** : ".upper(),
       ("Celcius", "Reamur", "Fahrenheit", "Kelvin"),
       placeholder="Select First Option",
    )

with col2:
    option2 = st.selectbox(
       "**Convert To** : ".upper(),
       ("Celcius", "Reamur", "Fahrenheit", "Kelvin"),
       placeholder="Select Second Option",
    )

def calculate():
    # error 
    if option == "Celcius" and option2 == "Celcius":
        hasil = suhu
        st.code(f"{hasil}°C")
    elif option == "Reamur" and option2 == "Reamur":
        hasil = suhu
        st.code(f"{hasil}°R")
    elif option == "Fahrenheit" and option2 == "Fahrenheit":
        hasil = suhu
        st.code(f"{hasil}°F")
    elif option == "Kelvin" and option2 == "Kelvin":
        hasil = suhu
        st.code(f"{hasil}°K")

    # Celcius 
    elif option == "Celcius" and option2 == "Reamur":
        hasil = 4/5*suhu
        st.code(f"{hasil}°C")
    elif option == "Celcius" and option2 == "Fahrenheit":
        hasil = 9/5*suhu+32
        st.code(f"{hasil}°C")
    elif option == "Celcius" and option2 == "Kelvin":
        hasil = suhu+273
        st.code(f"{hasil}°C")

    # Reamur 
    elif option == "Reamur" and option2 == "Celcius":
        hasil = 5/4*suhu
        st.code(f"{hasil}°R")
    elif option == "Reamur" and option2 == "Fahrenheit":
        hasil = 9/4*suhu+32
        st.code(f"{hasil}°R")
    elif option == "Reamur" and option2 == "Kelvin":
        hasil = 5/4*suhu+273
        st.code(f"{hasil}°R")

    # Fahrenheit 
    elif option == "Fahrenheit" and option2 == "Celcius":
        hasil = 5/9*(suhu-32)
        st.code(f"{hasil}°F")
    elif option == "Fahrenheit" and option2 == "Reamur":
        hasil = 4/9*(suhu-32)
        st.code(f"{hasil}°F")
    elif option == "Fahrenheit" and option2 == "Kelvin":
        hasil = 5/9*(suhu-32)+273
        st.code(f"{hasil}°F")

    # Kelvin 
    elif option == "Kelvin" and option2 == "Celcius":
        hasil = suhu-273
        st.code(f"{hasil}°K")
    elif option == "Kelvin" and option2 == "Reamur":
        hasil = 4/5*(suhu-273)
        st.code(f"{hasil}°K")
    elif option == "Kelvin" and option2 == "Fahrenheit":
        hasil = 9/5*(suhu-273)+32
        st.code(f"{hasil}°K")

    else:
        st.code(f"Undefined Error!.")

if st.button("Convert it!.", type="primary", use_container_width=True):
    calculate()
st.write("---")
st.markdown("Happy Streamlit-ing! :balloon:. :copyright: 2023 [Justikail]('https://github.com/justikail/')")