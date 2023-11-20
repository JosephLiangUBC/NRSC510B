# NRSC510B: Phenotype Data Dashboard for Multi-Worm Tracker Data

![Screenshot 2023-11-20 at 12 28 39 PM](https://github.com/JosephLiangUBC/NRSC510B/assets/41761806/4efb54c7-940e-46ff-a355-0a8fbbe32484)

<!-- About The Project -->
## About The Project

In 2019, the Parkinson’s Genomic Consortium identified 87 risk genes for Parkinson’s Disease (PD) in the largest genome wide association study (GWAS) meta-analyses to date[1]. Currently, not a lot is known about many of these newly identified genes especially in the context of PD. Because many PD-associated genes have orthologs expressed in the nematode Caenorhabditis elegans, I am systematically testing strains with loss-of-function mutations in nematode orthologs of PD risk genes using the Multi-Worm Tracker (MWT), which allows for the characterization of many freely moving animals simultaneously across up to 28 phenotypes[2]. With this data, I aim to: 1. Add functional annotation for many of these under-studied genes, 2. By clustering with MWT datasets from other screens in the lab identify disease-relevant phenotypes that are enriched in the PD gene cohort, and 3. Potentially identify subtypes of PD with the phenotypes extracted. I will build a data dashboard to make easily accessible data visualizations to help answer the following research questions: 1. Among all nematode phenotypes measured, are there disease-relevant phenotypes that are especially enriched in the PD-specific dataset? 2. Using these phenotypes, would it be possible to extract from our dataset potential subgroups of PD-relevant genes? With the dashboard, this project will contribute to the research field by making relevant MWT data more accessible to the community. Additionally, data from this project will help add functional annotation for understudied PD-linked risk genes.

PMID 31701892 2. PMID 21642964


<!-- Dataset Description -->
## Dataset Descirption
The dataset used for this project is the data output of 28 phenotypes from the MWT collected by the myself and other students within the Rankin Lab (101 strains and counting, each with sample size of ~50-100 worms per plate for up to 5 replicates each). The raw data (it is uninterpretable and requires translation through a proprietary java program) was processed and stored in .csv format. All 28 phenotypes are numerical in nature, variables range from morphological (length, width, area) to behaviour metrics (speed, response sensitivity and habituation metrics). The dataset is stored in a network-attached storage (NAS) affiliated with the Psychology department at UBC and in an external hard drive. As our lab generated this data ourselves, there are no permissions required for its reuse.


<!-- Coding Component -->
## Coding Component
The project is written in Python for its flexibility and compatibility with a number of data-science, statistics and visualization packages. After initial processing, data is be stored in SQLite as an efficient database management language (through the sqlite3 package). Numpy and pandas were used for the manipulation of the high-dimension dataset, Pingouin and scipy and statsmodels packages was used for any statistical analyses and Plotly and streamlit is be used for data visualization and the user interface of the data dashboard.

<!-- Steps and Project Timeline -->
## Steps required for project completion:

Backend (on Jupyter Notebook):

* Adapt old code to generate pd.Dataframe from MWT data (in the past this would then be saved in experiment-specific .csv files)
*     complete
* Perform statistical analyses (T-Test to Control group run in each experiment, Sample Mean Distance from Control for phenotype distribution, umap clustering for dimension reduction) - output in separate pd.DataFrame(s)
*     anticipated completion Nov. 10
* Create SQLite database file/server (sqlite3)
*     local .db file approach complete
* Convert all pd.Dataframes to SQLite tables and save to one .db data file (pandas.DataFrame.to_sql)
*     local .db file approach complete
* Update .db database (if possible, upload to a publicly hosted server)
*     anticipated completion Nov. 10


Frontend (Data Dashboard on Streamlit):

* Connect to and retrieve various SQL tables from SQLite file (.db) from local file (and if possible from a server). (sqlite3 & pandas.DataFrame.from_sql)
*     local .db file approach complete
* Data visualization (seaborn)
*     nearly complete (anticipated completion Nov. 15)
* Data dashboard (streamlit)
*     anticipated completion Nov. 17-21


<!-- Getting Started -->
## Getting Started

### Prerequesites

#### System Packages

### Installation

### Data

### Additional Data

### Configuration

<!-- USAGE EXAMPLES -->
## Usage

### Command line

<!-- LICENSE -->
## License


<!-- CONTACT -->
## Contact


