import logging
import os


def get_logger():
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("automation")

    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )

        file_handler = logging.FileHandler(
            "logs/TestAutomation.log"
        )

        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger



