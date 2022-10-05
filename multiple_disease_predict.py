import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open(
    'D:/ML_projects/Multiple_disease_prediction/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(
    'D:/ML_projects/Multiple_disease_prediction/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(
    'D:/ML_projects/Multiple_disease_prediction/saved_models/parkinsons_model.sav', 'rb'))

# sidebar for naviagtion

with st.sidebar:

    selected = option_menu('Mulitple Disease Prediction System', [
                           'Diabetes Prediction', 'Heart disease prediction', 'Parkinsons Prediction'], icons=['activity', 'heart', 'person'], default_index=0)

# diabetes prediction page

if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction')

    # getting inputs from user
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes pedigree fuction value')
    Age = st.text_input('Age of the preson')

    # prediction

    diab_dignosis = ''
    # creating a button for prediction

    if st.button('Diabetes test result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_dignosis = 'The Person is diabetic'

        else:
            diab_dignosis = 'The Person is not diabetic'
    st.success(diab_dignosis)


if (selected == 'Heart disease prediction'):

    # page title
    st.title('Heart disease prediction')

    # getting input from users

    age = st.text_input('Age of The person')
    sex = st.text_input('Gender')
    cp = st.text_input('Chest pain types')
    trestbps = st.text_input('resting blood pressure')
    chol = st.text_input('Cholestrol')
    fbs = st.text_input('fasting blood sugar')
    restecg = st.text_input('resting electrocardiographic results')
    thalach = st.text_input('maximum heart rate achieved')
    exang = st.text_input('exercise induced angina')
    oldpeak = st.text_input(
        'ST depression induced by exercise relative to rest')
    slope = st.text_input('the slope of the peak exercise ST segment')
    ca = st.text_input('number of major vessels colored by flourosopy')
    thal = st.text_input('Thal value')

    # prediction
    heart_dignosis = ''

    # creating a button for prediction
    if st.button('Heart Test Results'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_dignosis = 'The Person has heart disease'
        else:
            heart_dignosis = 'The Person dosen\'t have any heart disease'

    st.success(heart_dignosis)


if (selected == 'Parkinsons Prediction'):

    # page title
    st.title('Parkinsons Prediction')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict(
            [[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
