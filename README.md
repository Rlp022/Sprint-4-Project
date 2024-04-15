# Streamlit Web Application for Vehicle Data Visualization

## Project Overview

This project focuses on applying fundamental software engineering tasks to enhance your data skills and enhance your appeal to prospective employers. Core tasks include establishing and overseeing Python virtual environments, constructing a web application, and deploying it to a publicly accessible cloud platform.

Although the project employed a dataset of car sales advertisements, the primary emphasis wasn't on the dataset or its analysis. You have the flexibility to select any dataset that piques your interest.

1. What are the common attributes associated with the vehicles in the dataset, and how do they contribute to understanding the vehicle data?
2. How does the presence of missing values in certain columns impact the quality of the dataset, and what steps can be taken to address this issue?
3. What insights can be gained from analyzing the distribution of vehicle sales by manufacturer, condition, and type, and how does this information inform decision-making in the automotive industry?
## Steps Involved

### Step 1: Project Prerequisites

- Established a GitHub account and initialized a repository containing README.md and .gitignore files.
- Installed requisite packages such as pandas, streamlit, and plotly-express.
- Established a Render.com account and connected it to GitHub.
- Installed and configured VS Code, ensuring alignment of the Python interpreter with the virtual environment.

### Step 2: Data Acquisition

- Downloaded the car advertisement dataset (vehicles_us_cleaned.csv) and placed it in the root directory of the project.

### Step 3: Exploratory Data Analysis

- Formulated an EDA.ipynb Jupyter notebook to perform exploratory data analysis
- Utilized the plotly-express library to craft histograms and scatterplots.
- Initially prototyped the visualizations within the Jupyter notebook before integrating them into the web application.

### Step 4: Web Application Development

- Developed an app.py file in the project's root directory.
- Imported essential modules such as streamlit, pandas, and plotly_express.
- Utilized pandas to load CSV data into a DataFrame.
- Integrated a variety of streamlit components including headers, histograms, scatter plots, and checkboxes into the app.
- Revised README file to encompass a fundamental project overview and guidance for other users to execute the project locally.

### Step 5: Deployment to Render
- Streamlit configuration file was added to the GitHub repository.
- A new web service linked to the GitHub repository was created in Render.
- Render web service was configured to install necessary packages and run the app.py file.
- The final version of the application was deployed on Render.
- Verified the application's accessibility at: https://sprint-4-project-0xew.onrender.com
