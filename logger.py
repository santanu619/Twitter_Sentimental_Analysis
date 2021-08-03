import logging

class loggerconfig:

    def logging():
        logging.basicConfig(filename='Twitter.log',level=logging.DEBUG)

if __name__=="__main__":
    logger = loggerconfig()
    logger.logging()