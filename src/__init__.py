import os
import logging

logging_format = '%(asctime)s - %(levelname)s - %(module)s -  %(message)s'

log_dir = "logs"
log_file = "running_log.log"


os.makedirs(log_dir, exist_ok=True)
os.path.join("logs", "running_log.log")

logging.basicConfig(
    filename=os.path.join(log_dir, log_file),
    level=logging.INFO, 
    format=logging_format)

logger = logging.getLogger(__name__)
