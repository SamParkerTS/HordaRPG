import logging
import os


class Logger:

    def __init__(self, paths):

        log_file = os.path.join(paths.logs_dir, "app.log")

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                logging.FileHandler(log_file, encoding="utf-8"),
                logging.StreamHandler()
            ]
        )

        self.logger = logging.getLogger("HordaRPG")

        self.logger.info("Logger iniciado.")

    def get_logger(self):
        return self.logger