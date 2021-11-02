"""
To clone from a template repo, we need to run the following commands:

We have created a new template repo already with some pre-defined files that encompass the structure of a good repo.

Cloning from the template can be done with:
gh repo create <repo name> --template sak007/goodRepo_template --public -y

git clone https://github.com/sak007/goodRepo_template.git

git init --template ./goodRepo_template

"""

from subprocess import Popen, PIPE
import gits_logging


def gits_creategoodrepo(args):
    try:
        process_commands = ["git", "init" ,"create", args.repo_name, "--template", "sak007/goodRepo_template", "--public", "-y"]
        process = Popen(process_commands, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        if(process.returncode == 1):
            return False
    except Exception as e:
        gits_logging.gits_logger.error(
            "gits creategoodrepo command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits creategoodrepo command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
