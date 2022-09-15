from apps.data_preparation import data_preparation
import streamlit as st
import logging
import io
import os
import pandas as pd
from multipleapp import MultipleApp
# import your app modules here
from apps import entity_extraction, news_scoring,data_preparation


app = MultipleApp()

# Add all your application her

app.add_app("Data Preparation",data_preparation.data_preparation,pd.DataFrame())
app.add_app("Entity Extraction", entity_extraction.entity_extraction,pd.DataFrame())
app.add_app('News Artifact Scoring', news_scoring.news_scoring, pd.DataFrame())

# The main app
app.run()
