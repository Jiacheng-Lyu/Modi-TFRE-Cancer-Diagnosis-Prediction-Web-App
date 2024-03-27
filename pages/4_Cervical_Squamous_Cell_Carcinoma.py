#importing all the important libraries
import streamlit as st

import os
import warnings
warnings.simplefilter("ignore")
import joblib

import numpy as np

input_feature_type = st.sidebar.radio("Navigation Menu",["Home", "Plasma-Proteome", "CPTAC-Proteome"])
tumor_type = 'CESC'

#Home Page 
if input_feature_type == "Home":
    st.title("The prediction App for the {} diagnosis".format(tumor_type))
    st.text("The Following Sample Type and Data Type Are Available ->")
    st.text("1. Plasma-Proteome")
    st.text("2. CPTAC-Proteome")

def return_predict_result(predict_out, target_or_tumor_type):
    if target_or_tumor_type == 'multi':
        st.success("The patient have the {}".format(dict(zip(range(4), [])).get(predict_out)))
    else:
        if predict_out == 0:
            st.success("The patient have the {}".format(tumor_type))
        else:
            st.success("The patient is healthy")

def predict_state(input_value):
    predict_out = model.predict(input_value)
    return predict_out

def pipeline(input_feature_type):
    global model
    input_feature_types = {'Plasma-Proteome': 'PLASMA', 'CPTAC-Proteome': 'CPTAC', 'TCGA-Transcriptome': 'tissue_transcriptome'}
    sample_type = input_feature_types.get(input_feature_type)
    for f in os.listdir('./models'):
        if f.endswith('joblib') and tumor_type in f and sample_type in f:
            _, name2, *_ = f.split('_')
            model = joblib.load(os.path.join('./models', f))
    name_spaces = {'BRCA': 'breast cancer', 'LUAD': 'lung adenocarcinoma', 'LIHC': 'liver hepatocellular carcinoma', 'CESC': 'cervical squamous cell carcinoma', 'multi': 'specific cancer'}
    st.header("Predict whether the patient with {}.".format(name_spaces[name2]))
    st.write("Providing two decimal place will make the prediction more accurate")

if input_feature_type in ['Plasma-Proteome', 'CPTAC-Proteome']:
    pipeline(input_feature_type)

    atm = st.number_input("The ATM protein expression level")
    eno1 = st.number_input("The ENO1 protein expression level")
    mms19 = st.number_input("The MMS19 protein expression level")
    prdx5 = st.number_input("The PRDX5 protein expression level")
    tpr = st.number_input("The TPR protein expression level")

    input_value = np.array([[atm, eno1, mms19, prdx5, tpr]])
    predict_out = predict_state(input_value)

    if st.button("Predict"):
        return_predict_result(predict_out, tumor_type)