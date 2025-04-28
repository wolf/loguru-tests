import sys
from typing import Optional

import typer
from loguru import logger
from typing_extensions import Annotated

import package


def is_loggable_task(record, key: str) -> bool:
    # too long to be a lambda
    return "task" in record["extra"] and record["extra"]["task"] == key


def main(
    log_filter_key: Annotated[
        Optional[str],
        typer.Option()
    ] = None
):
    if log_filter_key is not None:
        logger.remove()
        logger.add(sys.stdout, filter=lambda record: is_loggable_task(record, log_filter_key))

    logger.debug("loguru message from main.py")
    print("Hello from test-loguru-shares-output!")

    package.write_important_output()


if __name__ == "__main__":
    typer.run(main)
