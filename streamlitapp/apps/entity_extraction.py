# import packages
from multiprocessing.sharedctypes import Value
from urllib import response
import missingno as msno
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.cluster import KMeans
import streamlit as st

import os
import sys
import logging
import numpy as np
import pandas as pd

import json
import requests

def get_entity(jds:dict):
    
    header = {'Content-Type': 'application/json'}
	# url = "http://backend.docker:8000/prediction" 
    url= "http://localhost:8000/jdentities"
    payload = json.dumps(jds)
    print(payload)
    response = requests.request("POST", url, headers=header, data=payload)
    response = response.text
    
    return response

def entity_extraction(df: pd.DataFrame):
    
    st.write('## Entity Extraction From Job Description')
    
    form = st.form(key='entity-form')
    jdes = form.text_input('Job Description', 'Job description here!')
    
    model = form.selectbox('Select Model',('xlarge','large','medium','small'))
    form.write('Set model parameters(using the default values is recommended).')
    temperature = form.slider(label='Temperature',step=0.1,value=0.5,
                              min_value=0.0, max_value=2.0)
    token = form.text_input('Token',50)
    top_k = form.text_input('Top-k',0)

    top_p = form.slider(label='Top-p', step=0.1,value=0.75,
                        min_value=0.0, max_value=1.0)
    freq_p = form.slider(label='Frequency Penalty', step=0.1,value=0.5,
                        min_value=0.0, max_value=1.0)
    pres_p = form.slider(label='Presence Penalty', step=0.1,value=0.5,
                         min_value=0.0, max_value=1.0)
    
    submit = form.form_submit_button(label="Submit", help=None,
                                     on_click=None, args=None, kwargs=None)
    
    if submit:
        ent = get_entity(jds = {"document":jdes})
        st.write('### Extracted Entity')
        st.write(ent)
  
