import logging

logging.basicConfig(
    filename="logs/etl_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def handle_error(stage, error):
    error_message = f"Error in {stage} stage: {error}"
    logging.error(error_message)
    print(error_message)