import streamlit as st
import pickle
import pandas as pd

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- MODEL LOADING ---
@st.cache_resource
def load_pipeline():
    """Loads the pre-trained machine learning pipeline from the pickle file."""
    try:
        with open('pipe.pkl', 'rb') as f:
            pipeline = pickle.load(f)
        return pipeline
    except FileNotFoundError:
        st.error("Model file ('pipe.pkl') not found. Please ensure it's in the same directory as app.py.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading the model: {e}")
        return None

pipeline = load_pipeline()

# --- APP INTERFACE ---
if pipeline is not None:
    st.title("🚢 Titanic Survival Prediction")
    st.markdown(
        "This application uses a Machine Learning model to predict whether a passenger "
        "would have survived the Titanic disaster. Please provide the passenger's details below."
    )

    # --- USER INPUTS in a Form ---
    with st.form("prediction_form"):
        st.header("Passenger Details")
        
        col1, col2 = st.columns(2)

        with col1:
            pclass = st.selectbox('Passenger Class (Pclass)', [1, 2, 3], help="Select the passenger's ticket class.")
            sex = st.selectbox('Sex', ['male', 'female'], help="Select the passenger's gender.")
            age = st.number_input('Age', min_value=0, max_value=120, value=30, step=1, help="Enter the passenger's age.")

        with col2:
            sibsp = st.number_input('Siblings/Spouses Aboard (SibSp)', min_value=0, max_value=10, value=0, help="Number of siblings or spouses aboard.")
            fare = st.number_input('Fare', min_value=0.0, max_value=1000.0, value=50.0, format="%.2f", help="Fare paid by the passenger.")
            embarked = st.selectbox('Port of Embarkation', ['S', 'C', 'Q'], help="S = Southampton, C = Cherbourg, Q = Queenstown.")

        # Submit button for the form
        submit_button = st.form_submit_button(label='**Predict Survival**')

    # --- PREDICTION LOGIC ---
    if submit_button:
        input_data = {
            'Pclass': pclass,
            'Sex': sex,
            'Age': age,
            'SibSp': sibsp,
            'Fare': fare,
            'Embarked': embarked
        }
        input_df = pd.DataFrame([input_data])

        try:
            prediction = pipeline.predict(input_df)
            prediction_proba = pipeline.predict_proba(input_df)

            st.markdown("---")
            st.subheader("Prediction Result")

            if prediction[0] == 1:
                survival_probability = prediction_proba[0][1]
                st.success(f"**Prediction: SURVIVED** (Confidence: {survival_probability:.2%})")
                st.balloons()
            else:
                non_survival_probability = prediction_proba[0][0]
                st.error(f"**Prediction: DID NOT SURVIVE** (Confidence: {non_survival_probability:.2%})")

            # Optional: Display probabilities
            with st.expander("View Prediction Probabilities"):
                st.write(f"Probability of Not Surviving: **{prediction_proba[0][0]:.2%}**")
                st.write(f"Probability of Surviving: **{prediction_proba[0][1]:.2%}**")

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

# --- FOOTER ---
st.markdown("---")
st.markdown("Developed for production deployment on Streamlit Community Cloud.")
