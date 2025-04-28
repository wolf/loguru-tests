from loguru import logger


this_specific_task = logger.bind(task="important_task")


def write_important_output() -> None:
    this_specific_task.debug("loguru output from package.py")
    print("This is important output from package.py")
