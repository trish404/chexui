import streamlit as st
from PIL import Image

# Page Config
st.set_page_config(
    page_title="Chest X-Ray Analysis",
    page_icon="🌸",
    layout="centered"
)

# Custom CSS for Professional but Cute Styling
st.markdown("""
    <style>
        body {
            font-family: "Segoe UI", sans-serif;
            background-color: #FAFAFA;
        }
        .title {
            font-size: 2.8em;
            font-weight: 600;
            color: #4A90E2;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 1.2em;
            color: #6B7280;
            text-align: center;
            margin-bottom: 30px;
        }
        .upload-box {
            border: 2px dashed #FFB6C1;
            border-radius: 12px;
            background-color: #FFFAF3;
            padding: 30px;
            text-align: center;
        }
        .footer {
            font-size: 0.85em;
            color: #6B7280;
            text-align: center;
            margin-top: 50px;
        }
        .caption {
            font-size: 1em;
            color: #6B7280;
            text-align: center;
            margin-top: 10px;
        }
        .success-message {
            color: #4CAF50;
            text-align: center;
            font-size: 1.1em;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<p class="title">🌸 Chest X-Ray Analysis with Grad-CAM 🌸</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">A simple and intuitive tool for analyzing X-Ray images</p>', unsafe_allow_html=True)

# Upload Section
st.write("### Upload Your X-Ray Image Below")
st.markdown('<div class="upload-box">', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Drag and drop or browse your file",
    type=["jpg", "jpeg", "png"],
    label_visibility="collapsed"
)
st.markdown('</div>', unsafe_allow_html=True)

# Display Uploaded Image
if uploaded_file:
    st.markdown('<p class="success-message">✅ File successfully uploaded!</p>', unsafe_allow_html=True)
    image = Image.open(uploaded_file)
    st.image(image, caption="Your Uploaded X-Ray Image", use_column_width=True)

    # Placeholder for Processing
    st.write("### Processing Image...")
    st.info("🔍 Generating Grad-CAM results... Please wait.")

# Footer
st.markdown('<p class="footer">Developed with care 🩺 | Grad-CAM helps identify critical regions in X-Ray images</p>', unsafe_allow_html=True)
