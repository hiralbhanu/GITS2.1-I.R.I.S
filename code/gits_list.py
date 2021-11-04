import gits_logging
import os


def gits_list_commands(args):
    """
    Function that prints list of custom commands
    to user console
    """
    print("GITS Custom Commands")
    path = "https://github.com/hiralbhanu/GITS2.1-I.R.I.S/tree/master/code"
    files = os.listdir(path)
    for f in files:
        if "_" in f and "gits" in f:
            f = f.replace('_', ' ')
            f = f[0:-3]
            print(f)
    gits_logging.gits_logger.info("List of Custom Command ")
