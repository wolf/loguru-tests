from loguru import logger


def write_important_output() -> None:
    logger.debug("loguru output from package.py")
    logger.log("PRINT", "This is important output from package.py")
