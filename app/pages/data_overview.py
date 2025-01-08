import streamlit as st
import pandas as pd

def show_data_overview(data):
    st.header("Dataset Overview")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Games", len(data))
    with col2:
        st.metric("Total Platforms", len(data['Platform'].unique()))
    with col3:
        st.metric("Total Publishers", len(data['Publisher'].unique()))
    
    st.subheader("Sample Data")
    st.dataframe(data.head())
    
    st.subheader("Data Statistics")
    st.dataframe(data.describe())