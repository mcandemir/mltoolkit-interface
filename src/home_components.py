"""
this is where you define your components
every component is a piece of row of your application
"""

import streamlit as st
from src import callbacks


def component_title():
    """
    app title
    """
    cols = st.columns(3)
    
    with cols[1]:
        st.markdown('# Welcome to MLToolKit!')
        st.markdown('#### What is MLToolKit?')
        st.markdown("""
                    MLToolKit is a user interface where you can apply 
                    various machine learning methods with no-code and 
                    learn how they work!
                    """)


def component_buttons():
    """
    app navigation
    """
    cols = st.columns(3)

    with cols[1]:
        cols = st.columns(2)
        with cols[0]:
            st.button('🎯 Classification',
                    use_container_width=True,
                    on_click=callbacks.set_page_classification)
        
        with cols[1]:
            st.button('📈 Regression',
                    use_container_width=True,
                    on_click=callbacks.set_page_regression)


def component_mypage2_title():
    """
    example component with mypage2 page info
    """
    pass
