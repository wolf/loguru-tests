from loguru import logger


def write_important_output() -> None:
    logger.debug("loguru output from package.py")
    print("This is important output from package.py")
