import streamlit as st
from modules.form import module_definition_form
from modules.dto import dto_section
from modules.prompt_builder import build_yaml_prompt, build_natural_language_prompt
from modules.controller import controller_section
from modules.service import service_section
import pyperclip

st.set_page_config(page_title="NestJS Prompt Generator", layout="centered")
st.title("NestJS Prompt Generator")

# Sidebar options
with st.sidebar:
    st.header("Options")
    include_swagger = st.checkbox("Include Swagger support", value=True)
    export_yaml = st.button("Export YAML as .txt")
    copy_prompt = st.button("Copy prompt to clipboard")

# Main form sections
data = {}
data.update(module_definition_form())
data["entities"] = {"User": {"id": "string", "email": "string"}}  # Dummy entity
data["dtos"] = dto_section()
data["endpoints"] = controller_section()
data["services"] = service_section()
data["swagger"] = include_swagger

# YAML and NL prompt generation
yaml_str = build_yaml_prompt(data)
nl_prompt = build_natural_language_prompt(data)

# Export options
if export_yaml:
    st.download_button("Download YAML", yaml_str, file_name="nestjs_prompt.yaml")
if copy_prompt:
    pyperclip.copy(nl_prompt)
    st.success("Prompt copied to clipboard!")
