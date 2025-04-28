from logot import Logot, logged

from package import write_important_output


def test_write_important_output(logot: Logot):
    write_important_output()
    logot.assert_logged(logged.debug("loguru output from package.py"))
