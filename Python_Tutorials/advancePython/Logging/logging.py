# Logging is useful to track the error or exception or information. It also helps in debugging.
# Basic Config: This method is used to configure the logging system
# basicConfig(**kwargs)
# 1.) filename: If specifies that a file handler be created using the specified filename.
# 2.) filemode: If filename is specified, filemode opens the file in specified mode (defaults to 'a')
# 3.) level: It sets the root logger level to specified level e.g. Notset, Debug,Info, Warning, Error, Critical.
# by default level is set to Warning.
# a.) info(msg) : This wil log a message with level INFO on this logger.
# b.) warning(msg) : This wil log a message with level WARNING on this logger.
# c.) critical(msg) : This wil log a message with level ERROR on this logger.
# d.) info(msg) : This wil log a message with level CRITICAL on this logger.
# 4.) format: Use the specified format string for the handler.
# 5.) datefmt: Use the specified date time format, as accepted by time.strftime()
# 6.) style: If the format is specified, use 'style' to format string. One of '%', '{', or 'S' (default '%')

# By default the level is set to "Warning" and above so if we move below (i.e. info, debug) it would not be
# printed in console



class Employee:

    def __init__(self):
        print('Employee created')

    def __del__(self):
        print("Destructor called")


def Create_obj():
    print('Making Object...')
    obj = Employee()
    print('function end...')
    return obj


print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')
