# import packages
import streamlit as st

import json
import requests

import os
import sys
import logging
import numpy as np
import pandas as pd

def get_score(news:dict):

    header = {'Content-Type': 'application/json'}
# url = "http://backend.docker:8000/prediction"
    url = "http://localhost:8000/dnewscore"
    
    payload = json.dumps(news)
    print(payload)
    response = requests.request("POST", url, headers=header, data=payload)
    response = response.text

    return response


def news_scoring(df: pd.DataFrame):

    st.write('### News Artifact Scoring')
    form = st.form(key='score-form')

    document_part = form.selectbox('Select Document Part',('Title','Description','Body')) 
    document = form.text_input('Document', 'Document here!')
    model = form.selectbox(
        'Select Model', ('xlarge', 'large', 'medium', 'small'))
    form.write('Set model parameters(using the default values is recommended).')
    temperature = form.slider(label='Temperature', step=0.1, value=0.5,
                              min_value=0.0, max_value=2.0)
    token = form.text_input('Token', 50)
    top_k = form.text_input('Top-k', 0)

    top_p = form.slider(label='Top-p', step=0.1, value=0.75,
                        min_value=0.0, max_value=1.0)
    freq_p = form.slider(label='Frequency Penalty', step=0.1, value=0.5,
                         min_value=0.0, max_value=1.0)
    pres_p = form.slider(label='Presence Penalty', step=0.1, value=0.5,
                         min_value=0.0, max_value=1.0)
    
    submit = form.form_submit_button(label="Submit", help=None,
                          on_click=None, args=None, kwargs=None)
    st.write('score')
    if submit:
        score = get_score(
            news={'document': document, 'document_part': document_part, 'model': model,
                      'temperature': temperature, 'token': token,
                      'top_k': top_k, 'top_p': top_p,
                      'freq_p': freq_p, 'pres_p': pres_p})
        
        st.write(json.loads(score))