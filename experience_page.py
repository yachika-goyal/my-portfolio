import streamlit as st
import streamlit_shadcn_ui as ui
from datetime import datetime

def experience_page():
    # Comprehensive Custom CSS for Experience Page
    st.markdown("""
    <style>
        /* Experience Page Global Styles */
        .experience-header {
            background: linear-gradient(45deg, #3b82f6, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
            font-size: 3rem;
            margin-bottom: 2.5rem;
            text-align: center;
            line-height: 1.2;
        }

        .timeline-container {
            position: relative;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px 0;
        }

        .timeline-container::before {
            content: '';
            position: absolute;
            width: 4px;
            background: linear-gradient(to bottom, #3b82f6, #8b5cf6);
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -2px;
            border-radius: 10px;
        }

        .timeline-item {
            padding: 20px 40px;
            position: relative;
            width: 50%;
            background: transparent;
            margin-bottom: 30px;
            border-radius: 15px;
            transition: all 0.3s ease;
        }

        .timeline-item:nth-child(even) {
            margin-left: 50%;
        }

        .timeline-item::before {
            content: '';
            position: absolute;
            width: 25px;
            height: 25px;
            background: linear-gradient(45deg, #3b82f6, #8b5cf6);
            border-radius: 50%;
            top: 50%;
            transform: translateY(-50%);
            z-index: 1;
            box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.2);
        }

        .timeline-item:nth-child(odd)::before {
            right: -12.5px;
        }

        .timeline-item:nth-child(even)::before {
            left: -12.5px;
        }

        .timeline-content {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.05), rgba(139, 92, 246, 0.05));
            border: 1px solid rgba(139, 92, 246, 0.1);
            border-radius: 15px;
            padding: 25px;
            position: relative;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            transition: all 0.3s ease;
        }

        .timeline-content:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            border-color: rgba(139, 92, 246, 0.2);
        }

        .role-title {
            color: #8b5cf6;
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 10px;
        }

        .company-name {
            color: #4a5568;
            font-weight: 600;
            margin-bottom: 10px;
        }

        .duration {
            color: #64748b;
            font-style: italic;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .duration-icon {
            color: #8b5cf6;
        }

        .experience-description {
            color: #4a5568;
            line-height: 1.6;
        }

        .achievement-badge {
            background-color: rgba(139, 92, 246, 0.1);
            color: #8b5cf6;
            padding: 3px 8px;
            border-radius: 15px;
            font-size: 0.8rem;
            margin-right: 8px;
            margin-bottom: 8px;
            display: inline-block;
            font-weight: 600;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<h1 class="experience-header">Professional Journey</h1>', unsafe_allow_html=True)

    # Enhanced Experience Data
    experiences = [
        {
            "role": "Senior Software Engineer",
            "company": "TechInnovate Solutions",
            "duration": "2020 - Present",
            "description": "Spearheading the development of cloud-native applications with a focus on microservices architecture and scalable solutions.",
            "achievements": [
                "Reduced infrastructure costs by 40%",
                "Led team of 5 developers",
                "Implemented advanced CI/CD pipelines"
            ],
            "technologies": ["Kubernetes", "AWS", "Microservices", "DevOps"]
        },
        {
            "role": "Software Developer",
            "company": "Digital Dynamics Inc.",
            "duration": "2018 - 2020",
            "description": "Developed innovative web applications and integrated complex systems, focusing on full-stack development and performance optimization.",
            "achievements": [
                "Improved application performance by 65%",
                "Developed 3 major client-facing platforms",
                "Implemented machine learning integrations"
            ],
            "technologies": ["React", "Node.js", "Machine Learning", "GraphQL"]
        },
        {
            "role": "Junior Software Engineer",
            "company": "Innovative Tech Labs",
            "duration": "2016 - 2018",
            "description": "Gained foundational experience in software development, working on diverse projects and learning cutting-edge technologies.",
            "achievements": [
                "Received 'Rising Talent' award",
                "Contributed to open-source projects",
                "Developed internal productivity tools"
            ],
            "technologies": ["Python", "Django", "Agile Methodologies", "Cloud Computing"]
        }
    ]

    # Timeline Container
    st.markdown('<div class="timeline-container">', unsafe_allow_html=True)

    # Experience Timeline
    for idx, exp in enumerate(experiences):
        st.markdown(f'''
        <div class="timeline-item">
            <div class="timeline-content">
                <div class="role-title">{exp['role']}</div>
                <div class="company-name">{exp['company']}</div>
                <div class="duration">
                    <span>⏱️</span> {exp['duration']}
                </div>
                <div class="experience-description">
                    {exp['description']}
                </div>
                <div style="margin-top: 15px;">
                    <strong style="color: #8b5cf6;">Key Achievements:</strong>
                    {''.join(f'<span class="achievement-badge">{achievement}</span>' for achievement in exp['achievements'])}
                </div>
                <div style="margin-top: 15px;">
                    <strong style="color: #8b5cf6;">Technologies:</strong>
                    {''.join(f'<span class="achievement-badge">{tech}</span>' for tech in exp['technologies'])}
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Additional Professional Summary
    st.markdown("---")
    
    # Professional Summary Section
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        ### Professional Summary
        A passionate and innovative software engineer with over 6 years of experience in developing cutting-edge technology solutions. 
        Proven track record of delivering high-performance, scalable applications across multiple domains including cloud computing, 
        web development, and machine learning.
        """)
    
    with col2:
        # Professional Metrics
        st.markdown("""
        ### Quick Stats
        - 🚀 3+ Companies
        - 💻 15+ Projects
        - 🏆 5+ Major Achievements
        """)

# Call the experience page function
experience_page()