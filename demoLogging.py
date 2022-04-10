import logging
import os

logging.basicConfig(
    filename=os.path.join("logs", "appLogs.log"),
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
    filemode="a"
    
)
logger = logging.getLogger(__name__)

logger.info("Test logger")