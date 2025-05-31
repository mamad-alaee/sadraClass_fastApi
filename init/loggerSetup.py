from loguru import logger


app_logger = logger

def setup_log_for_project():
    global app_logger
    logger.add("logs/app_info.log",rotation="1 MB",retention="1 week",level="INFO")
    logger.add("logs/app_error.log",rotation="1 MB",retention="1 week",level="ERROR")
    logger.add("logs/app_debug.log",rotation="1 MB",retention="1 week",level="DEBUG")
    logger.add("logs/app_warning.log",rotation="1 MB",retention="1 week",level="WARNING")
    app_logger = logger
    return app_logger