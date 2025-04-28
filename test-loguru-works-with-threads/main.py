import threading
from time import sleep

from loguru import logger

import package


def background_work():
    for _ in range(10):
        sleep(3)
        package.write_important_output()


def main():
    logger.debug("loguru message from main.py")
    print("Hello from test-loguru-shares-output!")

    my_thread = threading.Thread(target=background_work)
    my_thread.start()

    print("This is main() doing something while another thread is running")
    logger.debug("This is loguru, from main(), logging something")
    sleep(15)
    logger.debug("This is loguru, again from main(), logging yet again")

    my_thread.join()

    logger.debug("No more threads (except this one) are running!")


if __name__ == "__main__":
    main()
