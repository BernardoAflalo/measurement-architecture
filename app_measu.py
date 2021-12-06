import streamlit as st
import pandas as pd
import numpy as np
import hashlib
import datetime as DT
import altair as alt
import tab_attribution, tab_experiments, tab_experiments_add, tab_observational, aux_fun



st.title('POC Measurement as a Service')
st.markdown('Proof of Concept of Measurement as a Service. Goal is to allow different areas to perform self-service experiment analysis, quasi-experiments and attribution')




PAGES = {
    "Experiment - Add": tab_experiments_add,
    "Experiment - Analyze": tab_experiments,
    "Attribution": tab_attribution,
    "Observational": tab_observational
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()