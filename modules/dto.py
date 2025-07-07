import streamlit as st

def dto_section():
    st.header("DTO Section")
    num_dtos = st.number_input("Number of DTOs", min_value=1, max_value=10, value=2, step=1)
    dtos = {}
    for i in range(num_dtos):
        dto_name = st.text_input(f"DTO Name {i+1}", value=f"dto{i+1}", key=f"dto_name_{i}")
        fields = st.text_area(f"Fields for {dto_name} (name:type per line)", value="id:string\nemail:string", key=f"dto_fields_{i}")
        dtos[dto_name] = fields
    return dtos
