
from frontend import streamlitap
from multipleapp import MultipleApp
from apps import  entity_extraction as ee
from apps import news_scoring as ns
from apps import data_preparation as dp

app = MultipleApp()
streamlitap(app,ee,ns,dp)