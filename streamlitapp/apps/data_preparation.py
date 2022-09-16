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


def data_preparation(df: pd.DataFrame):

    st.write('# Promt Design')
    st.write('## Prompt Desigin for the Scoring')
    st.write('## Prompt Design for the Entity Extraction')
