import logging
from error_handler import handle_error

def extract_data():
    try:
        # Simulate data extraction
        raise ValueError("Data source not reachable")
    except Exception as e:
        handle_error("Extract", e)

def transform_data():
    try:
        # Simulate transformation
        data = 1 / 0  # Division by zero error
    except Exception as e:
        handle_error("Transform", e)

def load_data():
    try:
        # Simulate data load
        print("Data loaded successfully")
    except Exception as e:
        handle_error("Load", e)

def main():
    extract_data()
    transform_data()
    load_data()

if __name__ == "__main__":
    main()