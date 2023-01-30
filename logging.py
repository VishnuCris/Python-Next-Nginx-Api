import logging

def configure_logging(file,format='%(asctime)s %(message)s',filemode='w'):
    logging.basicConfig(filename=file,
                       format='%(asctime)s %(message)s',
                       filemode='w')
    print(file)
    # Creating an object
    logger = logging.getLogger()

    # # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)

    return logger