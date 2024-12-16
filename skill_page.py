import streamlit as st

def skill_page():
    st.header("💻 Technical Skills")
    
    # Define skills with additional metadata
    skills = {
        "Programming Languages": [
            {"name": "Python", "level": 95, "icon": "🐍"},
            {"name": "R", "level": 85, "icon": "📊"},
            {"name": "SQL", "level": 80, "icon": "🔍"}
        ],
        "Data Science Tools": [
            {"name": "Pandas", "level": 90, "icon": "📂"},
            {"name": "NumPy", "level": 85, "icon": "🔢"},
            {"name": "Scikit-learn", "level": 80, "icon": "🤖"}
        ],
        "Visualization Tools": [
            {"name": "Matplotlib", "level": 88, "icon": "📈"},
            {"name": "Seaborn", "level": 85, "icon": "📊"},
            {"name": "Tableau", "level": 80, "icon": "📊"}
        ],
        "Machine Learning & AI": [
            {"name": "TensorFlow", "level": 78, "icon": "🔗"},
            {"name": "Keras", "level": 75, "icon": "🧠"},
            {"name": "PyTorch", "level": 72, "icon": "🔥"}
        ]
    }
    
    # Custom styling with dark theme
    st.markdown("""
    <style>
    .stApp {
        background-color: #1a1b1e;
        color: #e5e5e5;
    }
    .skill-container {
        background-color: #2b2d31;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        transition: transform 0.3s ease;
    }
    .skill-container:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stProgress > div > div {
        background-color: #4CAF50 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Iterate through skill categories
    for category, skill_list in skills.items():
        st.subheader(category)
        
        # Create columns for skills
        cols = st.columns(len(skill_list))
        
        # Display skills in containers
        for i, skill_info in enumerate(skill_list):
            with cols[i]:
                with st.container():
                    st.markdown(f"""
                    <div class='skill-container'>
                        <h3>{skill_info['icon']} {skill_info['name']}</h3>
                        <div style='margin-top: 10px;'>
                            <div style='margin-bottom: 5px;'>
                                {skill_info['level']}% Proficiency
                            </div>
                            <div style='width: 100%;'>
                                <div style='width: {skill_info['level']}%; height: 10px; background-color: #4CAF50; border-radius: 5px;'></div>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

# Update function call
def main():
    st.set_page_config(
        page_title="Technical Skills",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    skill_page()

if __name__ == "__main__":
    main()
