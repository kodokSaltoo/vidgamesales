import os
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = os.path.join(BASE_DIR, 'data')
MODELS_DIR = os.path.join(BASE_DIR, 'models')

# Data paths
RAW_DATA_PATH = os.path.join(DATA_DIR, 'raw', 'vgsales.csv')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Model paths
SAVED_MODELS_DIR = os.path.join(MODELS_DIR, 'saved_models')

# App settings
APP_SETTINGS = {
    'title': 'Video Games Sales Analysis',
    'icon': '🎮',
    'layout': 'wide'
}