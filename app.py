import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Chest X-Ray Analysis", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS for Better Styling
st.markdown("""
    <style>
    .title { 
        font-size: 2.5em; 
        font-weight: bold; 
        text-align: center;
        color: #4A90E2; 
    }
    .subheader {
        font-size: 1.5em;
        text-align: center;
        color: #6B7280;
    }
    .upload-box {
        border: 2px dashed #4A90E2;
        padding: 20px;
        border-radius: 10px;
        background-color: #F3F4F6;
    }
    .footer {
        font-size: 0.8em;
        color: #6B7280;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Subtitle
st.markdown('<p class="title">Chest X-Ray Analysis with Grad-CAM</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Classify an X-Ray Image</p>', unsafe_allow_html=True)

# Upload Section
st.write("### Upload Your X-Ray Image Below")

uploaded_file = st.file_uploader(
    "Drag and drop your X-ray image here", 
    type=["jpg", "jpeg", "png"], 
    label_visibility="collapsed"
)

st.markdown('<div class="upload-box">', unsafe_allow_html=True)
st.write("Supported formats: **.jpg, .jpeg, .png** | Max file size: **10MB**")
st.markdown('</div>', unsafe_allow_html=True)

# Display Uploaded Image
if uploaded_file:
    st.success(f"✅ Successfully Uploaded: **{uploaded_file.name}**")
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded X-Ray Image", use_column_width=True)
    
    # Placeholder for Classification Result
    st.write("### ⏳ Processing Image...")
    st.info("🔍 This is where the Grad-CAM analysis and classification result will appear.")

# Footer
st.markdown('<p class="footer">The Grad-CAM tool helps visualize critical areas in X-Ray images for classification.</p>', unsafe_allow_html=True)
st.markdown('<p class="footer">Note: Use updated parameters for the best performance.</p>', unsafe_allow_html=True)
