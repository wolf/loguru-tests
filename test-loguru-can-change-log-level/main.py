import sys

import typer
from loguru import logger

import package


def main(loglevel: str):
    logger.remove()
    logger.add(sys.stdout, level=loglevel)

    logger.debug("loguru DEBUG message from main.py")
    logger.info("loguru INFO message from main.py")
    logger.warning("loguru WARNING message from main.py")
    logger.error("loguru ERROR message from main.py")
    logger.critical("loguru CRITICAL message from main.py")
    logger.trace("loguru TRACE message from main.py")
    logger.success("loguru SUCCESS message from main.py")
    print("Hello from test-loguru-can-change-log-level!")

    package.write_important_output()


if __name__ == "__main__":
    typer.run(main)
