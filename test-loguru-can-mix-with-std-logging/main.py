import logging

import package


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.debug("std logging message from main.py")
    print("Hello from test-loguru-can-mix-with-std-logging!")

    package.write_important_output()


if __name__ == "__main__":
    main()
