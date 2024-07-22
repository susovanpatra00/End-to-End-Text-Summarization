# End to End Text Summarization MLOps using Google Pegasus Model

This project demonstrates an end-to-end Machine Learning Operations (MLOps) pipeline using stages like data ingestion, data validation, data transformation, model training, and model evaluation. 


## Key Components

### 1. Data Ingestion
The data ingestion stage involves gathering data from various sources and storing it in a structured format. This project uses `samsum` dataset.

### 2. Data Validation
Data validation ensures that the data meets certain quality criteria. This involves checking for missing values, data types, and ensuring the data is within expected ranges.

### 3. Data Transformation
Data transformation involves cleaning and preprocessing the data to make it suitable for model training. This includes tasks like `tokenization`, normalization, and feature engineering.

### 4. Model Training
The model training stage involves training a machine learning model on the preprocessed data. This project uses the `google/pegasus-cnn_dailymail` model from the `transformers` library for text summarization.

### 5. Model Evaluation
Model evaluation involves assessing the performance of the trained model using various metrics like `rouge1`, `rouge2`, `rougeL`, `rougeLsum`. This ensures the model meets the required performance standards before deployment.

## Interactive App

An interactive app is built using Flask to provide a user-friendly interface for interacting with the model. The app allows users to input text and get summarized results in real-time.

### Running the App

To run the app locally, follow these steps:

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Start the Flask app:
    ```bash
    python app.py
    ```

3. Open your browser and navigate to `http://127.0.0.1:5000` to access the app.


## Notebooks

- `research/TextSummarization.ipynb`: Contains the actual process behind the whole project. 

## Understanding
- `learning.txt`: Contains the lower level explanation about the workflow.


## Acknowledgements

Special thanks to @entbappy for the learning.
