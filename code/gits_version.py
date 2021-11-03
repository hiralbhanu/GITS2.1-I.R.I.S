import subprocess
from subprocess import PIPE
import gits_logging
import helper

def gits_version(args):
    try:
        ver = list()
        ver.append("git")
        ver.append("--version")
        process1 = subprocess.Popen(ver, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process1.communicate()
        print(stdout.decode("UTF-8"))

    except Exception as e:
        print("ERROR: gits version command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
