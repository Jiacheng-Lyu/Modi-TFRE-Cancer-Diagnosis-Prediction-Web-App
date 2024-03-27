#importing all the important libraries
import streamlit as st

import os
import warnings
warnings.simplefilter("ignore")
import joblib

import numpy as np

input_feature_type = st.sidebar.radio("Navigation Menu",["Home", "TCGA-Transcriptome", "CPTAC-Proteome"])
tumor_type = 'multi'

#Home Page 
if input_feature_type == "Home":
    st.title("The prediction App for the {} diagnosis".format(tumor_type))
    st.text("The Following Sample Type and Data Type Are Available ->")
    st.text("1. TCGA-Transcriptome")
    st.text("2. CPTAC-Proteome")

def return_predict_result(predict_out, target_or_tumor_type):
    if target_or_tumor_type == 'multi':
        st.success("The patient have the {}".format(dict(zip(range(4), ['BRCA', 'CESC', 'LIHC', 'LUAD'])).get(predict_out[0])))
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
    input_feature_types = {'Plasma-Proteome': 'PLASMA', 'CPTAC-Proteome': 'CPTAC', 'TCGA-Transcriptome': 'TCGA'}
    sample_type = input_feature_types.get(input_feature_type)
    for f in os.listdir('./models'):
        if f.endswith('joblib') and tumor_type in f and sample_type in f:
            _, name2, *_ = f.split('_')
            model = joblib.load(os.path.join('./models', f))
    name_spaces = {'BRCA': 'breast cancer', 'LUAD': 'lung adenocarcinoma', 'LIHC': 'liver hepatocellular carcinoma', 'CESC': 'cervical squamous cell carcinoma', 'multi': 'specific cancer'}
    st.header("Predict whether the patient with {}.".format(name_spaces[name2]))
    st.write("Providing two decimal place will make the prediction more accurate")

if input_feature_type in ['Plasma-Proteome', 'TCGA-Transcriptome', 'CPTAC-Proteome']:
    pipeline(input_feature_type)

    bcl11b = st.number_input("The BCL11B protein expression level")
    cebpz = st.number_input("The CEBPZ protein expression level")
    cux1 = st.number_input("The CUX1 protein expression level")
    etv6 = st.number_input("The ETV6 protein expression level")
    foxp1 = st.number_input("The FOXP1 protein expression level")
    gatad2a = st.number_input("The GATAD2A protein expression level")
    gmeb1 = st.number_input("The GMEB1 protein expression level")
    gmeb2 = st.number_input("The GMEB2 protein expression level")
    hmbox1 = st.number_input("The HMBOX1 protein expression level")
    prdm10 = st.number_input("The PRDM10 protein expression level")
    sp3 = st.number_input("The SP3 protein expression level")
    tcf4 = st.number_input("The TCF4 protein expression level")
    terf2 = st.number_input("The TERF2 protein expression level")
    tp53 = st.number_input("The TP53 protein expression level")
    zfp91 = st.number_input("The ZFP91 protein expression level")
    zhx3 = st.number_input("The ZHX3 protein expression level")
    znf280c = st.number_input("The ZNF280C protein expression level")

    input_value = np.array([[bcl11b, cebpz, cux1, etv6, foxp1, gatad2a, gmeb1, gmeb2, hmbox1, prdm10, sp3, tcf4, terf2, tp53, zfp91, zhx3, znf280c]])
    predict_out = predict_state(input_value)

    if st.button("Predict"):
        return_predict_result(predict_out, tumor_type)