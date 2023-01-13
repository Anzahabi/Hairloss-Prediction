import streamlit as st
import pandas as pd
import pickle
from imblearn.over_sampling import SMOTENC
from PIL import Image
image1 = Image.open('lost3.jpg')



st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:30px !important;
}

.img {
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 5px;
  width: 150px;
}
</style>
""", unsafe_allow_html=True)

st.title('Let Us Predict Your Hair Loss Level')
st.image(image1, width=None)
st.write('Choose your habit on the side and press "Predict" button')



#STEP 1 import saved model
model = pickle.load(open('hair_loss.pkl', 'rb'))


# user input
coffee_consumed = st.sidebar.slider(label='Coffee Consumed in a day', min_value=0.0, max_value=10.0, value=0.0, step=1.0)
hair_grease = st.sidebar.slider(label='Hair Grease', min_value=1.0, max_value=5.0, value=1.0, step=0.5)
stress_level = st.sidebar.selectbox(label='Stress Level', options=['Low', 'Medium', 'High', 'Very High'], key=0)
pressure_level = st.sidebar.selectbox(label='Pressure Level', options=['Low', 'Medium', 'High', 'Very High'], key=1)
dandruff = st.sidebar.selectbox(label='Dandruff', options=['None', 'Few', 'Many'], key=2)
school_assesssment = st.sidebar.selectbox(label='School Assessment', options=['None', 'Team ass', 'Individual ass', 'Final exam revision', 'Final exam'], key=3)


					

# convert into dataframe
data = pd.DataFrame({'coffee_consumed': [coffee_consumed],
                'hair_grease': [hair_grease],
                'stress_level': [stress_level],
                'pressure_level':[pressure_level],
                'dandruff': [dandruff],
                'school_assesssment': [school_assesssment]})
                

# model predict
clas = model.predict(data).tolist()[0]

# interpretation


# interpretation
if st.button('Predict'):
    if clas == 0.0:
        st.markdown('<p class="big-font">DAMN YOU FINE! </p>', unsafe_allow_html=True)
        st.text('Your Hair are Amazing')
    elif clas == 1.0:
        st.markdown('<p class="big-font">BE CAREFUL! </p>', unsafe_allow_html=True)
        st.text('Your are about to experience hair loss')
    else:
        st.markdown('<p class="big-font">OH NO! </p>', unsafe_allow_html=True)
        st.text('You are experiencing Hair Loss')


