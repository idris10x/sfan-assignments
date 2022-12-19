import streamlit as st
from multiapp import MultiApp
from apps import quant, linearregression
st.set_page_config(layout="wide")
app = MultiApp()

# Add all your application here
app.add_app("Quantitative Stats", quant.app)
app.add_app("Linear Regression", linearregression.app)

# The main app
app.run()
