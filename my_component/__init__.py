import streamlit.components.v1 as components
import os

_component_func = components.declare_component(
    "my_component",
    # Build된 Static을 어떻게 연결할 것인가에 대한 방법은 더 연구가 필요함.
    # path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend/build"),
    url="http://localhost:3000"
)

def my_component(name, key=None):
    component_value = _component_func(name=name, key=key)
    return component_value