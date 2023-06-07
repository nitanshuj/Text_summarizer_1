import os, sys, logging

# Custom Log

logging_str = "[%(asctime)s:%(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)       # For the Terminal output
    ]
)

logger = logging.getLogger("textsSummarizerLogger")

