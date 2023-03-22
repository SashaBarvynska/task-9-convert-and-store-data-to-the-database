import logging

log_format = "%(asctime)s - %(levelname)s - "\
             "%(filename)s - %(message)s"
logging.basicConfig(level='DEBUG', format=log_format)
