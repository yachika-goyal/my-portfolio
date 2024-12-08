import streamlit as st
import streamlit_shadcn_ui as ui

def projects_page():
    # Custom CSS for Projects Page
    st.markdown("""
    <style>
        .projects-header {
            background: linear-gradient(45deg, #3b82f6, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 900;
            font-size: 3rem;
            margin-bottom: 2rem;
            text-align: center;
        }

        .project-card {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.05), rgba(139, 92, 246, 0.05));
            border-radius: 15px;
            padding: 25px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
            border: 1px solid rgba(139, 92, 246, 0.1);
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }

        .project-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            border-color: rgba(139, 92, 246, 0.2);
        }

        .project-title {
            color: #8b5cf6;
            margin-bottom: 15px;
            font-weight: 700;
            font-size: 1.5rem;
        }

        .project-description {
            color: #4a5568;
            margin-bottom: 15px;
        }

        .tech-badge {
            background-color: rgba(139, 92, 246, 0.1);
            color: #8b5cf6;
            padding: 5px 10px;
            border-radius: 20px;
            font-size: 0.8rem;
            display: inline-block;
            margin-right: 10px;
            margin-bottom: 10px;
            font-weight: 600;
        }

        .project-links {
            display: flex;
            gap: 15px;
            margin-top: 15px;
        }

        .project-link {
            background: linear-gradient(90deg, #3b82f6, #8b5cf6);
            color: white !important;
            text-decoration: none;
            padding: 8px 15px;
            border-radius: 25px;
            font-weight: 600;
            transition: transform 0.3s ease;
            display: inline-block;
            text-align: center;
        }

        .project-link:hover {
            transform: scale(1.05);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<h1 class="projects-header">Featured Projects</h1>', unsafe_allow_html=True)

    # Project data with more details
    projects = [
        {
            "name": "AI-Powered Dashboard",
            "description": "Developed an intelligent data visualization platform that leverages machine learning to provide predictive insights and interactive visualizations. The dashboard integrates complex data sources and uses advanced ML algorithms to generate actionable business intelligence.",
            "technologies": ["React", "Python", "Machine Learning", "Docker", "Data Visualization"],
            "github": "https://github.com/example/project1",
            "live": "https://demo.com",
            "challenges": ["Real-time data processing", "ML model integration", "Scalable architecture"],
            "impact": "Improved decision-making by 40% through advanced predictive analytics"
        },
        {
            "name": "Cloud Microservices Architecture",
            "description": "Designed and implemented a scalable microservices solution with advanced cloud integration, focusing on high availability, fault tolerance, and seamless service communication. The project showcases best practices in distributed system design and cloud-native application development.",
            "technologies": ["Kubernetes", "AWS", "Node.js", "GraphQL", "Microservices"],
            "github": "https://github.com/example/project2",
            "live": "https://demo.com",
            "challenges": ["Service orchestration", "Horizontal scaling", "Inter-service communication"],
            "impact": "Reduced infrastructure costs by 35% and improved system resilience"
        },
        {
            "name": "Full-Stack E-Learning Platform",
            "description": "Created a comprehensive e-learning platform with personalized learning paths, interactive content, and advanced progress tracking. The application uses machine learning to recommend courses and assess learning effectiveness.",
            "technologies": ["Next.js", "Django", "PostgreSQL", "Redis", "Machine Learning"],
            "github": "https://github.com/example/project3",
            "live": "https://demo.com",
            "challenges": ["Personalized learning algorithms", "Real-time progress tracking", "Scalable content delivery"],
            "impact": "Increased user engagement by 50% through personalized learning experiences"
        }
    ]

    # Display projects
    for project in projects:
        st.markdown(f'''
        <div class="project-card">
            <div class="project-title">{project['name']}</div>
            <div class="project-description">{project['description']}</div>
            
            <div style="margin-bottom: 15px;">
                {''.join(f'<span class="tech-badge">{tech}</span>' for tech in project['technologies'])}
            </div>
            
            <div class="project-links">
                <a href="{project['github']}" class="project-link" target="_blank">GitHub</a>
                <a href="{project['live']}" class="project-link" target="_blank">Live Demo</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)

        # Optional: Expander for more project details
        with st.expander("Project Details"):
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("#### Key Challenges")
                for challenge in project.get('challenges', []):
                    st.markdown(f"- {challenge}")
            
            with col2:
                st.markdown("#### Project Impact")
                st.markdown(f"> {project.get('impact', 'No specific impact metrics available')}")

# Call the projects page function
projects_page()