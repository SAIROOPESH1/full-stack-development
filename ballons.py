import streamlit as st

st.title("Hello Streamlit-er created by Sai roopesh👋")

st.markdown(
    """
    This is code used for the generate the ballons for the code.
    It can generate ballons.
    """ 
)

if st.button("Send balloons!"):
    st.balloons()