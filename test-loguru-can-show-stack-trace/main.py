from loguru import logger

import package


logger.add("include-stack-trace.log", backtrace=True, diagnose=True)


def main():
    logger.debug("loguru message from main.py")
    print("Hello from test-loguru-can-show-stack-trace!")

    package.write_important_output()


if __name__ == "__main__":
    main()
