import streamlit as st
import pandas as pd

st.title("Sample App")

df = pd.DataFrame({"1列目": [1, 2, 3, 4], "2列目": [5, -2, -3, -4]})

st.dataframe(df.style.highlight_max(axis=1), width=200, height=200)

st.json(
    {
        "data": {
            "name": "abc",
            "age": 123,
        }
    }
)
