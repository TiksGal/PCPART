import logging
from database import Database
from pc_builder import PCBuilder

if __name__ == "__main__":
    # Create a logger for the main script
    logger = logging.getLogger("MainLogger")
    logger.setLevel(logging.INFO)

    # Configure a console handler for the main script logger
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    # Configure a file handler for the main script logger
    file_handler = logging.FileHandler("app_log.txt")  # Change "app_log.txt" to the desired file name
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    # Add the console and file handlers to the main script logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    # Create the Database object and pass the main script logger to it
    db = Database(logger)

    # Create the PCBuilder object and pass the Database object to it
    app = PCBuilder(db)

    # Start the PCBuilder application
    app.start()

