#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:42:43 2024

@author: abhishekjain
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open('/Users/abhishekjain/Documents/GitHub/ML Projects/Multiple-Disease-Prediction-using-ML-in-Python/trained_diabetes_model.sav','rb'))

heart_model = pickle.load(open('/Users/abhishekjain/Documents/GitHub/ML Projects/Multiple-Disease-Prediction-using-ML-in-Python/trained_heart_disease.sav','rb'))



# Creating side navigation bar using streamlit option menu 
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons=['activity','heart'],
                           default_index=0)
    

# Prediction Page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    # Getting the input data from user
    # Columns from input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose level")

    with col3:
        BloodPressure = st.text_input("Blood Pressure level")

    with col1:
        SkinThickness = st.text_input("Skin Thickness value")

    with col2:
        Insulin = st.text_input("Insulin level")

    with col3:
        BMI = st.text_input("BMI value")

    with col1:
        DiabetesPedigreeFunc = st.text_input("Diabetes Pedigree Function value")

    with col2:
        Age = st.text_input("Age of the person")
    
    
    # Code for prediction
    diab_diagnosis = ''
    
    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunc, Age]])
    
    
        if (diab_prediction[0]==1):
            diab_diagnosis='The person is diabetic'
            
        else:
            diab_diagnosis='The person is not diabetic'
            
    
    st.success(diab_diagnosis)
    
    

if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    # Columns for user input
    # Getting the input data from user
    # Columns from input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input("Age")
        
    with col2:
        sex = st.text_input("Sex")
        
    with col3:
        cp = st.text_input("Chest Pain types")
        
    with col1:
        trestbps = st.text_input("Resting Blood Pressure")
        
    with col2:
        chol = st.text_input("Cholestrol")
        
    with col3:
        fbs = st.text_input("fbs")
        
    with col1:
        restecg = st.text_input("Resting ECG")
        
    with col2:
        thalach = st.text_input("thalach")
        
    with col3:
        exang = st.text_input("exang")
        
    with col1:
        oldpeak = st.text_input("oldpeak")
        
    with col2:
        slope = st.text_input("slope")
        
    with col3:
        ca = st.text_input("ca")
        
    with col1:
        thal = st.text_input("thal")
        
        
     # Code for prediction
    heart_diagnosis = ''
     
     # Creating a button for prediction
    if st.button('Heart Test Result'):
         heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
     
     
         if (heart_prediction[0]==1):
             heart_diagnosis='The person has a heart disease'
             
         else:
             heart_diagnosis='The person does not have a heart disease'
             
     
    st.success(heart_diagnosis) 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    