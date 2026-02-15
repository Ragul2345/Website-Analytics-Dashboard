## 📊 Website Analytics Dashboard – Interactive Data Visualization App

* A professional and interactive Website Analytics Dashboard built using Python and Streamlit to analyze and visualize website performance metrics in a clean, modern layout.
* This project demonstrates real-world data analysis and dashboard development skills using structured datasets and multiple visualization techniques.

## 📖 Project Overview

* The Website Analytics Dashboard is a data-driven web application that provides insights into website performance over time.
* It processes website analytics data from a CSV dataset and presents key performance indicators (KPIs) along with interactive visualizations to help understand traffic patterns, user behavior, device usage and
  traffic sources.

## 🚀 This Project Showcases Skills In:

* Data analysis
* Data visualization
* Dashboard design
* KPI computation
* Front-end data presentation using Streamlit

## 🛠️ Technologies Used

* Python – Core programming language
* Pandas – Data cleaning and aggregation
* Streamlit – Interactive dashboard framework
* Matplotlib – Basic plotting support
* Plotly Express – Interactive charts and visualizations

## 📂 Dataset Information

The dataset (website_analytics.csv) contains the following fields:

* date – Daily website activity date
* visitors – Number of visitors per day
* page_views – Total page views per day
* bounce_rate – Percentage of users leaving without interaction
* avg_session_duration – Average time spent on the website (seconds)
* traffic_source – Organic, Direct, Social, Referral
* device – Desktop, Mobile, Tablet
* country – Visitor country

The dashboard automatically processes and aggregates this data for visualization.

## ⚙️ Key Features
## 🔢 KPI Metrics Section

* Total Visitors
* Total Page Views
* Average Bounce Rate
* Average Session Duration

## 📈 Visitors Over Time

* Line chart showing daily visitor trends
* Helps analyze growth patterns and traffic fluctuations

## 🌍 Page Views by Country

* Bar chart comparing total page views across countries
* Useful for geographical traffic analysis

## 📱 Device Distribution

* Donut chart displaying user distribution across Desktop, Mobile and Tablet
* Helps understand device usage trends

## 🔄 Traffic Source Distribution

* Donut chart showing traffic breakdown (Organic, Direct, Social, Referral)
* Useful for marketing performance analysis

## 📋 Data Preview Section

* Displays the first 15 rows of the dataset
* Helps verify and understand raw data structure

## 🔄 Process Flow

* Load the website analytics CSV dataset
* Convert date column into proper datetime format
* Compute aggregated KPIs (sum and average values)
* Group and summarize data using Pandas
* Generate visualizations using Plotly and Streamlit
* Display all components in a structured wide dashboard layout

## 🖥️ Dashboard Layout Structure

Top Section: 
* KPI Metrics (4-column layout)

Second Section:
* Visitors Over Time (Line Chart)
* Page Views by Country (Bar Chart)

Third Section:
* Device Distribution (Donut Chart)
* Traffic Source Distribution (Donut Chart)

Bottom Section:
* Data Preview Table

## 🚀 How to Run the Project

1️⃣ Install Required Libraries
* pip install streamlit pandas matplotlib plotly

2️⃣ Place Dataset
* Ensure website_analytics.csv is in the same directory as your Python file.

3️⃣ Run the App
* streamlit run app.py

The dashboard will open automatically in your browser.

## 🎯 Learning Outcomes

* Build interactive dashboards using Streamlit
* Clean and analyze data using Pandas
* Compute real-world website KPIs
* Visualize trends and distributions
* Structure professional dashboard layouts

## 📌 Note

* This project uses a sample dataset for demonstration purposes.
* It can be extended by adding filters, date range selectors, authentication or deployment (Streamlit Cloud, Render, etc.).
* Suitable for portfolio projects, resume showcasing, and data analytics practice.
