from loguru import logger


@logger.catch
def write_important_output() -> float:
    answer = 1 / 0
    logger.debug("loguru output from package.py")
    print("This is important output from package.py")
    return answer
