import sys
import logging

def get_logger(
    script_name: str, 
    log_level: int = logging.INFO,
    format: str = "%(asctime)s %(name)s %(levelname)s Line %(lineno)d: %(message)s",
    date_format: str = "%Y-%m-%d %H:%M:%S"
) -> logging:
    
    logger = logging.getLogger(script_name)
    logger.setLevel(log_level)
    
    formatter = logging.Formatter(format, datefmt=date_format)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger