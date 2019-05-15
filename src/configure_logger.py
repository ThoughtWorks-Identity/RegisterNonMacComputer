import logging
import os
import tempfile

def configure_logger(): 
    logger = logging.getLogger('Winzog')
    logger.setLevel(logging.DEBUG)
    tempfile.gettempdir()
    fh = logging.FileHandler(os.path.join(tempfile.gettempdir(), "Winzog.log"))
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger