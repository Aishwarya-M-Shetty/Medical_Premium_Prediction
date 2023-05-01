import logging
from datetime import datetime
import os

LOG_DIR="Insurance_log"

current_time_stamp=f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
LOG_FILE_NAME=f"log_{current_time_stamp}.log"
os.makedirs(LOG_DIR,exist_ok=True)
LOG_FILE_PATH=os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,filemode="w",format='[%(asctime)s] %(name)s - %(levelname)s -%(message)s',
                    #level=logging.INFO,
                    level=logging.DEBUG
                    )
