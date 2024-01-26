"""
this is where you define your callbacks
"""

import streamlit as st


def set_page_home():
    """
    example callback that will set the selected page to 'home'
    """
    st.session_state['selected_page'] = 'home'


def set_page_classification():
    """
    example callback that will set the selected page to 'mypage1'
    """
    st.session_state['selected_page'] = 'classification'


def set_page_regression():
    """
    example callback that will set the selected page to 'mypage2'
    """
    st.session_state['selected_page'] = 'regression'

def set_state_something():
    """
    example callback with empty template
    """
    st.session_state['state'] = 'something'
