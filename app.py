import streamlit as st
import pandas as pd
import pickle
from scripts.preprocess import load_and_preprocess_data

# Load model
def load_model():
    with open('models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Main Streamlit App
def main():
    st.title("Video Game Sales Analysis")
    st.sidebar.title("Navigation")
    
    # Upload data
    uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write("Dataset Preview:")
        st.dataframe(data.head())
        
        # Preprocessing
        data = load_and_preprocess_data(uploaded_file)
        
        # Prediction
        model = load_model()
        if st.button("Predict Global Sales"):
            predictions = model.predict(data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']])
            data['Predicted_Global_Sales'] = predictions
            st.write("Predicted Global Sales:")
            st.dataframe(data[['Name', 'Predicted_Global_Sales']])
    
if __name__ == "__main__":
    main()
