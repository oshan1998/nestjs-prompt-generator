import streamlit as st

def module_definition_form():
    st.header("Module Definition")
    module_name = st.text_input("Module Name", value="User")
    module_description = st.text_area("Module Description", value="Handles user management.")
    return {
        "name": module_name,
        "description": module_description
    }
