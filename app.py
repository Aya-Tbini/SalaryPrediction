import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

import streamlit as st
page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

 

if page == "Predict":
    st.title("Software Developer Salary Prediction")
  
    st.image("predict.jpg", width=400)   # Specify the width parameter to display the image smaller

    show_predict_page()
else:
    st.title("Explore Software Engineer Salaries")
    # # Specify the width parameter to display the image smaller
    #st.image("explore.jpg") 
    show_explore_page()
    