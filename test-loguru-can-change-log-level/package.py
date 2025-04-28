from loguru import logger


def write_important_output() -> None:
    logger.debug("loguru DEBUG message from package.py")
    logger.info("loguru INFO message from package.py")
    logger.warning("loguru WARNING message from package.py")
    logger.error("loguru ERROR message from package.py")
    logger.critical("loguru CRITICAL message from package.py")
    logger.trace("loguru TRACE message from package.py")
    logger.success("loguru SUCCESS message from package.py")

    print("This is important output from package.py")
