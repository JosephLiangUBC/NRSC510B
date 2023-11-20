# NRSC510B: Phenotype Data Dashboard for Multi-Worm Tracker Data

![Screenshot](https://github.com/JosephLiangUBC/NRSC510B/assets/41761806/4efb54c7-940e-46ff-a355-0a8fbbe32484)

<!-- About The Project -->
## About The Project

In 2019, the Parkinson’s Genomic Consortium identified 87 risk genes for Parkinson’s Disease (PD) in the largest genome wide association study (GWAS) meta-analyses to date[1]. Currently, not a lot is known about many of these newly identified genes especially in the context of PD. Because many PD-associated genes have orthologs expressed in the nematode Caenorhabditis elegans, I am systematically testing strains with loss-of-function mutations in nematode orthologs of PD risk genes using the Multi-Worm Tracker (MWT), which allows for the characterization of many freely moving animals simultaneously across up to 28 phenotypes[2]. With this data, I aim to: 1. Add functional annotation for many of these under-studied genes, 2. By clustering with MWT datasets from other screens in the lab identify disease-relevant phenotypes that are enriched in the PD gene cohort, and 3. Potentially identify subtypes of PD with the phenotypes extracted. I will build a data dashboard to make easily accessible data visualizations to help answer the following research questions: 1. Among all nematode phenotypes measured, are there disease-relevant phenotypes that are especially enriched in the PD-specific dataset? 2. Using these phenotypes, would it be possible to extract from our dataset potential subgroups of PD-relevant genes? With the dashboard, this project will contribute to the research field by making relevant MWT data more accessible to the community. Additionally, data from this project will help add functional annotation for understudied PD-linked risk genes.

PMID 31701892 2. PMID 21642964


<!-- Dataset Description -->
## Dataset Descirption
The dataset used for this project is the data output of 23 phenotypes from the MWT collected by the myself and other students within the Rankin Lab (101 strains and counting, each with sample size of ~50-100 worms per plate for up to 5 replicates each). The raw data (it is uninterpretable and requires translation through a proprietary java program) was processed and stored in .csv file formats that are stored within the original experiment files. All 23 phenotypes are numerical in nature, ranging from morphological (length, width, area) to behaviour metrics (speed, response sensitivity and habituation metrics). All experimental data from the dataset are stored in a network-attached storage (NAS) affiliated with the Psychology department at UBC, distributed across separate folders, organized by date. As our lab generated this data ourselves, there are no permissions required for its reuse. The contents of the OSF page are licensed by GNU General Public License (GPL) 3.0, as currently intention is only to make the underlying code publicly available. Because a majority of the data used for this project is currently unpublished data, the dataset is licensed by Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND 4.0) International.


<!-- Coding Component -->
## Coding Component
The project is written in Python for its flexibility and compatibility with a number of data-science, statistics and visualization packages. After initial processing, data is stored in .db format as an efficient database management language (through the sqlite3 package). Numpy and pandas were used for the manipulation of the high-dimension dataset, Scipy and statsmodels packages was used for any statistical analyses. Streamlit and seaborn is used for data visualization and the user interface of the data dashboard.

<!-- Getting Started -->
## Getting Started

### Prerequesites
The code was executed using the following Python version and platform:

Python version v.3.11.1 (2022-12-06)
Copyright (C) Python Software Foundation
Platform: Apple M1 Pro on macOS Ventura v13.5.2 (ARM 64-bit)

#### System Packages
* ipyfilechooser 0.6.0
* jupyter 1.0.0
* matplotlib 3.7.1
* notebook 7.0.2
* numpy 1.24.3
* pandas 2.0.2
* requests 2.28.2
* scipy 1.10.1
* seaborn 0.12.2
* streamlit 1.27.2
* tqdm 4.65.0

### Data
All data used by the streamlit app is stored in 'mwt_data.db'
Download 'mwt_data.db' file from the OSF page.

<!-- USAGE EXAMPLES -->
## Usage
Download NRSC510B_app.py from GitHub

### Command line
To run the streamlit app after its download:
In terminal/command prompt, navigate towards the local directory of NRSC510B_app.py
Then run streamlit app:
```
streamlit run NRSC510B_app.py
```
<!-- LICENSE -->
## License

Distributed under the GNU General Public License (GPL) 3.0

<!-- Laundry List of Improvements -->
## List of things I am currently working on to improve the app:


<!-- CONTACT -->
## Contact

For questions or comments specific to the implementation provided in this repository, please contact:

Joseph Liang - [GitHub](https://github.com/JosephLiangUBC) - joseph.liang@psych.ubc.ca

Additional questions about the project, such as further information and requests for data should be directed to and will be fulfilled by the Lead Contact, Catharine H. Rankin (crankin@psych.ubc.ca)

<!-- Project Author -->
## Project Author
* Joseph Liang

