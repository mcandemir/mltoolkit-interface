"""
this is where you define your components
every component is a piece of row of your application
"""

import streamlit as st
from src import callbacks


def component_title():
    """
    example component with a home button and header
    """
    st.markdown('# Welcome to MLToolKit!')
    


def component_description():
    """
    example component with a page selection
    """
    st.markdown('#### What is MLToolKit?')
    st.markdown('MLToolKit is a user interface where you can apply various machine learning methods with no-code and learn how they work!')

def component_mypage1_title():
    """
    example component with mypage1 page info
    """
    st.write('My Page 1')

def component_mypage2_title():
    """
    example component with mypage2 page info
    """
    st.write('My Page 2')
