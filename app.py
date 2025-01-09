import streamlit as st
import pandas as pd
import pickle
from scripts.preprocess import load_and_preprocess_data

# Load model
def load_model():
    with open('models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Fungsi untuk membaca file CSV langsung dari folder data
def load_data(file_name):
    file_path = f"data/{file_name}"
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        st.error(f"File '{file_name}' tidak ditemukan di folder 'data/'.")
        return None
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
        return None

# Main Streamlit App
def main():
    st.title("Video Game Sales Analysis")
    
    # Membaca data langsung dari folder data
    file_name = "vgsales.csv"  # Nama file dataset
    data = load_data(file_name)
    
    if data is not None:
        st.write("Dataset Preview:")
        st.dataframe(data.head())  # Menampilkan 5 baris pertama
        
        # Preprocessing data
        data = load_and_preprocess_data(f"data/{file_name}")
        
        # Load model
        model = load_model()
        
        # Prediction
        if st.button("Predict Global Sales"):
            try:
                predictions = model.predict(data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']])
                data['Predicted_Global_Sales'] = predictions
                st.write("Predicted Global Sales:")
                st.dataframe(data[['Name', 'Predicted_Global_Sales']])
            except KeyError as e:
                st.error(f"Kolom yang diperlukan tidak ditemukan dalam dataset: {e}")
            except Exception as e:
                st.error(f"Terjadi kesalahan saat prediksi: {e}")
    
if __name__ == "__main__":
    main()
