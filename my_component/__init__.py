import streamlit.components.v1 as components
import os

_component_func = components.declare_component(
    "my_component",
    # path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend"),
    url="http://localhost:3000"
)

def my_component(name, key=None):
    component_value = _component_func(name=name, key=key)
    return component_value