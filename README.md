# Loguru Feature Tests

The [Loguru GitHub repo](git@github.com:Delgan/loguru.git) and the
[Loguru ReadTheDocs](https://loguru.readthedocs.io/en/stable/overview.html)

This is all one big Git repo, but inside it are several individual tests of various Loguru capabilities. This is all
Python. Each test is a Python project of its own. Each project was created by and is run by `uv`. To run a specific
test, go into that directory, create and activate a virtual environment, and run `main.py`. Here's what that looks like:

- `cd test-loguru-shares-output`
- `uv venv`
- `source .venv/bin/activate`
- `uv sync`
- `python main.py`

If there are instructions specific to a given test, they will be given in a `README.md` in that directory. The
requirements for each test are in their `pyproject.toml` files; and for every one of them, the version of Python is
pinned at 3.8.15, just like SiLOC (at least, at the moment).

Here are the individual "tests" arranged (roughly) from simplest to hardest:

- test-loguru-shares-output
- test-loguru-writes-to-a-file
- test-loguru-can-write-only-to-the-file
- test-loguru-can-split-specific-modules-into-their-own-logs
- test-loguru-can-filter-to-a-specific-activity
- test-loguru-can-change-log-level
- test-loguru-can-log-exceptions
- test-loguru-can-show-stack-trace
- test-loguru-can-be-tested
- test-loguru-works-with-threads
- test-loguru-can-mix-with-std-logging
- test-loguru-can-replace-prints
