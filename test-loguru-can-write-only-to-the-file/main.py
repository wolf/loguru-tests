from loguru import logger

import package


logger.remove()
logger.add("test-loguru-can-write-only-to-the-file-{time}.log")


def main():
    logger.debug("loguru message from main.py")
    print("Hello from test-loguru-can-write-only-to-the-file!")

    package.write_important_output()


if __name__ == "__main__":
    main()
