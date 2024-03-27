#importing all the important libraries
import streamlit as st

import os
import warnings
warnings.simplefilter("ignore")
import joblib

import numpy as np

input_feature_type = st.sidebar.radio("Navigation Menu",["Home", "Plasma-Proteome", "CPTAC-Proteome"])
tumor_type = 'LUAD'

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
    gatad2b = st.number_input("The GATAD2B protein expression level")
    hnrnpdl = st.number_input("The HNRNPDL protein expression level")
    lonp1 = st.number_input("The LONP1 protein expression level")
    mcm7 = st.number_input("The MCM7 protein expression level")
    med11 = st.number_input("The MED11 protein expression level")
    tnks1bp1 = st.number_input("The TNKS1BP1 protein expression level")

    input_value = np.array([[gatad2b, hnrnpdl, lonp1, mcm7, med11, tnks1bp1]])
    predict_out = predict_state(input_value)

    if st.button("Predict"):
        return_predict_result(predict_out, tumor_type)