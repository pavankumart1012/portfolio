import streamlit as st
from PIL import Image

# --- Page Config ---
st.set_page_config(page_title="Pavan Kumar Portfolio", layout="wide")

# --- Style settings ---
hide_streamlit_style = ""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# --- Load profile pic ---
profile_pic = "https://www.streamlit.io/images/brand/streamlit-mark-color.png"  # Replace with your actual image file name

# --- Initialize session state ---
if 'page' not in st.session_state:
    st.session_state.page = "About Me"

# --- Navigation ---
col1, col2, col3, col4, col5 = st.columns(5)

if col1.button("About Me"):
    st.session_state.page = "About Me"
if col2.button("Education"):
    st.session_state.page = "Education"
if col3.button("Projects"):
    st.session_state.page = "Projects"
if col4.button("Skills"):
    st.session_state.page = "Skills"
if col5.button("Contact"):
    st.session_state.page = "Contact"

# --- Header ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1542831323-533a40c64e5c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8Y29kaW5nfGVufDB8fDB8fA%3D%3D&w=1000&q=80");
        background-size: cover;
        color: black;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --- Side Panel / Header ---
with st.sidebar:
    st.image(profile_pic, width=150)
    st.title("Pavan Kumar Tarivetla",  )
    st.markdown("📍Amalapuram, India", )
    st.markdown("📞 8919233032", )
    st.markdown("**Software Engineer**", )
    st.markdown("Python | ML | Data Science", )
    st.markdown("---")
    st.markdown("[GitHub](https://github.com/pavankumart1012)", )
    st.markdown("[LinkedIn](https://linkedin.com/in/pavan-kumar-tarivetla-445556330)", )
    st.markdown("[Email](https://mail.google.com//pavankumart955@gmail.com)", )
    st.markdown("[📄 View Resume](https://your-resume-link.com)", )

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
    st.write("""
    - Python, Pandas, NumPy, Matplotlib, Seaborn
    - Scikit-learn, Regression, Classification, Random Forest
    - EDA, Data Cleaning, Feature Engineering
    - Git, Streamlit, Jupyter
    """)

    st.markdown("### 💼 Work Experience")
    st.write("""
    - **Software Engineer at Lyros Technologies** (October 2024 - Present)
    - Applied machine learning techniques to solve real-world problems, enhancing understanding of data science principles.
    - Skills Gained: Python, Machine Learning, Data Analysis, Software Development
    """)

elif st.session_state.page == "Education":
    
        st.header("Education")
        st.markdown("## 🎓 Education")
        st.write("---")
        st.write("**Degree:** Bachelor of Technology (B.Tech) in Electrical and Electronics Engineering")
        st.write("**Institution:** Aditya Engineering College, Andhra Pradesh")
        st.write("**Graduation Year:** 2021")
        st.markdown("**Project: 🤖 Surveillance Robot using Raspberry Pi**")
        st.write("---")

elif st.session_state.page == "Projects":
    st.header("Projects")
    st.write("Here are some of my projects:")

    # Project 1
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

    st.markdown("---")
    #st.success("📩 Want to know more or see the code? Feel free to reach out!")

    # Project 2
    #st.subheader("Project Title 2")
    #st.write("Description of project 2. This project involved...")
    #st.markdown("[Code Repository](https://github.com/yourusername/project2)")
    #st.markdown("[Live Demo](https://yourproject2.com)")


elif st.session_state.page == "Skills":
    st.header("Skills")
    st.write("I possess a diverse skill set developed through academic projects and professional experience. Here are some highlights:")

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

elif st.session_state.page == "Contact":
    st.header("Contact")
    st.write("Feel free to reach out to me through the following channels:")

    st.markdown("[LinkedIn](https://www.linkedin.com/in/pavan-kumar-tarivetla-445556330)")
    st.markdown("[GitHub](https://github.com/pavankumart1012)")
    st.markdown("[Email](https://mail.google.com//pavankumart955@gmail.com)")