Here, we added a log level specifically to replace print statements.  Because print **always** happens, I felt it should
be a pretty high numeric value, but just shy of CRITICAL.  Then, a global search and replace where the regular expression
for which we were searching was:

  \bprint\(

...and the replacement text was:

  logger.log("PRINT",

Note that there is a space character after the comma, above.
