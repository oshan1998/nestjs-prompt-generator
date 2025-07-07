import streamlit as st

def service_section():
    st.header("Service Section")
    services = []
    num_services = st.number_input("Number of services", min_value=1, max_value=10, value=1, step=1)
    for i in range(num_services):
        st.subheader(f"Service {i+1}")
        service_name = st.text_input(f"Service Name {i+1}", value=f"Service{i+1}", key=f"service_name_{i}")
        num_methods = st.number_input(f"Number of methods for {service_name}", min_value=1, max_value=10, value=1, step=1, key=f"num_methods_{i}")
        methods = []
        for j in range(num_methods):
            st.write(f"Method {j+1}:")
            method_name = st.text_input(f"Method Name {j+1}", value=f"method{j+1}", key=f"method_name_{i}_{j}")
            return_type = st.text_input(f"Return Type {j+1}", value="Promise<any>", key=f"return_type_{i}_{j}")
            description = st.text_area(f"Description {j+1}", value="Method description", key=f"method_desc_{i}_{j}")
            methods.append({
                "name": method_name,
                "return_type": return_type,
                "description": description
            })
        services.append({
            "name": service_name,
            "methods": methods
        })
    return services 