from loguru import logger

import package


logger.add("test-loguru-can-split-specific-modules-into-their-own-logs-{time}.log")
logger.add("package.log", filter="package")


def main():
    logger.debug("loguru message from main.py")
    print("Hello from test-loguru-writes-to-a-file!")

    package.write_important_output()


if __name__ == "__main__":
    main()
