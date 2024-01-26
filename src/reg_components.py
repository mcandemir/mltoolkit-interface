"""
components of regression page 
"""

import streamlit as st
from src import callbacks


def component_homebutton():
    """
    regression home button
    """
    st.button('🏠 Home',
              on_click=callbacks.set_page_home)


def component_header():
    """
    regression page header
    """
    st.markdown('# Regression')