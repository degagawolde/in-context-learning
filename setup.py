
from streamlitapp.frontend_main import streamlitap
from streamlitapp.multipleapp import MultipleApp
from streamlitapp.apps import  entity_extraction as ee
from streamlitapp.apps import news_scoring as ns
from streamlitapp.apps import data_preparation as dp

app = MultipleApp()
streamlitap(app,ee,ns,dp)
