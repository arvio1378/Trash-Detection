import streamlit as st
import tempfile
from ultralytics import YOLO
from utils.detect_img import detect_image
from utils.detect_video import detect_video
from utils.categories import categories

# Baca file CSS eksternal
with open("style\style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Konfigurasi Streamlit
st.set_page_config(
    page_title="Trash Detection App",
    page_icon="🗑️",
    layout="wide"
)

# Load model YOLOv8
@st.cache_resource
def load_model():
    return YOLO(r"runs\detect\train\weights\best.pt")

# Navigasi sidebar
st.sidebar.title("Navigation")
# Pilihan Navigasi
pages = st.sidebar.selectbox("Menu : ", ["Picture", "Video", "Profile"])

# Page Program
if pages == "Picture":
    st.markdown('<h1 class="main-title">Trash Detection App</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # upload image
    st.write("#### Upload an image to detect trash items.")
    uploaded_file_img = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    if uploaded_file_img is not None:
        col1, col2 = st.columns(2)
        with col1:
            # Display uploaded image
            st.image(uploaded_file_img, caption='Uploaded Image', use_container_width=True)

        # Load the model
        model = load_model()

        # Perform detection
        results_img = detect_image(uploaded_file_img, model)

        with col2:
            # Display results
            st.image(results_img["img_rgb"], caption='Detection Results', use_container_width=True)
        
        # Display class names and counts
        st.markdown("### Detected Classes and Counts")

        # tampilkan hasilnya
        for cls, count in results_img["class_counts"].items():
            # ambil kategori dan warna sampah
            category, color, emoji, info = categories.get(cls, ("Unknown", "black", "❓", "information not available"))
            # tampilkan dengan format yang menarik
            st.markdown(
                f"<p style='font-size:18px;'>"
                f"{emoji} <b>{cls}</b>: {count} "
                f"===> <span style='color:{color};'><b>{category}</b></span><br>"
                f"<span>{info}</span>"
                f"</p>",
                unsafe_allow_html=True
            )

# Page Video
elif pages == "Video":
    st.markdown('<h1 class="main-title">Trash Detection App</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # upload video
    st.write("#### Upload a video to detect trash items.")
    uploaded_file_video = st.file_uploader("Upload Video", type=["mp4", "mov", "avi", "mkv"])
    if uploaded_file_video is not None:
        # save uploaded video to a temporary file
        tempfile_video = tempfile.NamedTemporaryFile(delete=False)
        tempfile_video.write(uploaded_file_video.read())
        st.video(tempfile_video.name)

        # Load the model
        model = load_model()

        # stframe to display video frames
        stframe = st.empty()

        # Perform detection
        results_video = detect_video(tempfile_video.name, model, stframe)

        # Display detected classes and counts after video processing
        st.markdown("### Detected Classes and Counts")
        for cls, count in results_video["class_counts"].items():
            # ambil kategori dan warna sampah
            category, color, emoji, info = categories.get(cls, ("Unknown", "black", "❓", "information not available"))
            # tampilkan dengan format yang menarik
            st.markdown(
                f"<p style='font-size:18px;'>"
                f"{emoji} <b>{cls}</b>"
                f" ===> <span style='color:{color};'><b>{category}</b></span><br>"
                f"<span>{info}</span>"
                f"</p>",
                unsafe_allow_html=True
            )

        # button to play again video results
        if st.button("Play again"):
            stframe.empty()
            tempfile_video.close()


# Page Profile
elif pages == "Profile":
    # Judul aplikasi dan huruf italic
    st.title("Arvio Abe Suhendar")
    # Subheader
    st.subheader("Career Shifter | From Network to AI | Designing Intelligent Futures | Ready to Make an Impact in AI | Python Developer | Machine Learning Engineer | Data Scientist")
    st.markdown("---")

    # About me
    st.write("### 📝 About Me")
    st.write("👨‍💻 I'm a tech enthusiast with a strong foundation in Informatics Engineering from Universitas Gunadarma, where I developed solid analytical thinking, programming, and problem-solving skills.")
    st.write("🔧 After graduating, I began my professional journey as a Junior Network Engineer, managing enterprise network services like VPNIP, Astinet, and SIP Trunk on Huawei and Cisco platforms—handling configurations, service activations, and troubleshooting.")
    st.write("🤖 Over time, my curiosity led me to explore the world of Artificial Intelligence & Machine Learning. I've been actively upskilling through bootcamps and self-learning—covering data preprocessing, supervised & unsupervised learning, and deep learning using Python.")
    st.write("🎯 I'm now transitioning my career into AI/ML, combining my network infrastructure background with my growing expertise in data and intelligent systems. I'm particularly interested in how AI can improve systems, automate operations, and drive smarter decision-making.")
    st.write("🤝 Open to collaborations, mentorship, and new opportunities in the AI/ML space.")
    st.markdown("---")

    tab1, tab2, tab3 = st.tabs(["Education", "Experience", "Skills"])
    with tab1:
        # Pendidikan
        st.write("### 🎓 Education")
        st.write("""
        - **Bachelor of Informatics Engineering**   
        Universitas Gunadarma, 2019 - 2023, GPA 3.82/4.00
            - Built multiple applications (web & desktop) using Java, Python, and PHP in individual and team projects.
            - Built and optimized database systems
            - Learn techniques for solving mathematical problems using programming, numerical integration, and solving equations.
        - **Bootcamp AI/ML**    
        Dibimbing.id Academy, Apr 2025 - Sep 2025
            - Mastered core concepts of Python programming including variables, data types, control structures, and functions.
            - Understanding the fundamentals of Artificial Intelligence and Machine Learning, key concepts, and applications.
            - Techniques to clean, transform, and prepare data for analysis, including handling missing data and feature scaling.
        """)
    with tab2:
        # Pengalaman
        st.write("### 💼 Experience")
        st.write("""
        - **Junior Network Engineer**   
        PT. Infomedia Nusantara, 2023 - Present
            - Astinet & VPNIP Service Management (Huawei Routers) : 
                 Handled service activation, disconnection,isolation, modification, and resumption for enterprise clients.
            - Wifi.id Service Provisioning (Cisco & WPgen) :    
                 Performed end-to-end activation and troubleshooting for public Wi-Fi services.
            - SIP Trunk International Access Control :  
                 Managed blocking and unblocking processes for international SIP trunk services to ensure secure and compliant voice connectivity
        """)
    with tab3:
        # Keterampilan
        st.write("### 🛠️ Skills")
        st.write("""
        - **Programming Languages**: Python
        - **Machine Learning**: Scikit-learn, TensorFlow, Keras
        - **Data Analysis**: Pandas, NumPy, Matplotlib, Seaborn
        - **Database Management**: MySQL, PostgreSQL
        - **Networking**: Huawei Routers, Cisco Routers, WPgen
        - **Tools & Technologies**: Git, Docker, Jupyter Notebook
        - **Soft Skills**: Attention to Detail, Team Collaboration, Adaptability
        """)
    
    st.markdown("---")
    # Kontak
    st.write("### 📞 Contact Information")
    st.write("I'm currently studying and building a career in AI/ML. This project is my practice in building a simple Python application. I want to further develop my skills in this field through existing projects.")
    st.write("Feel free to contact me if you have any questions or suggestions regarding this project.")
    st.write("Email: 4rv10suhendar@gmail.com")
    st.write("LinkedIn: [Arvio Abe Suhendar](https://www.linkedin.com/in/arvio-abe-suhendar/)")
    st.write("Location: Depok, Indonesia")
    st.write("GitHub: [Arvio1378](https://github.com/arvio1378)")