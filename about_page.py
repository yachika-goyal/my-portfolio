import streamlit as st
import streamlit_shadcn_ui as ui

def about_page():
    # Custom CSS for the About page with enhanced design
    st.markdown("""
    <style>
        /* Advanced styling for About page */
        .about-header {
            background: linear-gradient(45deg, #3b82f6, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
            font-size: 3rem;
            margin-bottom: 2rem;
            text-align: center;
        }

        .professional-journey {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
            border-left: 5px solid #8b5cf6;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }

        .professional-journey:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        .code-text {
            background-color: rgba(139, 92, 246, 0.2);
            padding: 3px 8px;
            border-radius: 6px;
            font-family: 'Cascadia Code', monospace;
            color: #8b5cf6;
            font-weight: 600;
        }

        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            margin-top: 1.5rem;
        }

        .metric-card {
            background: linear-gradient(145deg, #ffffff, #f0f5ff);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            box-shadow: 8px 8px 16px #d1d9e6, -8px -8px 16px #ffffff;
            transition: all 0.3s ease;
        }

        .metric-card:hover {
            transform: scale(1.05);
            box-shadow: 12px 12px 24px #d1d9e6, -12px -12px 24px #ffffff;
        }

        .metric-value {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(90deg, #3b82f6, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .metric-label {
            font-size: 1rem;
            color: #64748b;
            margin-top: 10px;
        }

        .skill-container {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 1rem;
        }

        .skill-progress {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }

        .skill-name {
            flex-grow: 1;
            margin-right: 15px;
            font-weight: 600;
            color: #4a5568;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header with gradient text
    st.markdown('<h1 class="about-header">About Me</h1>', unsafe_allow_html=True)
    
    # Main content columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Professional Journey section with enhanced styling
        st.markdown("""
        <div class="professional-journey">
            <h3 style="color: #8b5cf6; margin-bottom: 15px;">Professional Journey</h3>
            
            <p>I'm a passionate <strong>full-stack developer</strong> dedicated to pushing technological boundaries, with expertise in:</p>
            
            <ul style="list-style-type: none; padding-left: 0; display: flex; gap: 10px; flex-wrap: wrap;">
                <li><span class="code-text">Web Technologies</span></li>
                <li><span class="code-text">Cloud Computing</span></li>
                <li><span class="code-text">Machine Learning</span></li>
                <li><span class="code-text">AI Solutions</span></li>
            </ul>
            
            <p>With over 6 years of experience, I craft innovative solutions that bridge cutting-edge technologies with real-world challenges, transforming complex problems into elegant, efficient systems.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Enhanced metrics design with grid layout
        st.markdown("""
        <div class="metrics-grid">
            <div class="metric-card">
                <div class="metric-value">6+</div>
                <div class="metric-label">Years Experience</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">50+</div>
                <div class="metric-label">Projects</div>
            </div>
            <div class="metric-card">
                <div class="metric-value">15+</div>
                <div class="metric-label">Technologies</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Divider
    st.markdown("---")  

    # Skills visualization with custom design
    st.markdown('<h3 style="color: #8b5cf6; text-align: center; margin-bottom: 20px;">Core Skills</h3>', unsafe_allow_html=True)
    
    # Skill progress bars with enhanced styling
    skills = {
        "Python & Data Science": 90,
        "Full-Stack Web Development": 85,
        "Cloud & DevOps": 80,
        "Machine Learning & AI": 75,
        "System Architecture": 70
    }
    
    st.markdown('<div class="skill-container">', unsafe_allow_html=True)
    for skill, percentage in skills.items():
        st.markdown(f"""
        <div class="skill-progress">
            <div class="skill-name">{skill}</div>
            <div style="width: 200px; background-color: #e2e8f0; border-radius: 10px; overflow: hidden;">
                <div style="width: {percentage}%; background: linear-gradient(90deg, #3b82f6, #8b5cf6); height: 10px; border-radius: 10px;"></div>
            </div>
            <div style="margin-left: 15px; color: #4a5568;">{percentage}%</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Call the about page function
about_page()