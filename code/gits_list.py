import gits_logging
import os


def gits_list_commands(args):
    """
    Function that prints list of custom commands
    to user console
    """
    print("GITS Custom Commands")
    path = "/Users/hiral/Applications/GITS2.1-I.R.I.S/code"
    files = os.listdir(path)
    for f in files:
        if "_" in f and "gits" in f:
            f = f.replace('_', ' ')
            f = f[0:-3]
            print(f)
    gits_logging.gits_logger.info("List of Custom Command ")
