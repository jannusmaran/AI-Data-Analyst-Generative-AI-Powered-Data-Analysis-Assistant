# 🤖 AI Data Analyst — Generative AI Powered Data Analysis Assistant

An end-to-end AI-powered data analysis application that allows users to upload datasets and interact with their data using natural language.

The application combines **Python-based data analysis** with **Generative AI** to provide dataset insights, statistical analysis, missing value detection, interactive visualizations, and AI-generated answers.

---

## 📌 Project Overview

Data analysis often requires technical knowledge of tools such as Python, SQL, Excel, and visualization libraries.

This project aims to simplify the data analysis process by allowing users to upload a dataset and ask questions in natural language.

The application automatically analyzes the dataset using Python and Pandas, while Generative AI helps users understand the data and generate meaningful insights.

---

## 🎯 Problem Statement

Organizations collect large amounts of data, but extracting meaningful insights often requires technical expertise.

Non-technical users may find it difficult to:

- Understand dataset structure
- Identify missing values
- Perform statistical analysis
- Create visualizations
- Extract business insights
- Ask complex questions about data

The **AI Data Analyst** solves this problem by providing an interactive application where users can upload datasets and receive automated analysis and AI-powered insights.

---

## 🎯 Project Objective

The main objective of this project is to build an intelligent data analysis assistant that can:

- Upload CSV and Excel datasets
- Analyze dataset structure
- Identify missing values
- Generate statistical summaries
- Analyze categorical data
- Create interactive visualizations
- Answer questions about datasets using Generative AI
- Provide useful business insights in natural language

---

# 🚀 Features

### 📁 Dataset Upload

Users can upload:

- CSV files
- Excel (.xlsx) files

---

### 📊 Dataset Analysis

The application provides:

- Number of rows and columns
- Column names
- Data types
- Dataset preview
- Missing value analysis
- Statistical summary

---

### 📈 Interactive Visualizations

Users can generate:

- Bar Charts
- Line Charts
- Scatter Plots
- Histograms

using interactive Plotly visualizations.

---

### 🤖 Generative AI Data Assistant

Users can ask questions such as:

> What are the most important insights from this dataset?

> Are there any data quality issues?

> What trends can you identify?

> Give me business recommendations based on this data.

The AI analyzes the dataset context and provides responses in natural language.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Streamlit | Web application development |
| Plotly | Interactive data visualization |
| OpenRouter API | Access to Generative AI models |
| Requests | API communication |
| Python-Dotenv | Secure API key management |
| OpenPyXL | Excel file processing |

---

# 🏗️ Project Architecture

```text
                ┌──────────────────┐
                │   User Uploads   │
                │ CSV / Excel File │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    Streamlit     │
                │   Application    │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │      Pandas      │
                │ Data Processing  │
                └────────┬─────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
     ┌─────────────────┐   ┌─────────────────┐
     │ Data Analysis   │   │ Data Context    │
     │ & Visualization │   │ for Generative  │
     └─────────────────┘   │       AI        │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │   OpenRouter    │
                           │   Generative AI │
                           └────────┬────────┘
                                    │
                                    ▼
                           ┌─────────────────┐
                           │ AI Generated   │
                           │ Insights       │
                           └─────────────────┘
