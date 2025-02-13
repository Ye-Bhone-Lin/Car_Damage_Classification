import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# Load the YOLO model
load_model = YOLO('best.pt')

uploaded_file = st.file_uploader("Choose your image", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    # Open image using PIL
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption='Uploaded Image')
    
    # Convert PIL image to NumPy array
    image_array = np.array(image)

    # Run YOLO model prediction
    results = load_model(image_array)

    # Create two columns for layout
    
    # Extract and display detected image
    for result in results:
        # Display image with detections
        with col2:
            st.image(result.plot(), caption="Detection Result", use_column_width=True)

        probs = result.probs.data.cpu().numpy()
        class_names = {0: "dent", 1: "glass shatter", 2: "lamp broken", 3: "scratch"}

        for class_id, class_name in class_names.items():
            confidence = probs[class_id]
            if round(confidence,2) > 0.5:  # Strong classification confidence
                st.markdown(f"🔴 **{class_name.upper()} DETECTED** — The model classifies this as {confidence:.2%} likely.\n")
            elif round(confidence,2) > 0.1:  # Weak classification confidence
                st.markdown(f"🟡 **Possible {class_name.upper()}** — The model suggests {confidence:.2%} likelihood.\n")
            else:  # No damage classified
                st.markdown(f"🟢 **No {class_name.upper()} detected.**\n")