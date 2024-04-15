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

### Conclusion
In conclusion, the project has exemplified the application of fundamental software engineering tasks to enhance data skills and attract potential employers. While the dataset used pertained to car sales advertisements, the primary focus extended beyond the dataset itself or its analysis. Instead, it aimed to showcase proficiency in critical tasks like establishing Python virtual environments, constructing a web application, and deploying it to a publicly accessible cloud platform. Insights may be uncovered that help to provide a more sophisticated knowledge of the information and its ramifications. The project acts as a stepping stone to competency in both data analysis and software engineering by continuously exploring and improving data abilities.

Furthermore, the successful launch of the project on Render has made it available for others to explore and learn from. The application's availability at the specified site means that its findings may be shared and used by a larger audience, promoting cooperation and information diffusion.

In summary, the study of the car dataset provided useful insights into numerous elements of the automotive sector. Comprehensive data investigation and visualization yielded insights into car sales patterns, popular brands, and market preferences. Addressing data inconsistencies and outliers has increased the dependability of the analysis, allowing for better informed decision-making in areas such as marketing strategies, inventory management, and product development. As the project progresses, there is a continued commitment to unearthing new insights that contribute to a better knowledge of the automotive industry environment.
