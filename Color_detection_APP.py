import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Function to detect colors
def color_detection(low_range, high_range, color_name):
    cap = cv2.VideoCapture(0)
    st.markdown(f"### Detecting {color_name.capitalize()} Color")
    st.warning("Press 'Esc' to stop detection in the video window.")
    
    while True:
        _, frame = cap.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_frame, low_range, high_range)
        color_detected = cv2.bitwise_and(frame, frame, mask=mask)
        
        # Show the frames
        cv2.imshow("Original Frame", frame)
        cv2.imshow(f"{color_name.capitalize()} Detection", color_detected)
        
        key = cv2.waitKey(1)
        if key == 27:  # Press 'Esc' to exit detection
            break

    cap.release()
    cv2.destroyAllWindows()

# Streamlit UI
st.title("🎨 Color Detection App")
st.markdown(
    """
    Welcome to the **Color Detection App**!  
    Select a predefined color (Red, Green, Blue) or create your **Custom Color Detection**.  
    Using your webcam, detect specific colors in real-time effortlessly.  
    """
)
st.image("https://source.unsplash.com/800x400/?colors", caption="Eye-Catching Design", use_column_width=True)

# Sidebar Options
st.sidebar.title("Options")
st.sidebar.info("Choose a mode to detect colors.")
choice = st.sidebar.radio("Select a Color Mode", ["Red", "Green", "Blue", "Custom"])

if choice == "Red":
    st.header("🔴 Detecting Red Color")
    if st.button("Start Detection"):
        low_red = np.array([160, 150, 80])
        high_red = np.array([180, 255, 255])
        color_detection(low_red, high_red, "red")

elif choice == "Blue":
    st.header("🔵 Detecting Blue Color")
    if st.button("Start Detection"):
        low_blue = np.array([94, 80, 2])
        high_blue = np.array([126, 255, 255])
        color_detection(low_blue, high_blue, "blue")

elif choice == "Green":
    st.header("🟢 Detecting Green Color")
    if st.button("Start Detection"):
        low_green = np.array([25, 52, 71])
        high_green = np.array([102, 255, 255])
        color_detection(low_green, high_green, "green")

elif choice == "Custom":
    st.header("🎨 Custom Color Detection")
    st.write("Enter the **HSV Color Range** below:")

    low_h = st.number_input("Low H", min_value=0, max_value=179, value=0)
    low_s = st.number_input("Low S", min_value=0, max_value=255, value=0)
    low_v = st.number_input("Low V", min_value=0, max_value=255, value=0)

    high_h = st.number_input("High H", min_value=0, max_value=179, value=179)
    high_s = st.number_input("High S", min_value=0, max_value=255, value=255)
    high_v = st.number_input("High V", min_value=0, max_value=255, value=255)

    color_name = st.text_input("Specify the Color Name", "Custom Color")

    if st.button("Start Detection"):
        low_custom = np.array([low_h, low_s, low_v])
        high_custom = np.array([high_h, high_s, high_v])
        color_detection(low_custom, high_custom, color_name)

# Footer
st.markdown("---")
st.markdown("© 2024 Developed by **Darshanikanta**")
