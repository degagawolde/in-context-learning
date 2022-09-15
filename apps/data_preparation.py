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

    st.write('## Data Preparation')
    st.write('- News Artifact data preparation')
    st.write('- Job Description data preparation')
