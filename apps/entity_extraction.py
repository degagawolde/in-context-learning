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

def entity_extraction(df: pd.DataFrame):
    
    st.write('### Extract Entity From Job Description')
    
