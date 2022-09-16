# import packages
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

def get_score(title:str,description:str,body:str):
    return 1,90

def news_scoring(df: pd.DataFrame):

    st.write('### News Artifact Scoring')
    form = st.form(key='score-form')
    title = form.text_input('Title', 'Title here!')
    desciption = form.text_input('Description', 'Description here!')
    body = form.text_input('Body', 'Body here!')
    
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

    if submit:
        score,prob = get_score(title=title,description=desciption,body=body)
        st.write('The news has {} with {} probability'.format(score,prob))
