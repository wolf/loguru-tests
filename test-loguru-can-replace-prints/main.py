from loguru import logger

import package


logger.level("PRINT", no=48, color="<blue>")
logger.add("test-loguru-can-replace-prints.log")


def main():
    logger.debug("loguru message from main.py")
    logger.log("PRINT", "Hello from test-loguru-can-replace-prints!")

    package.write_important_output()


if __name__ == "__main__":
    main()
