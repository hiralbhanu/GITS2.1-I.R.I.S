"""
To clone from a template repo, we need to run the following commands:

We have created a new template repo already with some pre-defined files that encompass the structure of a good repo.

Cloning from the template can be done with:
gh repo create <repo name> --template sak007/goodRepo_template --public -y

git clone https://github.com/sak007/goodRepo_template.git

git init --template ./goodRepo_template

"""

from subprocess import Popen, PIPE


def gits_creategoodrepo(args):
    return False