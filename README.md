
# 🌿 Smart Home Energy Consumption Estimator

This is a beginner-friendly web application built with **Streamlit** and a **Random Forest model** to predict a home's **monthly energy usage (in kWh)** based on household and environmental inputs.

---

## 📌 Project Description

The project aims to help individuals estimate how much energy their home consumes by inputting details such as number of occupants, house size, income, outdoor temperature, heating/cooling types, and other features. It uses a pre-trained Random Forest Regressor to make predictions.



## 🧠 Technologies Used

- Python
- Streamlit
- Pandas
- Joblib (for model loading)
- Scikit-learn (model trained beforehand)



## 📁 Project Structure

| File                    | Description                                           |
|-------------------------|-------------------------------------------------------|
| `s.py`                  | Main Streamlit application with UI and logic          |
| `RandomForestModel.pkl` | Trained Random Forest model used for prediction       |
| `requirements.txt`      | Python dependencies required to run the project       |
| `README.md`             | Project overview and setup instructions (this file)   |



## 🚀 How to Run the Project

> 🧑‍💻 Perfect for beginners. Follow these steps:

### 1. Clone the Repository


git clone https://github.com/YourUsername/Smart-Energy-Estimator.git
cd Smart-Energy-Estimator


Or download and extract the ZIP.


### 2. Install Required Packages

Create and activate a virtual environment (optional):

python -m venv venv
venv\Scripts\activate  # On Windows

Then install the dependencies:


pip install -r requirements.txt

If `requirements.txt` is not available, install manually:

pip install streamlit pandas joblib



### 3. Run the Streamlit App


streamlit run s.py


After a few seconds, your browser will open the application at:

http://localhost:8501




## ✨ App Features

- 📊 Predict monthly energy usage in kilowatt-hours (kWh)
- 🎯 Takes detailed inputs such as:
  - Number of occupants
  - House size (sqft)
  - Heating and cooling types
  - Monthly income
  - Outdoor temperature
  - Day, month, year
  - Certified energy star home
- 📦 Displays a summary of the prediction inputs
- 🌈 Visually pleasing UI with background image and styled components






## 🧠 ML Model Insights

The Random Forest model uses features like:
- One-hot encoding for heating and cooling type
- Season detection (winter, summer, etc.)
- Day of the week, weekend flag
- Income per person, sqft per person
- High income and low temperature flags

All these are automatically derived from your inputs before prediction.








