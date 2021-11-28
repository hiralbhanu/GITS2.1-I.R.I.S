import gits_logging
import os
import sys
from pathlib import Path


def gits_list_commands(args):
    """
    Function that prints list of custom commands
    to user console
    """
    print("GITS Custom Commands")
    # path = "https://github.com/jayrshah98/GITS2.1-I.R.I.S/tree/master/code"


    path = ""
    if sys.platform[:3] == "win":
        path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir)), "code")

    elif sys.platform == "linux" or sys.platform == "linux2":
        user_home_dir = str(Path.home())
        path = os.path.join(user_home_dir, "code")

    files = os.listdir(path)
    for f in files:
        if "_" in f and "gits" in f:
            f = f.replace('_', ' ')
            f = f[0:-3]
            print(f)
    gits_logging.gits_logger.info("List of Custom Command ")
