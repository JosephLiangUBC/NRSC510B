import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import sqlite3


# Read data from SQLite database
conn = sqlite3.connect('/Users/Joseph/Desktop/NRSC510B/mwt_data.db')
tap_output = pd.read_sql_query("SELECT * FROM tap_response_data", conn)
conn.close()
tap_output['Strain'] = tap_output['Gene']+" ("+tap_output['Allele'] + ")"

# Streamlit Dashboard starts here
st.title('NRSC510B: Data Dashboard for MWT Data')

st.header('Data at a glance')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(tap_output)

col1, col2 = st.columns([2, 3])
col1.subheader("For A Single Phenotype")
phenotype_option = col1.selectbox(
    'Select a phenotype',
    ('placeholder', 'list', 'of','phenotypes'))
# seaborn graph of phenotypic view (sample mean distance if possible) + st.pyplot()
flights = sns.load_dataset("flights")
flights_wide = flights.pivot(index="year", columns="month", values="passengers")
sns.set_context('notebook')
fig, ax = plt.subplots()
ax=sns.barplot(flights_wide, orient='h')
col1.pyplot(fig)
col1.caption(f'Sample mean distance from wildtype for all strains for selected phenotype: {phenotype_option}')
# Insert download graph button

col2.subheader("Comprehensive Heatmap")
# seaborn graph of heatmap + st.pyplot()
glue = sns.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")
sns.set_context('notebook')
fig, ax = plt.subplots()
ax = sns.heatmap(glue)
col2.pyplot(fig)
col2.caption('Comprehensive heatmap of entire dataset')
# Insert download graph button


st.header('Gene-specific Data')
gene_option = st.selectbox(
    'Select a gene',
    (tap_output['Gene'].unique()))

col3, col4 = st.columns([1,1])
col3.subheader('phenotypic profile')
# seaborn graph of phenotypic profile of selected gene
col3.caption(f'Phenotypic profile of {gene_option}')
# Insert download graph button

col4.subheader('Rank in phenotype')
gene_phenotype_option = col4.selectbox(
    'Select a phenotype',
    ('placeholder', 'list', 'of','gene','phenotypes'))
# seaborn graph of phenotypic view (sample mean distance) + st.pyplot
col4.caption(f'Sample mean distance from wildtype for all strains for selected phenotype: {gene_phenotype_option}')
# Insert download graph button

st.subheader('Habituation Curves')
tab1, tab2, tab3 = st.tabs(["Probability of Tap-Response",
                            "Duration of Tap-Response",
                            "Speed of Tap-Response"])

with tab1:
   st.subheader("Probability")
# Seaborn graph of probability habituation curve
# Insert download graph button

with tab2:
   st.subheader("Duration")
# Seaborn Graph of Duration Habituation curve
# Insert download graph button

with tab3:
   st.subheader("Speed")
# seaborn graph of Speed Habituation Curve
# Insert download graph button



st.header('Allele-specific Data')
allele_option = st.selectbox(
    'Select a gene',
    (tap_output['Strain'].unique()))

col5, col6 = st.columns([1,1])
col5.subheader('phenotypic profile')
# seaborn graph of phenotypic profile of selected gene
col5.caption(f'Phenotypic profile of gene allele {allele_option}')
# Insert download graph button

col4.subheader('Rank in phenotype')
allele_phenotype_option = col6.selectbox(
    'Select a phenotype',
    ('placeholder', 'list', 'of','allele','phenotypes'))
# seaborn graph of phenotypic view (sample mean distance) + st.pyplot
col6.caption(f'Sample mean distance from wildtype for all strains for selected phenotype: {allele_phenotype_option}')
# Insert download graph button

st.subheader('Habituation Curves')
tab4, tab5, tab6 = st.tabs(["Probability of Tap-Response",
                            "Duration of Tap-Response",
                            "Speed of Tap-Response"])

with tab4:
   st.subheader("Probability")
# Seaborn graph of probability habituation curve
# Insert download graph button

with tab5:
   st.subheader("Duration")
# Seaborn Graph of Duration Habituation curve
# Insert download graph button

with tab6:
   st.subheader("Speed")
# seaborn graph of Speed Habituation Curve
# Insert download graph button












