import streamlit as st

# Import individual page functions
from home_page import home_page
from about_page import about_page
from academics_page import academics_page
from skill_page import skill_page
from contact_page import contact_page

def set_page_config():
    """
    Set up the overall Streamlit app configuration with enhanced styling
    """
    st.set_page_config(
        page_title="Yachika Goyal | Portfolio",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def load_comprehensive_css():
    """
    Create an advanced, comprehensive global CSS for the entire application
    """
    css = """
    <style>
        /* Advanced Root Variables */
        :root {
            --background-primary: #0f172a;
            --background-secondary: #1e293b;
            --background-tertiary: #2c3e50;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent-color: #3b82f6;
            --accent-hover: #2563eb;
            --gradient-primary: linear-gradient(135deg, #4a4fe4 0%, #7b68ee 100%);
            --gradient-secondary: linear-gradient(45deg, #6a11cb 0%, #2575fc 100%);
        }

        /* Global Reset and Base Styling */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scrollbar-width: thin;
            scrollbar-color: var(--accent-color) var(--background-secondary);
        }

        /* Body and Global Styles */
        body {
            background-color: var(--background-primary) !important;
            color: var(--text-primary) !important;
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
        }

        /* Enhanced Scrollbar */
        ::-webkit-scrollbar {
            width: 10px;
        }
        ::-webkit-scrollbar-track {
            background: var(--background-secondary);
        }
        ::-webkit-scrollbar-thumb {
            background: var(--gradient-primary);
            border-radius: 5px;
        }

        /* Sidebar Advanced Styling */
        .css-1aumxhk {
            background: linear-gradient(
                to bottom, 
                var(--background-secondary) 0%, 
                var(--background-tertiary) 100%
            ) !important;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        }

        /* Navigation Menu Enhanced Styling */
        .stRadio > div {
            display: flex;
            flex-direction: column;
            gap: 15px;
            background: rgba(30, 41, 59, 0.5);
            padding: 20px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }

        .stRadio > div > label {
            background-color: transparent !important;
            color: var(--text-secondary);
            padding: 12px 20px;
            border-radius: 10px;
            transition: all 0.4s ease;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .stRadio > div > label:hover {
            background-color: var(--accent-color) !important;
            color: white !important;
            transform: translateX(10px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        /* Active Page Indicator */
        .stRadio > div > label[data-baseweb="radio"] {
            background: var(--gradient-primary) !important;
            color: white !important;
            transform: scale(1.05);
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        }

        /* Sidebar Profile Image */
        .sidebar-profile {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-bottom: 30px;
        }

        .sidebar-profile img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 5px solid var(--accent-color);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            transition: transform 0.4s ease;
        }

        .sidebar-profile img:hover {
            transform: scale(1.1) rotate(5deg);
        }

        .sidebar-profile h2 {
            margin-top: 15px;
            font-size: 1.2rem;
            color: var(--text-primary);
            text-align: center;
        }

        /* Content Area */
        .css-1dixf5 {
            padding: 2rem;
            background: linear-gradient(
                to bottom right, 
                var(--background-primary) 0%, 
                var(--background-secondary) 100%
            );
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        }

        /* Footer Styling */
        .footer {
            background: var(--background-secondary);
            color: var(--text-secondary);
            padding: 20px;
            text-align: center;
            border-top: 2px solid var(--accent-color);
            margin-top: 30px;
            border-radius: 0 0 15px 15px;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def sidebar_navigation():
    """
    Create a sophisticated sidebar navigation with modern design
    """
    # Sidebar Profile Section
    st.sidebar.markdown("""
    <div class="sidebar-profile">
        <h2>Yachika Goyal</h2>
    </div>
    """, unsafe_allow_html=True)

    # Define pages with icons
    pages = {
        "🏠 Home": home_page,
        "👤 About": about_page,
        "💼 Academics": academics_page,
        "💡 Skills": skill_page,
        "📞 Contact": contact_page
    }

    # Navigation using radio buttons
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
    
    # Load comprehensive CSS
    load_comprehensive_css()

    # Sidebar navigation
    selected_page = sidebar_navigation()

    # Render the selected page
    selected_page()

    # Enhanced Footer
    st.markdown("""
    <footer class="footer">
        © 2024 Yachika Goyal | Data Analytics & Finance Professional 
        <div style="margin-top: 10px; font-size: 0.8rem;">
            Built with ❤️ using Streamlit
        </div>
    </footer>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
