import streamlit as st

def controller_section():
    st.header("Endpoint (Controller) Section")
    endpoints = []
    num_endpoints = st.number_input("Number of endpoints", min_value=1, max_value=10, value=1, step=1)
    for i in range(num_endpoints):
        st.subheader(f"Endpoint {i+1}")
        method = st.selectbox(f"Method {i+1}", ["GET", "POST", "PUT", "DELETE", "PATCH"], key=f"method_{i}")
        path = st.text_input(f"Path {i+1}", value=f"/resource/{i+1}", key=f"path_{i}")
        action = st.text_input(f"Action {i+1}", value="findOne", key=f"action_{i}")
        description = st.text_area(f"Description {i+1}", value="Endpoint description", key=f"desc_{i}")
        endpoints.append({
            "method": method,
            "path": path,
            "action": action,
            "description": description
        })
    return endpoints 