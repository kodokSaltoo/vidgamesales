import pandas as pd
import streamlit as st
from app.config import RAW_DATA_PATH

class DataLoader:
    @st.cache_data
    def load_data():
        try:
            df = pd.read_csv(RAW_DATA_PATH)
            return df
        except FileNotFoundError:
            st.error("Data file not found. Please check the data directory.")
            return None

    @staticmethod
    def filter_data(df, year_range, platforms):
        if df is None:
            return None
            
        return df[
            (df['Year'].between(year_range[0], year_range[1])) &
            (df['Platform'].isin(platforms))
        ]