import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to modi-TFRE based cancer diagnosis models! 👋")

st.markdown(
    """
    Modi-TFRE is a tool built specifically for transcriptor factor (TF) enrichment
    The preferred TFs were differed from cancer to cancer, which hence, could be used for cancer diagnosis by Machine Learning. 
    The models for four different cancers including lung adenocarcinoma, liver hepatocellular carcinoma, breast cancer, and cervical squamous cell carcinoma based on different sample types and data types were trained 
    **👈 Select a specific button from the sidebar** to start the prediction!

    ### What sample type options supplied?
    - Tissue data
    - Plasma data
    ### What data type options supplied?
    - Transcriptome-based TF activities
    - Proteome data
    """
)