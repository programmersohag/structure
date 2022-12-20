# importing module
import logging


class Logger:
    # Create and configure logger
    logging.basicConfig(filename="loggerfile.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    def logDebug(message):
        # Creating an object
        logger = logging.getLogger()
        # Setting the threshold of logger to DEBUG
        logger.setLevel(logging.DEBUG)

        logger.debug(message)
        return logger
