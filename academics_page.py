import streamlit as st

def academics_page():
    # Custom CSS for styling
    st.markdown("""
    <style>
        .academics-header {
            background: linear-gradient(45deg, #3b82f6, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
            font-size: 3rem;
            margin-bottom: 2rem;
            text-align: center;
        }
        .academics-card {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.05), rgba(139, 92, 246, 0.05));
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }
        .academics-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        .degree-title {
            color: #8b5cf6;
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 5px;
        }
        .institution-name {
            color: #4a5568;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .duration {
            color: #64748b;
            font-style: italic;
            margin-bottom: 15px;
        }
        .description {
            color: #4a5568;
            line-height: 1.5;
        }
        .badge {
            display: inline-block;
            background-color: rgba(139, 92, 246, 0.1);
            color: #8b5cf6;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 0.8rem;
            margin-right: 5px;
            margin-bottom: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<h1 class="academics-header">Academic Journey</h1>', unsafe_allow_html=True)

    # Academics Data
    academics = [
        {
            "degree": "CA Intermediate",
            "institution": "ICAI",
            "duration": "Attempted 2-3 times",
            "description": "Gained comprehensive knowledge of accounting, auditing, and financial management through rigorous preparation and exams.",
            "achievements": ["Strong grasp of accountancy principles", "Exposure to financial and risk management"],
            "skills": ["Tally", "Excel", "Financial Analysis"]
        },
        {
            "degree": "B.Com Graduate",
            "institution": "Delhi University (School of Open Learning)",
            "duration": "Completed in 2022",
            "description": "Developed a strong foundation in finance, accounting, and business management principles.",
            "achievements": ["Consistent academic performance", "Specialized in finance and accounting"],
            "skills": ["MS Office", "Business Analytics"]
        },
        {
            "degree": "FRM Studies",
            "institution": "GARP",
            "duration": "Ongoing",
            "description": "Currently pursuing the Financial Risk Manager certification to enhance expertise in financial analytics and risk assessment.",
            "achievements": ["In-depth understanding of financial risks", "Focus on quantitative modeling"],
            "skills": ["R", "Python", "Risk Models"]
        }
    ]

    # Render Academics Cards in Two Columns
    col1, col2 = st.columns(2, gap="large")

    for idx, acad in enumerate(academics):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(f"""
            <div class="academics-card">
                <div class="degree-title">{acad['degree']}</div>
                <div class="institution-name">{acad['institution']}</div>
                <div class="duration">{acad['duration']}</div>
                <div class="description">{acad['description']}</div>
                <div>
                    <strong>Key Achievements:</strong>
                    {''.join(f'<span class="badge">{ach}</span>' for ach in acad['achievements'])}
                </div>
                <div style="margin-top: 10px;">
                    <strong>Skills:</strong>
                    {''.join(f'<span class="badge">{skill}</span>' for skill in acad['skills'])}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Additional Academic Summary
    st.markdown("---")

    # Academic Summary Section
    col1, col2 = st.columns([3, 2])

    with col1:
        st.markdown("""
        ### Academic Summary
        A committed learner with a solid academic foundation in commerce and finance, complemented by a growing expertise in data analytics 
        and risk management. Dedicated to leveraging education to solve real-world challenges and achieve professional excellence.
        """)

    with col2:
        # Academic Stats
        st.markdown("""
        ### Quick Stats
        - 🎓 2+ Major Degrees/Certifications
        - 📘 5+ Specialized Subjects
        - 🌟 Continuous Learning
        """)

# Update function call
def main():
    st.set_page_config(
        page_title="Academic Journey",
        page_icon=":mortar_board:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    academics_page()

if __name__ == "__main__":
    main()
