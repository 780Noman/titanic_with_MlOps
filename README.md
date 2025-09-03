# 🚢 Titanic Survival Prediction - Streamlit App

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

This project is an end-to-end machine learning application that predicts whether a passenger would have survived the Titanic disaster. The model is built using a `scikit-learn` pipeline and deployed as a fully interactive web application using Streamlit.

## 🚀 Live Demo

**[➡️ View the live application here](https://your-app-url.streamlit.app/)**

*(Note: Replace the URL above with the link to your deployed app on Streamlit Community Cloud.)*

## 📸 Screenshot

*A screenshot of the running application:*



*(Note: Replace the URL above with a link to a screenshot of your running application.)*

## ✨ Features

- **Interactive UI:** User-friendly interface to input passenger data (Class, Sex, Age, etc.).
- **Real-Time Predictions:** Instantly get a survival prediction from the trained Random Forest model.
- **Prediction Confidence:** View the probability of the prediction to understand the model's confidence.
- **Reproducible ML Pipeline:** Built with a `scikit-learn` pipeline to ensure consistent preprocessing and prediction.
- **Custom Theming:** A clean, dark-themed interface configured via Streamlit's theming system.

## 🛠️ Technology Stack

- **Language:** `Python`
- **Machine Learning:** `scikit-learn`, `pandas`, `numpy`
- **Web Application:** `Streamlit`
- **Deployment:** `Streamlit Community Cloud`

## 📂 Project Structure

The repository is organized as follows, following best practices for a deployable Streamlit application:

```
.
├── .streamlit/
│   └── config.toml   # Streamlit theme and server configuration
├── app.py            # The main Streamlit application script
├── pipe.pkl          # Serialized pre-trained model pipeline
├── requirements.txt  # Python dependencies for reproducibility
└── README.md         # You are here!
```

## ⚙️ Setup and Local Installation

To run this project on your local machine, follow these steps:

**1. Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
*(Replace `your-username/your-repo-name` with your actual GitHub repository path.)*

**2. Create and Activate a Virtual Environment (Recommended)**
- This isolates the project's dependencies from your system's Python installation.

*On Windows:*
```bash
python -m venv venv
.\venv\Scripts\activate
```

*On macOS/Linux:*
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**
- The `requirements.txt` file contains all the necessary libraries.
```bash
pip install -r requirements.txt
```

**4. Run the Streamlit App**
- Once the dependencies are installed, you can start the application.
```bash
streamlit run app.py
```
Your web browser should automatically open with the application running.

## ☁️ Deployment

This application is designed for easy deployment on **Streamlit Community Cloud**.

- The deployment is handled directly from the `main` branch of the GitHub repository.
- Streamlit Cloud automatically reads the `requirements.txt` file, installs the dependencies, and runs the `app.py` script.
- Any push to the `main` branch will trigger an automatic update of the live application.

## 🔮 Future Improvements

This project serves as a strong foundation. Future MLOps enhancements could include:

- **CI/CD Pipeline:** Automate testing and deployment using GitHub Actions.
- **Experiment Tracking:** Integrate tools like MLflow to log and compare different model versions.
- **Model Monitoring:** Implement a system to monitor the live model for data drift and performance degradation.

---
