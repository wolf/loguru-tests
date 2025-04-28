In this example, you're not going to run `main.py`.  You're going to run the tests.  And tests aren't packages, so importing
the function under test is hard.  You have to specify the `PYTHONPATH`.  Here's what to say:

  `PYTHONPATH=. pytest`
