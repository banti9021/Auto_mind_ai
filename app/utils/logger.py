import logging
import os

class Logger:
    """
    A utility class for setting up and managing logging.
    """

    def __init__(self, name: str, log_file: str = "app.log", level: int = logging.INFO):
        """
        Initialize the Logger.

        Args:
            name (str): The name of the logger.
            log_file (str): The file to log messages to. Defaults to 'app.log'.
            level (int): The logging level. Defaults to logging.INFO.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Create file handler
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)

        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        """
        Get the configured logger instance.

        Returns:
            logging.Logger: The logger instance.
        """
        return self.logger

if __name__ == "__main__":
    # Example usage
    logger = Logger(name="ExampleLogger").get_logger()
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")