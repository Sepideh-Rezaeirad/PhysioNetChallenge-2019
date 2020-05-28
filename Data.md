# Data 
Data used in the competition is sourced from ICU patients in three separate hospital systems. Data from two hospital systems will be publicly available; however, one data set will be censored and used for scoring. The data for each patient will be contained within a single pipe-delimited text file. Each file will have the same header and each row will represent a single hour's worth of data. Available patient co-variates consist of Demographics, Vital Signs, and Laboratory values, which are defined in [Challenge Data].(https://physionet.org/content/challenge-2019/1.0.0/)

# Data Description
The Challenge data repository contains one file per subject (e.g., training/p00101.psv for the training data). Each training data file provides a table with measurements over time. Each column of the table provides a sequence of measurements over time (e.g., heart rate over several hours), where the header of the column describes the measurement. Each row of the table provides a collection of measurements at the same time (e.g., heart rate and oxygen level at the same time).

# Accessing the Data
[Click here](https://archive.physionet.org/pnw/challenge-2019-request-access) to download the complete training database (42 MB), consisting of two parts: training set A (20,336 subjects) and B (20,000 subjects).


### In this Repository

- `Supporting Scripts/`
  - `Cluster` 
  - `Evaluation` 
  - `Imputation` 
  - `Train_Prediction` 
 

