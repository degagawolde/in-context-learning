import streamlit as st
import logging
import os,sys,io
import pandas as pd

def streamlitap(app,ee,ns,dp):
    # Add all your application her

    app.add_app("Prompt Design",dp.data_preparation,pd.DataFrame)
    app.add_app("Entity Extraction", ee.entity_extraction,pd.DataFrame)
    app.add_app('News Artifact Scoring', ns.news_scoring, pd.DataFrame)

    # The main app
    app.run()