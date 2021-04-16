import logging

logging.basicConfig(level = logging.DEBUG, filename = "simple/test.log")

# 5 levels:
# Debug
# info
# warning
# error
# critical

# the first value in basicConfig is the level
# the secont value is the output file (you have to make sure this exists)

logging.debug('this is a debug message')

# this will output (with the level of debug) 'this is a debug message'
# note this will ONLY output if you say that logging.DEBUG is enabled (this lets debug and anything more 'important' be output)
