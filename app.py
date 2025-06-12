import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="Pavan Kumar Portfolio", layout="wide")

# --- Hide default Streamlit style ---
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- Load profile pic ---
profile_pic = "https://www.streamlit.io/images/brand/streamlit-mark-color.png"

# --- Initialize session state ---
if 'page' not in st.session_state:
    st.session_state.page = "About Me"

# --- Navigation Buttons ---
col1, col2, col3, col4 = st.columns(4)
if col1.button("About Me"):
    st.session_state.page = "About Me"
if col2.button("Education"):
    st.session_state.page = "Education"
if col3.button("Projects"):
    st.session_state.page = "Projects"
if col4.button("Skills"):
    st.session_state.page = "Skills"

# --- Custom Styling ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
        font-family: 'Arial', Helvetica, sans-serif;
    }

    h1, h2, h3, h4, h5, h6, p, div, span, a {
        color: #FFFFFF !important;
    }

    div.stButton > button:first-child {
        background-color: #333333;
        color: #FFFFFF;
        border: 1px solid #555555;
    }

    div.stButton > button:hover {
        background-color: #555555;
        color: #FFFFFF;
    }

    div.stButton > button:active {
        background-color: #777777;
        color: #FFFFFF;
    }

    div.stButton > button:disabled {
        background-color: #111111;
        color: #888888;
        border: 1px solid #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar ---
st.sidebar.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #222222;
            color: #FFFFFF;
        }
        [data-testid="stSidebar"] a {
            color: #FFFFFF;
        }
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image(profile_pic, width=150)
    st.title("Pavan Kumar Tarivetla")
    st.markdown("📍 Amalapuram, India")
    st.markdown("📞 8919233032")
    st.markdown("**Software Engineer**")
    st.markdown("Python | ML | Data Science")
    st.markdown("---")
    st.markdown("[GitHub](https://github.com/pavankumart1012)")
    st.markdown("[LinkedIn](https://linkedin.com/in/pavan-kumar-tarivetla-445556330)")
    st.markdown("[Email](mailto:pavankumart955@gmail.com)")
    st.markdown("[📄 View Resume](https://your-resume-link.com)")

# --- Main Content ---
if st.session_state.page == "About Me":
    st.title("👋 Hello, I'm Pavan Kumar")
    st.subheader("Turning data into insights with Python & Machine Learning")

    st.write("""
    I’m a fresher passionate about data science, machine learning, and analytics.
    I enjoy working with data, solving problems, and building impactful projects.
    My goal is to continuously learn and grow in the world of AI/ML.
    """)

    st.markdown("### 🔍 What I Work With")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 🤖 Machine Learning")
        st.write("""
        - Scikit-learn  
        - Regression, Classification  
        - Random Forest, Decision Trees  
        - K-Nearest Neighbors, SVM  
        - Model Evaluation & Tuning
        """)

        st.markdown("#### ☁️ Cloud")
        st.write("""
        - Google Colab  
        - Basic AWS (EC2, S3)
        """)

    with col2:
        st.markdown("#### 🧠 Deep Learning")
        st.write("""
        - Neural Networks (Basics)  
        - TensorFlow (Basics)  
        - Keras (Basics)
        """)

        st.markdown("#### 🛠️ Technologies & Libraries")
        st.write("""
        - Python, Pandas, NumPy  
        - Matplotlib, Seaborn  
        - EDA, Feature Engineering
        """)

    with col3:
        st.markdown("#### 🧰 Tools & Frameworks")
        st.write("""
        - Streamlit, Jupyter Notebook  
        - Git & GitHub  
        - VS Code  
        - Anaconda
        """)

    st.markdown("### 💼 Work Experience")
    st.write("""
    - **Software Engineer at Lyros Technologies** (October 2024 - Present)  
    - Applied machine learning techniques to solve real-world problems, enhancing understanding of data science principles.  
    - Skills Gained: Python, Machine Learning, Data Analysis, Software Development
    """)

elif st.session_state.page == "Education":
    st.header("🎓 Education")
    st.write("---")
    st.write("**Degree:** Bachelor of Technology (B.Tech) in Electrical and Electronics Engineering")
    st.write("**Institution:** Aditya Engineering College, Andhra Pradesh")
    st.write("**Graduation Year:** 2021")
    st.markdown("**Project: 🤖 Surveillance Robot using Raspberry Pi**")
    st.write("---")

elif st.session_state.page == "Projects":
    st.header("📁 Projects")
    st.subheader("🤖 Surveillance Robot using Raspberry Pi")
    st.write("""
    Our project titled **"Surveillance Robot using Raspberry Pi"** aims to develop a cost-effective and portable robot for **real-time surveillance and monitoring** in remote or sensitive areas.
    
    It is equipped with:
    - A **Raspberry Pi** (as the main controller)
    - A **Pi Camera module** for live video streaming
    - **DC motors** for movement
    - Controlled via a **motor driver module**
    - Interface built using **Python** and **Flask**
    
    This robot can be remotely accessed and controlled via Wi-Fi, offering a live camera feed through a web-based interface.
    """)

    st.markdown("### 🧰 Technologies Used")
    st.write("""
    - **Hardware:** Raspberry Pi, Pi Camera, DC Motors, L293D Motor Driver, Chassis Kit  
    - **Software:** Python, Flask (Web Interface), OpenCV (for video feed), HTML/CSS (basic UI)  
    - **Protocols:** Wi-Fi-based communication using Flask routes
    """)

    st.markdown("### 🚀 Key Features")
    st.write("""
    - Real-time **video surveillance** over web  
    - **Remote control** through browser (forward, backward, left, right, stop)  
    - Compact and **cost-effective**  
    - Useful in **monitoring restricted or dangerous areas**
    """)

    st.markdown("### 📚 What I Learned")
    st.write("""
    - Interfacing hardware components with Raspberry Pi  
    - Building Flask apps and using video streaming with OpenCV  
    - Working with motor drivers and GPIO pins  
    - Handling live video feed and control over the web
    """)

elif st.session_state.page == "Skills":
    st.header("🛠️ Skills")
    st.subheader("Python Programming")
    st.write("""
    - Proficient in Python with experience in data analysis, machine learning, and web development.
    - Example: Developed a surveillance robot using Raspberry Pi, utilizing Python and OpenCV for real-time video streaming and remote control.
    """)

    st.subheader("HTML")
    st.write("""
    - Experienced in creating web interfaces using HTML.
    - Example: Designed the user interface for the surveillance robot project, enabling remote access and control through a web browser.
    """)

    st.subheader("CSS")
    st.write("""
    - Skilled in styling web applications using CSS.
    - Example: Enhanced the visual appeal and user experience of the surveillance robot's web interface with custom CSS styles.
    """)

    st.subheader("ServiceNow")
    st.write("""
    - Familiar with ServiceNow platform.
    """)
