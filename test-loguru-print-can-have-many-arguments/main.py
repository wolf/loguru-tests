from loguru import logger

import package


logger.level("PRINT", no=48, color="<blue>")
logger.add("test-loguru-print-can-have-many-arguments.log")


def main():
    x = 5
    y = "Hello, world!"
    z = 3.2

    logger.debug("loguru message from main.py")
    logger.log("PRINT", x, y, z)

    package.write_important_output()


if __name__ == "__main__":
    main()
