# AlgerianForestFire

## 📊 Dataset Details

The data used in this project is based on observations from two regions of Algeria: Bejaia (Northeast) and Sidi Bel-abbes (Northwest) between June 2012 and September 2012.

*   **`Algerian_forest_fires_dataset_INITIAL.csv`**: The raw data as downloaded. The notebook includes a rigorous cleaning phase to handle region merging, type casting, missing values, and whitespace stripping.
*   **`Algerian_forest_fires_dataset_CLEANED.csv`**: The final result of the data preparation phase. This file is directly fed into the model training pipeline within the notebook.

### Features Used for Prediction

1.  **Temperature**: Noon temperature (max) in Celsius.
2.  **RH**: Relative Humidity in %.
3.  **Ws**: Wind speed in km/h.
4.  **Rain**: Total day rain in mm.
5.  **FFMC**: Fine Fuel Moisture Code index.
6.  **DMC**: Duff Moisture Code index.
7.  **ISI**: Initial Spread Index.
8.  **Classes**: Categorical input (encoded to numeric in pipeline) indicating 'fire' or 'not fire'.
9.  **Region**: Categorical input identifying Bejaia or Sidi Bel-abbes.

**Target Variable:** FWI (Fire Weather Index).

## 🛠️ Installation & Setup

To run this project locally, you will need Python installed.

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/raj4aryan/ForestFire-Predictor.git](https://github.com/raj4aryan/ForestFire-Predictor.git)
    cd ForestFire-Predictor
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

### Running the Web Application

1.  Start the Flask server:
    ```bash
    python application.py
    ```
2.  Open your web browser and navigate to localhost

***

# Algerian Forest Fire Predictor - FWI Prediction

This is an end-to-end Machine Learning project that predicts the **Fire Weather Index (FWI)**—a critical component of the Canadian Forest Fire Weather Index (FWI) System used to estimate forest fire danger—based on meteorological data from specific regions in Algeria.

The project encompasses the entire data science lifecycle: Exploratory Data Analysis (EDA), Feature Engineering, Model Training, and Deployment as a Flask Web Application.

## 🚀 Features

*   **Research & Development:** Detailed Jupyter Notebook showcasing data cleaning, visualization, and comparison of multiple linear regression models (OLS, Ridge, Lasso, ElasticNet).
*   **Selected Model:** A tuned Ridge Regression model was selected for deployment due to its balance of accuracy and generalization.
*   **Web Application:** HTML interface allowing users to input weather parameters and receive instant FWI predictions.
*   **Preprocessing Pipeline:** Input data via the web app is automatically standardized using a pre-trained `StandardScaler` to match training data conditions.

## 📂 Repository Structure

```text

├── Algerian_forest_fires_dataset_CLEANED.csv      # Post-processed dataset used for training
├── Algerian_forest_fires_dataset_INITIAL.csv      # Raw dataset (UCI Repository)
└── EDA and Model Training.ipynb                   # Data exploration and ML pipeline development
├── templates/
│   ├── home.html                                   # Web page containing the input form
│   └── index.html                                  # Basic landing/header page template
├── application.py                                  # Main Flask application script
├── requirements.txt                                # Project dependencies
├── ridge.pkl                                       # Serialized tuned Ridge Regression model
└── scaler.pkl                                      # Serialized StandardScaler object
