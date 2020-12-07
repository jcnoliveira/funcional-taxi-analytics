import logging


def log():
    # create logger
    logger = logging.getLogger('dataimport')
    logger.setLevel(logging.DEBUG)
    logging.basicConfig(filename='dataimport.log', filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
    return logger