## **Seoul Bike Sharing Demand Analysis & Dashboard** 🚴
This project analyzes the Seoul Bike Sharing Demand dataset, performs data cleaning, exploratory data analysis (EDA), and delivers interactive visualizations via a Streamlit dashboard.
##  **Project Structure**

```
Bike-dashboard/
├── app.py                      # Streamlit dashboard app
├── data_cleaning.py            # Script for data cleaning
├── eda.py                      # Notebook/script for exploratory analysis & plots
├── load_data.py                # Data loading and inspection utilities
├── test_data.py                # Automated tests for data integrity and functions
├── SeoulBikeData.csv           # Raw Kaggle dataset
├── SeoulBikeData_cleaned.csv   # Cleaned, processed dataset
└── requirements.txt            # Python package dependencies
```
##  **Description**
**Goal:** Explore patterns in bike rental demand across time, weather, holidays, and seasons, and visualize insights with an interactive dashboard.
Features:

* Data cleaning (duplicates, types, categorical consistency)
* Statistical checks for outliers and negative values
* EDA with Matplotlib & Seaborn
* Streamlit dashboard with date, season, hour, and monthly trends
* Automated tests for robust, reproducible data processing

## **Getting Started**
### 1. Clone this repo
 ``` 
git clone <your-repo-url>
 ``` 
 ``` 
cd Bike-dashboard
 ``` 

### 2. Install dependencies
(optional) First create & activate a virtual environment:

``` 
python -m venv .venv
``` 
``` 
source .venv/bin/activate# On Windows: .venv\Scripts\activate
 ``` 
 ``` 
 pip install -r requirements.txt
 ``` 

#### Then install requirements:

 ``` 
pip install -r requirements.txt
 ``` 

### 3. Data Preparation
Place SeoulBikeData.csv in the project folder (get from Kaggle).

#### Run the cleaning script:

 ``` 
python data_cleaning.py
 ``` 

This outputs SeoulBikeData_cleaned.csv.

### 4. Run automated tests
 ``` 
pytest -v
 ```
Verifies data types, cleaning, and filtering logic.

### 5. Launch the dashboard
 ``` 
streamlit run app.py
 ``` 

### Opens an interactive web interface to explore bike rental patterns visually.

##  **Dashboard Features**
**Filters: Month, Hour, Season, Date range selection**

**Visualizations:**

* Daily rental trends (line plot)

* Hourly usage patterns (boxplot)

*  Monthly totals (bar chart)

* Feature correlation heatmap

## Testing
* All core data functions are tested with pytest in test_data.py.

* Tests cover correct data loading, cleaning, and filtering.

**📝 Notes**
- If you see encoding issues, ensure the CSV is read using encoding='latin1'.

- To add your own analyses, modify eda.py or expand the dashboard in app.py.

##  Dataset Source
[Seoul Bike Sharing Demand on Kaggle](https://www.kaggle.com/datasets/saurabhshahane/seoul-bike-sharing-demand-prediction)

## Author / Credits
Developed by **Ansal P Mathew**