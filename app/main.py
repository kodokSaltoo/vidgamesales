import streamlit as st
from app.config import APP_SETTINGS
from app.utils.data_loader import DataLoader
from app.pages import data_overview, sales_analysis, prediction_model

def main():
    # Set page config
    st.set_page_config(**APP_SETTINGS)
    
    # Load data
    data = DataLoader.load_data()
    if data is None:
        return
        
    # Sidebar filters
    st.sidebar.header("Filters")
    
    years = data['Year'].dropna().astype(int)
    year_range = st.sidebar.slider(
        "Select Year Range",
        min_value=int(years.min()),
        max_value=int(years.max()),
        value=(int(years.min()), int(years.max()))
    )
    
    platforms = st.sidebar.multiselect(
        "Select Platforms",
        options=sorted(data['Platform'].unique()),
        default=sorted(data['Platform'].unique())[:5]
    )
    
    # Filter data
    filtered_data = DataLoader.filter_data(data, year_range, platforms)
    
    # Show pages
    tabs = st.tabs(["Data Overview", "Sales Analysis", "Prediction Model"])
    
    with tabs[0]:
        data_overview.show_data_overview(filtered_data)
    with tabs[1]:
        sales_analysis.show_sales_analysis(filtered_data)
    with tabs[2]:
        prediction_model.show_prediction_model(filtered_data)

if __name__ == "__main__":
    main()