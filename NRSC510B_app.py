import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import sqlite3
import io

@st.cache_data
def read(table):
    result = pd.read_sql_query(f"SELECT * FROM {table}", conn)
    return result

# Read data from SQLite database
conn = sqlite3.connect('/Users/Joseph/Desktop/NRSC510B/mwt_data.db')
tap_output = read('tap_response_data')
# tap_baseline = read('tap_baseline_data')
tap_tstat_allele = read('tstat_data')
allele_metric_data=read('allele_phenotype_data')

# tap_output = pd.read_sql_query("SELECT * FROM tap_response_data", conn)
# tap_baseline = pd.read_sql_query("SELECT * FROM tap_baseline_data", conn)
conn.close()
tap_output['Strain'] = tap_output['Gene']+" ("+tap_output['Allele'] + ")"

# Streamlit Dashboard starts here
st.title('NRSC510B: Data Dashboard for MWT Data')

st.header('Data at a glance')

if st.checkbox('Show raw tap data'):
    st.subheader('Raw tap data')
    st.write(tap_output)
#
# if st.checkbox('Show raw baseline data'):
#     st.subheader('Raw baseline data')
#     st.write(tap_baseline)
#
# if st.checkbox('Show tstat data'):
#     st.subheader('tstat data')
#     st.write(tap_tstat_allele)

col1, col2 = st.columns([2, 3])

col1.subheader("For A Single Phenotype")

phenotype_option = col1.selectbox(
    'Select a phenotype',
    tap_tstat_allele.columns.values[1:])

# seaborn graph of phenotypic view (sample mean distance if possible) + st.pyplot()
sns.set_context('notebook')
fig, ax = plt.subplots(figsize=(4,20))
ax = sns.barplot(data = allele_metric_data[allele_metric_data.Metric==phenotype_option],
            x="T_score",
            y="dataset",orient='h',
            palette=["dimgray"]).set_title(f"{phenotype_option}")
plt.xlabel('T-Score')
plt.ylabel('')
col1.pyplot(fig)
col1.caption(f'Sample mean distance from wildtype for all strains for selected phenotype: {phenotype_option}')

# Insert download graph button

col2.subheader("Comprehensive Heatmap")
sns.set_context('notebook', font_scale=1)
fig, ax = plt.subplots(figsize=(15, 20))
# ax = sns.heatmap(glue)

ax = sns.heatmap(data = tap_tstat_allele.set_index('dataset').drop(index="N2"),
                 annot=False,
                 linewidth=0.2,
                 square=True,
                 cmap="vlag",
#                  cmap=sns.diverging_palette(55, 250, s=100, l=40,as_cmap=True),
                 center=0,
                 vmax=3,
                 vmin=-3,
                 # xticklabels='auto',
                 # yticklabels='auto',
                 cbar_kws={"shrink": .2, "pad": 0.01})
ax.set(xlabel="", ylabel="")
col2.pyplot(fig)
col2.caption('Comprehensive heatmap of entire dataset')
# Insert download graph button
# Insert download csv

st.header('Gene-specific Data')
gene_option = st.selectbox(
    'Select a gene',
    (tap_output['Gene'].unique()))


tap_output_gene=tap_output[tap_output['Gene']==gene_option]
# st.write(tap_output_allele)
# st.write(tap_output_allele['Date'].unique())
gene_tap_data=tap_output[tap_output['Date'].isin(tap_output_gene['Date'].unique())]
gene_tap_data_plot=gene_tap_data[gene_tap_data['Gene'].isin(['N2', gene_option])]
gene_tap_data_plot['taps']=gene_tap_data_plot['taps'].astype(int)
st.write(gene_tap_data_plot)


col3, col4 = st.columns([1,1])
col3.subheader('phenotypic profile')
# seaborn graph of phenotypic profile of selected gene
col3.caption(f'Phenotypic profile of {gene_option}')
# Insert download graph button

col4.subheader('Rank in phenotype')
gene_phenotype_option = col4.selectbox(
    'Select a phenotype',
    ('list', 'of','gene','phenotypes'))
# seaborn graph of phenotypic view (sample mean distance) + st.pyplot
col4.caption(f'Sample mean distance from wildtype for all strains for selected phenotype: {gene_phenotype_option}')
# Insert download graph button

st.subheader('Habituation Curves')
tab1, tab2, tab3 = st.tabs(["Probability of Tap-Response",
                            "Duration of Tap-Response",
                            "Speed of Tap-Response"])

with tab1:
   #  Habituation of Response Probability Plot
   st.subheader("Probability")
   fig, ax = plt.subplots(figsize=(12, 10))
   # seaborn plot
   plt.gca().xaxis.grid(False)  # <- gets rid of x-axis markers to make data look clean
   ax = sns.pointplot(x="taps",  # <- Here we use seaborn as our graphing package.
                      y="prob",
                      data=gene_tap_data_plot,
                      hue='Gene',  # <- Here we use the extra column from step 6 to separate by group
                      errorbar='se')  # <- Confidence interval. 95 = standard error
   plt.xlabel("Taps")  # <- X-axis title
   plt.ylabel("Probability")  # <- Y-Axis title
   plt.title("Habituation of Response Probability", fontsize='16')  # <- Figure Title
   plt.ylim(0, 1)
   ax.legend(loc='upper right', fontsize='12')  # <- location of your legend

   tab1.pyplot(fig)
   tab1.caption(f'Habituation of Response Probability: {gene_option}')

   # download graph button
   img1 = io.BytesIO()
   plt.savefig(img1, format='png', dpi=300, bbox_inches='tight')
   st.download_button(label="Download Plot",
                      data=img1,
                      file_name=f"Probability of Tap Habituation {gene_option}.png",
                      mime="image/png",
                      key='dnldbtn1')


with tab2:
   #  Habituation of Response Duration Plot
   st.subheader("Duration")
   fig, ax = plt.subplots(figsize=(12, 10))
   # seaborn plot
   ax = sns.pointplot(x="taps",
                      y="dura",
                      data=gene_tap_data_plot,
                      hue='Gene',
                      # palette=pal,
                      errorbar='se')
   plt.xlabel("Taps", fontsize='12')
   plt.ylabel("Duration", fontsize='12')
   plt.title("Habituation of Response Duration", fontsize='16')
   plt.ylim(0, None)
   ax.legend(loc='upper right', fontsize='12')
   tab2.pyplot(fig)
   tab2.caption(f'Habituation of Response Duration: {gene_option}')

   # download graph button
   img2 = io.BytesIO()
   plt.savefig(img2, format='png', dpi=300, bbox_inches='tight')
   st.download_button(label="Download Plot",
                      data=img2,
                      file_name=f"Duration of Tap Habituation {gene_option}.png",
                      mime="image/png",
                      key='dnldbtn2')
# Seaborn Graph of Duration Habituation curve
# Insert download graph button

with tab3:
   #  Habituation of Response Speed Plot
   st.subheader("Speed")
   fig, ax = plt.subplots(figsize=(12, 10))
   # seaborn plot
   ax = sns.pointplot(x="taps",
                      y="speed",
                      data=gene_tap_data_plot,
                      hue='Gene',
                      errorbar='se')
   plt.xlabel("Taps", fontsize='12')
   plt.ylabel("Speed", fontsize='12')
   plt.title("Habituation of Response Speed", fontsize='16')
   plt.ylim(0, None)
   ax.legend(loc='upper right', fontsize='12')
   tab3.pyplot(fig)
   tab3.caption(f'Habituation of Response Speed: {gene_option}')

   # download graph button
   img3 = io.BytesIO()
   plt.savefig(img3, format='png', dpi=300, bbox_inches='tight')
   st.download_button(label="Download Plot",
                      data=img3,
                      file_name=f"Speed of Tap Habituation {gene_option}.png",
                      mime="image/png",
                      key='dnldbtn3')
# seaborn graph of Speed Habituation Curve
# Insert download graph button



st.header('Allele-specific Data')
allele_option = st.selectbox(
    'Select a allele',
    (tap_output['dataset'].unique()))



tap_output_allele=tap_output[tap_output['dataset']==allele_option]
# st.write(tap_output_allele)
# st.write(tap_output_allele['Date'].unique())
allele_tap_data=tap_output[tap_output['Date'].isin(tap_output_allele['Date'].unique())]
allele_tap_data_plot=allele_tap_data[allele_tap_data['dataset'].isin(['N2', allele_option])]
allele_tap_data_plot['taps']=allele_tap_data_plot['taps'].astype(int)
# st.write(allele_tap_data_plot)

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
   #  Habituation of Response Probability Plot
   st.subheader("Probability")
   fig, ax = plt.subplots(figsize=(12, 10), linewidth=2.5)
   # seaborn plot
   plt.gca().xaxis.grid(False)  # <- gets rid of x-axis markers to make data look clean
   ax = sns.pointplot(x="taps",  # <- Here we use seaborn as our graphing package.
                      y="prob",
                      data=allele_tap_data_plot,
                      hue='dataset',  # <- Here we use the extra column from step 6 to separate by group
                      errorbar='se')  # <- Confidence interval. 95 = standard error
   plt.xlabel("Taps")  # <- X-axis title
   plt.ylabel("Probability")  # <- Y-Axis title
   plt.title("Habituation of Response Probability", fontsize='16')  # <- Figure Title
   plt.ylim(0, 1)
   ax.legend(loc='upper right', fontsize='12')  # <- location of your legend

   tab4.pyplot(fig)
   tab4.caption(f'Habituation of Response Probability: {allele_option}')

   # download graph button
   img4 = io.BytesIO()
   plt.savefig(img4, format='png', dpi=300, bbox_inches='tight')
   st.download_button(label="Download Plot",
                      data = img4,
                      file_name=f"Probability of Tap Habituation {allele_option}.png",
                      mime="image/png",
                      key='dnldbtn4')

with tab5:
   #  Habituation of Response Duration Plot
   st.subheader("Duration")
   fig, ax = plt.subplots(figsize=(12, 10))
   # seaborn plot
   ax = sns.pointplot(x="taps",
                      y="dura",
                      data=allele_tap_data_plot,
                      hue='dataset',
                      # palette=pal,
                      errorbar='se')
   plt.xlabel("Taps", fontsize='12')
   plt.ylabel("Duration", fontsize='12')
   plt.title("Habituation of Response Duration", fontsize='16')
   plt.ylim(0, None)
   ax.legend(loc='upper right', fontsize='12')
   tab5.pyplot(fig)
   tab5.caption(f'Habituation of Response Duration: {allele_option}')

   # download graph button
   img5 = io.BytesIO()
   plt.savefig(img5, format='png', dpi=300, bbox_inches='tight')
   st.download_button(label="Download Plot",
                      data = img5,
                      file_name=f"Duration of Tap Habituation {allele_option}.png",
                      mime="image/png",
                      key='dnldbtn5')


with tab6:
   #  Habituation of Response Speed Plot
   st.subheader("Speed")
   fig, ax = plt.subplots(figsize=(12, 10))
   # seaborn plot
   ax = sns.pointplot(x="taps",
                      y="speed",
                      data=allele_tap_data_plot,
                      hue='dataset',
                      errorbar='se')
   plt.xlabel("Taps", fontsize='12')
   plt.ylabel("Speed", fontsize='12')
   plt.title("Habituation of Response Speed", fontsize='16')
   plt.ylim(0, None)
   ax.legend(loc='upper right', fontsize='12')
   tab6.pyplot(fig)
   tab6.caption(f'Habituation of Response Speed: {allele_option}')

   # download graph button
   img6 = io.BytesIO()
   plt.savefig(img6, format='png', dpi=300, bbox_inches='tight')
   st.download_button(label="Download Plot",
                      data = img6,
                      file_name=f"Speed of Tap Habituation {allele_option}.png",
                      mime="image/png",
                      key='dnldbtn6')













