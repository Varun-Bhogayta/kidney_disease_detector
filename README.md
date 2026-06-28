# Chronic Kidney Disease Prediction using ANN

A machine learning project that uses an Artificial Neural Network (ANN) to predict the likelihood of Chronic Kidney Disease (CKD) based on medical parameters. The project includes a Streamlit web application for interactive predictions.

## Overview

This project leverages deep learning to predict CKD status using key medical indicators such as creatinine levels, blood urea nitrogen (BUN), GFR, and other relevant parameters. The model is trained on a kidney disease dataset and deployed via a user-friendly web interface.

## Features

- **ANN Model**: Trained deep neural network for CKD prediction
- **Interactive Web App**: Streamlit-based UI for real-time predictions
- **Multiple Input Parameters**: Age, Creatinine Level, BUN, Diabetes status, Hypertension status, GFR, and Urine Output
- **Probability Output**: Returns both binary prediction and probability score

## Project Structure

```
ANN project/
├── app.py                      # Streamlit web application
├── ckd_ann_model.h5            # Trained ANN model
├── scaler.pkl                  # Saved StandardScaler for preprocessing
├── requirements.txt            # Python dependencies
├── Dataset/
│   └── kidney_disease_dataset.csv  # Training dataset
├── traning.ipynb               # Model training notebook
├── prediction.ipynb            # Prediction testing notebook
├── finding_optimal_ann_.ipynb  # Hyperparameter optimization notebook
└── logs/                       # TensorBoard logs
    └── fit/
```

## Dataset

The dataset contains medical records with the following features:

| Feature | Description |
|---------|-------------|
| Age | Patient age |
| Creatinine_Level | Serum creatinine (mg/dL) |
| BUN | Blood Urea Nitrogen (mg/dL) |
| Diabetes | Diabetes status (0/1) |
| Hypertension | Hypertension status (0/1) |
| GFR | Glomerular Filtration Rate |
| Urine_Output | Daily urine output (ml/day) |
| CKD_Status | Target variable (0/1) |
| Dialysis_Needed | Whether dialysis is required (0/1) |

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd "ANN project"
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter the required medical parameters in the web interface to get CKD predictions

## Model Architecture

The ANN model consists of:
- Input layer with 7 features
- Hidden layers with ReLU activation
- Output layer with sigmoid activation for binary classification

## Dependencies

- TensorFlow
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Streamlit
- TensorBoard
- Scikeras

## License

This project is for educational and research purposes.
