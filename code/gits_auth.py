import subprocess
import gits_logging
import sys


def gits_authenticator(args):
    try:
        process_commands = ["gh", "auth", "login", "--web"]
        if sys.platform == "linux" or sys.platform == "linux2":
            process = Popen(process_commands, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()
            if(process.returncode == 1):
                return False
        elif sys.platform[:3] == "win":
            process = subprocess.Popen(process_commands, shell=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(process)
            stdout, stderr = process.communicate()
            print(stdout.decode("UTF-8"))
            print(stderr.decode("UTF-8"))
            if(process.returncode == 1):
                return False
    except Exception as e:
        gits_logging.gits_logger.error(
            "gits auth command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits auth command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
