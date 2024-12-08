import streamlit as st
import base64

def load_css():
    """
    Create a custom CSS for enhanced styling and theming.
    """
    css = """
    <style>
        /* Root variables for easy theming */
        :root {
            --background-primary: #0f172a;
            --background-secondary: #1e293b;
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent-color: #3b82f6;
            --accent-hover: #2563eb;
        }

        /* Custom scrollbar */
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

        /* Body and main container styling */
        body {
            background-color: var(--background-primary);
            color: var(--text-primary);
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Button styling */
        .stButton > button {
            background-color: var(--accent-color) !important;
            color: white !important;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background-color: var(--accent-hover) !important;
            transform: scale(1.05);
        }

        /* Responsive Typography */
        h1 {
            font-size: 2.5rem;
            font-weight: 800;
            margin-bottom: 0.5rem;
        }

        h2 {
            font-size: 1.5rem;
            font-weight: 500;
            color: var(--text-secondary);
        }

        /* Profile picture container */
        .profile-container {
            display: flex;
            align-items: center;
            gap: 20px;
            margin-bottom: 1rem;
        }

        .profile-image {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            border: 4px solid var(--accent-color);
        }

        /* Social Media Icons */
        .social-icons {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }

        .social-icons a {
            color: var(--text-primary);
            font-size: 1.5rem;
            transition: color 0.3s;
        }

        .social-icons a:hover {
            color: var(--accent-color);
        }

        /* Button container */
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }

        /* Custom button styles */
        .custom-button {
            display: inline-block;
            position: relative;
            padding: 12px 25px;
            font-size: 16px;
            font-weight: 500;
            color: white;
            background: linear-gradient(135deg, #4a4fe4 0%, #7b68ee 100%);
            border: none;
            border-radius: 6px;
            text-transform: none;
            letter-spacing: 0.5px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
            transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.3s ease;
            cursor: pointer;
            overflow: hidden;
        }

        .custom-button:hover {
            background: linear-gradient(135deg, #5a70e7 0%, #8a75f1 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.12), 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def home_page():
    # Load custom CSS
    load_css()
    
    # Add gradient background
    st.markdown('<div class="page-background"></div>', unsafe_allow_html=True)
    
    # Profile section
    st.markdown("""
    <div class="profile-container">
        <img src="https://via.placeholder.com/150" alt="Yachika Goyal" class="profile-image">
        <div>
            <h1>Hi, I'm <span style="color: var(--accent-color);">Yachika Goyal</span></h1>
            <h2>Finance-Risk Manager and Data Analytics</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction paragraph
    st.markdown("""
    <p style="color: var(--text-secondary); font-size: 1.1em; line-height: 1.6;">
    I'm Yachika Goyal, and I'm working on improving my data analytics abilities while obtaining the FRM certification. I hold a B.Com. from DU SOL and have a solid background in management, accounting, and finance, which has been strengthened by my attempts at a CA Intermediate. I'm enthusiastic in combining analytics and finance to produce significant outcomes.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
        # Add a button centered within the column with custom styling
        st.markdown(
            '''
            <div class="button-container">
                <a href="https://github.com" target="_blank" class="custom-button">Written Resume</a>
            </div>
            ''',
            unsafe_allow_html=True
        )

    with col2:
        # Add a button centered within the column with custom styling
        st.markdown(
            '''
            <div class="button-container">
                <a href="path/to/resume.pdf" target="_blank" class="custom-button">Video Resume</a>
            </div>
            ''',
            unsafe_allow_html=True
        )

    # Social Media Links
    st.markdown("""
    <div class="social-icons">
        <a href="https://www.linkedin.com/in/yachika-goyal-394a9a340/" target="_blank">🐦</a>
        <a href="https://github.com/yachika-goyal" target="_blank">🔗</a>
        <a href="https://x.com/Yachika_Goyal" target="_blank">🐙</a>
    </div>
    """, unsafe_allow_html=True)

# Call the home page function
home_page()
