#importing all the important libraries
import streamlit as st

import os
import warnings
warnings.simplefilter("ignore")
import joblib

import numpy as np

input_feature_type = st.sidebar.radio("Navigation Menu",["Home", "Plasma-Proteome", "CPTAC-Proteome"])
tumor_type = 'LIHC'

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

    eno1 = st.number_input("The ENO1 protein expression level")
    hnrnpab = st.number_input("The HNRNPAB protein expression level")
    med11 = st.number_input("The MED11 protein expression level")
    msl1 = st.number_input("The MSL1 protein expression level")
    znf512b = st.number_input("The ZNF512B protein expression level")

    input_value = np.array([[eno1, hnrnpab, med11, msl1, znf512b]])
    predict_out = predict_state(input_value)

    if st.button("Predict"):
        return_predict_result(predict_out, tumor_type)