

import streamlit as st
# import streamlit_shadcn_ui as ui
# from pathlib import Path
# import base64

# Import individual page functions
from home_page import home_page
from about_page import about_page
from skill_page import skill_page
from projects_page import projects_page
from experience_page import experience_page
from contact_page import contact_page

# Additional page imports would go here (projects, contact, etc.)

def set_page_config():
    """
    Set up the overall Streamlit app configuration and custom styling
    """
    st.set_page_config(
        page_title="Alex Rodriguez | Portfolio",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def load_global_css():
    """
    Create a comprehensive global CSS for the entire application
    """
    css = """
    <style>
        /* Root color variables */
        :root {
            --background-primary: #0f172a;
            --background-secondary: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent-color: #3b82f6;
            --accent-hover: #2563eb;
        }

        /* Global reset and base styles */
        body {
            background-color: var(--background-primary) !important;
            color: var(--text-primary) !important;
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Sidebar customization */
        .css-1aumxhk {
            background-color: var(--background-secondary) !important;
        }

        /* Navigation menu styling */
        .stRadio > div {
            display: flex;
            justify-content: space-between;
            background-color: var(--background-secondary);
            padding: 10px;
            border-radius: 10px;
        }

        .stRadio > div > label {
            background-color: transparent !important;
            color: var(--text-secondary);
            padding: 8px 16px;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .stRadio > div > label:hover {
            background-color: var(--accent-color) !important;
            color: white !important;
        }

        /* Active page indicator */
        .stRadio > div > label[data-baseweb="radio"] {
            background-color: var(--accent-color) !important;
            color: white !important;
        }

        /* Scrollbar styling */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: var(--background-secondary);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--accent-color);
            border-radius: 4px;
        }

        /* Content area padding */
        .css-1dixf5 {
            padding: 2rem;
            background-color: var(--background-primary);
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def sidebar_navigation():
    """
    Create a custom sidebar navigation with modern styling
    """
    # Add custom logo or profile picture (optional)
    st.sidebar.markdown("""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <img src="https://via.placeholder.com/150" style="border-radius: 50%; width: 100px; height: 100px; object-fit: cover; border: 4px solid #3b82f6;">
    </div>
    """, unsafe_allow_html=True)

    # Navigation menu
    pages = {
        "Home": home_page,
        "About": about_page,
        "Skill": skill_page,
        "Projects": projects_page,
        "Experience": experience_page,
        "Contact": contact_page,
        # Add more pages here as you create them
        # "Projects": projects_page,
        # "Contact": contact_page
    }

    # Use radio buttons for navigation
    page_names = list(pages.keys())
    selected_page_index = st.sidebar.radio(
        "Navigate", 
        page_names, 
        index=0,
        label_visibility="collapsed"
    )

    # Return the selected page function
    return pages[selected_page_index]

def main():
    # Set up page configuration
    set_page_config()
    
    # Load global CSS
    load_global_css()

    # Sidebar navigation
    selected_page = sidebar_navigation()

    # Render the selected page
    selected_page()

    # Optional: Footer
    st.markdown("""
    <footer style="text-align: center; color: var(--text-secondary); padding: 20px; margin-top: 20px;">
        © 2024 Alex Rodriguez | Built with Streamlit
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()