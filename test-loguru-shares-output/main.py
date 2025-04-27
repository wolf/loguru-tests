from loguru import logger

import package


def main():
    logger.debug("loguru message from main.py")
    print("Hello from test-loguru-shares-output!")

    package.write_important_output()


if __name__ == "__main__":
    main()
