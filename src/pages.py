"""
this is where you define your pages (as classes with static "loadPage" functions)
and build your pages with the components you created
"""

from src import home_components, clf_components, reg_components



# HOME PAGE ================================================================================
class HomePage():
    """
    Your Home / Landing Page
    Here you can add your defined components under the loadPage() function
    """
    @staticmethod
    def load_home_page():
        """
        example home page load function
        """
        home_components.component_title()
        home_components.component_buttons()


# EXAMPLE PAGE ================================================================================
class ClassificationPage():
    """
    Example Page class
    """
    @staticmethod
    def load_classification_page():
        """
        example page load function
        """
        clf_components.component_homebutton()
        clf_components.component_header()
        clf_components.component_data()



# ML PAGE ================================================================================
class RegressionPage():
    """
    Example Page class
    """
    @staticmethod
    def load_regression_page():
        """
        example page load function
        """
        
        reg_components.component_homebutton()
        reg_components.component_header()
