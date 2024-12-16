import streamlit as st

def contact_page():
    # Comprehensive Custom CSS for Contact Page
    st.markdown("""
    <style>
        .contact-header {
            background: linear-gradient(45deg, #3b82f6, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
            font-size: 3rem;
            margin-bottom: 2.5rem;
            text-align: center;
            line-height: 1.2;
        }

        .contact-container {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.05), rgba(139, 92, 246, 0.05));
            border-radius: 20px;
            padding: 40px;
            border: 1px solid rgba(139, 92, 246, 0.1);
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        }

        .contact-form {
            background-color: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            border: 1px solid rgba(139, 92, 246, 0.1);
            transition: all 0.3s ease;
            width: 100%;
            max-width: 700px;
        }

        .contact-form:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        .stTextInput > div > div > input, .stTextArea > div > div > textarea {
            border-radius: 10px !important;
            border: 1px solid #e2e8f0 !important;
            padding: 12px 15px !important;
            transition: all 0.3s ease !important;
        }

        .stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
            border-color: #8b5cf6 !important;
            box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.1) !important;
        }

        .contact-submit {
            background: linear-gradient(90deg, #3b82f6, #8b5cf6) !important;
            color: white !important;
            border: none !important;
            border-radius: 25px !important;
            padding: 12px 25px !important;
            font-weight: 600 !important;
            transition: transform 0.3s ease !important;
        }

        .contact-submit:hover {
            transform: scale(1.05) !important;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2) !important;
        }

        .contact-info {
            background: linear-gradient(135deg, #f0f5ff, #f5f3ff);
            border-radius: 15px;
            padding: 30px;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            border: 1px solid rgba(139, 92, 246, 0.1);
            transition: all 0.3s ease;
        }

        .contact-info:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        .contact-social {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }

        .social-link {
            background-color: rgba(139, 92, 246, 0.1);
            color: #8b5cf6;
            border-radius: 50%;
            width: 50px;
            height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            text-decoration: none !important;
        }

        .social-link:hover {
            background-color: rgba(139, 92, 246, 0.2);
            transform: scale(1.1);
        }

        .form-instructions {
            font-size: 1.1rem;
            margin-bottom: 20px;
        }

        .contact-text {
            font-size: 0.9rem;
            color: #6b7280;
            margin-top: 15px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<h1 class="contact-header">Contact Me</h1>', unsafe_allow_html=True)

    # Columns for Form and Contact Info
    col1, col2 = st.columns([2, 1])

    with col1:
        with st.form("contact_form", clear_on_submit=True):
            st.markdown("### Send me a Message")
            
            # Form instructions
            st.markdown('<div class="form-instructions">Please provide your details and message, and I\'ll get back to you as soon as possible!</div>', unsafe_allow_html=True)
            
            # Form fields
            name = st.text_input("Name", placeholder="Your Full Name", label_visibility="collapsed")
            email = st.text_input("Email", placeholder="Your Email Address", label_visibility="collapsed")
            message = st.text_area("Message", placeholder="Write your message here...", label_visibility="collapsed", height=200)
            
            # Submit button
            submit = st.form_submit_button("Send Message", use_container_width=True, help="Click to send your message")
            
            if submit:
                # Basic validation
                if not name or not email or not message:
                    st.error("Please fill out all fields.")
                elif "@" not in email:
                    st.error("Please enter a valid email address.")
                else:
                    # Simulated message sending (replace with actual backend logic)
                    st.success("Message sent successfully! I'll get back to you soon.")
            
            st.markdown('<div class="contact-text">Your data will remain confidential, and I will respond within 2-3 business days.</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown("### Let's Connect")
        
        # Contact Details
        st.markdown("""
        Feel free to reach out through any of these channels. 
        I'm always open to discussing new projects, collaborations, or opportunities in tech.
        """)
        
        # Social Links
        st.markdown("""
        <div class="contact-social">
            <a href="https://www.linkedin.com/in/yachika-goyal-394a9a340/" class="social-link" target="_blank">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path>
                    <rect x="2" y="9" width="4" height="12"></rect>
                    <circle cx="4" cy="4" r="2"></circle>
                </svg>
            </a>
            <a href="https://github.com/yachika-goyal" class="social-link" target="_blank">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
                </svg>
            </a>
            <a href="mailto:yachikagoyal2004@gmail.com" class="social-link" target="_blank">
                <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                    <polyline points="22,6 12,13 2,6"></polyline>
                </svg>
            </a>
        </div>
        """, unsafe_allow_html=True)
