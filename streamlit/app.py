import streamlit as st


number = st.sidebar.slider("Pick a Num", 0, 100, 50)

st.sidebar.write(f"number: {number}")


left_col, center_col, right_col = st.columns(3)
left_col.slider("Pick a Num", 0, 100)
center_col.slider("middle column", 0, 100)
right_col.slider("right column", 0, 100)
