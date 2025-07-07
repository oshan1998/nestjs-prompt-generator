import streamlit as st
import yaml

def build_yaml_prompt(data):
    st.header("YAML Prompt Generator")
    yaml_str = yaml.dump(data, sort_keys=False)
    st.code(yaml_str, language="yaml")
    return yaml_str

def build_natural_language_prompt(data):
    st.header("Natural Language Prompt Generator")
    # Dummy example
    prompt = f"Generate a NestJS module named {data.get('name', 'Module')}. It has an entity with fields ..."
    st.code(prompt, language="markdown")
    return prompt
