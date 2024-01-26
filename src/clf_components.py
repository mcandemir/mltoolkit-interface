"""
components of classification page 
"""

import streamlit as st
from src import callbacks
import pandas as pd


def component_homebutton():
    """
    regression home button
    """
    st.button('**🏠 Home**',
              on_click=callbacks.set_page_home)
    

def component_header():
    """
    classificaton page header
    """
    st.markdown('# Classification')
    st.markdown('Here you can train classification models.')
    st.markdown('---')


def component_data():
    """
    classification page data preparing
    """
    # init variables that may not initialized
    data_file = None

    st.markdown('### Data')

    cols = st.columns(5)
    
    with cols[0]:
        st.markdown('In order to begin, you will need to provide your datasets. Or, you can give it a try by using built-in datasets!')
        radio_input = st.radio('Data:', 
                               options=[
                                   'Custom',
                                   'Built-in'
                                   ])


    with cols[1]:
        match(radio_input):
            case 'Custom':
                data_file = st.file_uploader('**Upload Training Data:**')
                data_file = st.file_uploader('**Upload Test Data:**')
            
            case 'Built-in':
                st.selectbox('**Available Datasets:**',
                             options=['Iris', 'California Housing', 'Wine Quality'])

    
    with cols[3]:
        if data_file:
            data = pd.read_csv(data_file)
            st.dataframe(data, use_container_width=True, height=108)




