"""
this is the main module where you set your initial sessions states
and navigate your page with respect to `selected_page` session state
"""

import streamlit as st
from src.pages import HomePage, ClassificationPage, RegressionPage


# page config
st.set_page_config(page_title="My Project",
                   layout="wide",
                   initial_sidebar_state="collapsed")


# set session states
if 'selected_page' not in st.session_state:
    st.session_state['selected_page'] = 'home'


# page navigation
match st.session_state['selected_page']:
    case 'home':
        HomePage.load_home_page()

    case 'classification':
        ClassificationPage.load_classification_page()

    case 'regression':
        RegressionPage.load_regression_page()
