"""
this is where you define your pages (as classes with static "loadPage" functions)
and build your pages with the components you created
"""

from src import home_components



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
        home_components.component_description()


# EXAMPLE PAGE ================================================================================
class MyPage1():
    """
    Example Page class
    """
    @staticmethod
    def load_mypage1():
        """
        example page load function
        """
        home_components.component_title()


# ML PAGE ================================================================================
class MyPage2():
    """
    Example Page class
    """
    @staticmethod
    def load_mypage2():
        """
        example page load function
        """
        home_components.component_title()
