import streamlit as st
import datetime
import time
def app():
    st.title('Observational Model - Diff in diff')
    st.write("To run analysis when you don\'t have separation between control and treatment")

    st.header('Data Input')
    analysis_name = st.text_input('Name of Analysis/ Campaign')

    description =st.text_input('Enter Description','Observational Analysis of Loyalty Lvl 6, given navigation in signature webpage.')
    hypothesis =st.text_input('Describe the Hypothesis', 'People that acquired loyalty lvl6 increase sales')
    responsible =st.text_input('Responsible (email)','xxxx@yourcompany.com')
    channel =st.selectbox('Choose Channel', ['web', 'push', 'email', '3P'], 1)
    granularity = st.selectbox('Granularity', ['customer', 'geo', 'other'], 1)

    target_metric = st.selectbox('Target Metric', ['web_navigation', 'sales', 'churn', 'loyalty_acquisition'], 1)

    st.subheader('Dates')
    date_min = st.date_input('Date Init', datetime.date(2021,10,30))
    date_max = st.date_input('Date End', datetime.date(2021,10,30))
    data_rage = [date_min, date_max]

    window_size = st.number_input('Window size', 0, 100, 10)

    st.subheader('Control')
    st.write("Define the 'control' group")

    control_metric = st.selectbox('Pick one', ['web_navigation', 'sales', 'churn', 'loyalty_acquisition'], 0)
    control_variation = st.text_input('Variation', 'https://www.mercadolivre.com.br/assinaturas/nivel-6')
    control_query = st.text_input("Alternatively, provide the query (Big Query) returning CUSTOMER, DATE")

    st.subheader('Treatment')
    st.write("Define the 'treatment' group")

    treat_metric = st.selectbox('Pick one', ['web_navigation', 'sales', 'churn', 'loyalty_acquisition'], 3)
    treat_variation = st.text_input('Variation', '6')
    treat_query = st.text_input("Alternatively, provide the query (Big Query) returning CUSTOMER, DATE for treatment")

    run_button = st.button('Run')

    if run_button:
        with st.spinner(text='In progress'):
            time.sleep(5)
        st.success('Done')
        st.write("Here are your report with the results! All info already logged ")