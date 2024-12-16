import streamlit as st
import base64

def load_enhanced_css():
    """
    Create a comprehensive custom CSS for enhanced styling and theming.
    """
    css = """
    <style>
        /* Enhanced Root Variables */
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
            transition: all 0.3s ease;
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

        /* Body and Container Styling */
        body {
            background-color: var(--background-primary);
            color: var(--text-primary);
            font-family: 'Inter', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
        }

        /* Enhanced Streamlit Container */
        .stApp {
            background-color: var(--background-primary);
            margin: 0 auto;
            padding: 2rem;
            background: linear-gradient(
                135deg, 
                var(--background-primary) 0%, 
                var(--background-secondary) 100%
            );
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            border-radius: 15px;
        }

        /* Profile Section */
        .profile-container {
            display: flex;
            align-items: center;
            gap: 30px;
            margin-bottom: 2rem;
            background: var(--background-secondary);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }

        .profile-image {
            width: 250px;
            height: 200px;
            border-radius: 50%;
            object-fit: cover;
            border: 6px solid var(--accent-color);
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            transition: transform 0.4s ease;
        }

        .profile-image:hover {
            transform: scale(1.05) rotate(5deg);
        }

        /* Typography */
        h1 {
            font-size: 3rem;
            font-weight: 900;
            background: var(--gradient-primary);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }

        h2 {
            font-size: 1.8rem;
            font-weight: 600;
            color: var(--text-secondary);
            margin-bottom: 1rem;
        }

        /* Introduction Text */
        .intro-text {
            background: rgba(30, 41, 59, 0.5);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 2rem;
            border-left: 5px solid var(--accent-color);
        }

        /* Social Icons */
        .social-icons {
            display: flex;
            justify-content: center;
            gap: 25px;
            margin-top: 30px;
            background: var(--background-secondary);
            padding: 20px;
            border-radius: 10px;
        }

        .social-icons a {
            color: var(--text-primary);
            text-decoration: none;
            transition: all 0.3s ease;
        }

        .social-icons a svg {
            width: 30px;
            height: 30px;
            stroke: var(--text-primary);
            transition: all 0.3s ease;
        }

        .social-icons a:hover svg {
            stroke: var(--accent-color);
            transform: scale(1.2) rotate(360deg);
        }

        /* Enhanced Buttons */
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }

        .custom-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 12px 25px;
            font-size: 16px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            background: var(--gradient-primary);
            color: white;
            border: none;
            border-radius: 8px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            transition: all 0.4s ease;
            text-decoration: none;
        }

        .custom-button:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 25px rgba(0,0,0,0.3);
            background: var(--gradient-secondary);
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def home_page():
    # Load enhanced CSS
    load_enhanced_css()
    
    # Profile section with enhanced layout
    st.markdown("""
    <div class="profile-container">
        <img src="http://res.cloudinary.com/dpu2z3jfg/image/upload/v1734332817/cte7vwhg6qcpesdhsoxy.jpg" alt="Yachika Goyal" class="profile-image">
        <div>
            <h1>Yachika Goyal</h1>
            <h2>Finance-Risk Manager & Data Analytics Professional</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced introduction paragraph
    st.markdown("""
    <div class="intro-text">
        <p style="color: var(--text-secondary); font-size: 1.1em; line-height: 1.8;">
        I'm Yachika Goyal, a dynamic professional passionate about leveraging data analytics in finance and risk management. With a robust background from Delhi University and ongoing FRM certification, I bridge the gap between financial expertise and analytical insights. My journey through B.Com and CA Intermediate has equipped me with a comprehensive understanding of management, accounting, and financial strategies.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Button section
    st.markdown("""
    <div class="button-container">
        <a href="https://github.com" target="_blank" class="custom-button">Written Resume</a>
        <a href="path/to/resume.pdf" target="_blank" class="custom-button">Video Resume</a>
    </div>
    """, unsafe_allow_html=True)

    # Social Media Links with SVG Icons
    st.markdown("""
    <div class="social-icons">
        <a href="https://www.linkedin.com/in/yachika-goyal-394a9a340/" target="_blank" title="LinkedIn">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                <rect x="2" y="9" width="4" height="12"></rect>
                <circle cx="4" cy="4" r="2"></circle>
            </svg>
        </a>
        <a href="https://github.com/yachika-goyal" target="_blank" title="GitHub">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
            </svg>
        </a>
        <a href="https://x.com/Yachika_Goyal" target="_blank" title="Twitter (X)">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5.4c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"></path>
            </svg>
        </a>
    </div>
    """, unsafe_allow_html=True)
