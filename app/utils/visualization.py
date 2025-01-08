import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

class Visualizer:
    @staticmethod
    def plot_platform_sales(data):
        fig = plt.figure(figsize=(15, 8))
        sns.barplot(x='Platform', y='Sale_Price', hue='Sale_Area', data=data)
        plt.xticks(rotation=45)
        return fig

    @staticmethod
    def plot_genre_distribution(data):
        fig = plt.figure(figsize=(10, 6))
        data.plot(kind='bar')
        plt.title("Global Sales by Genre")
        plt.xticks(rotation=45)
        return fig