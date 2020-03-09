# Logger
import logging,inspect
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#logs folder should be on the local
#this will create new directory for logs
if not os.path.exists("../logs"):
    os.makedirs("../logs")
# Create a file handler
handler = logging.FileHandler('../logs/application.log')
# Create a logging format
func = inspect.currentframe().f_back.f_code
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# Add the handlers to the logger
logger.addHandler(handler)