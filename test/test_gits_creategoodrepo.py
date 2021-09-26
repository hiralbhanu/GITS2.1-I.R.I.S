import argparse
import sys
import os
import shutil

sys.path.insert(1, os.getcwd())

from gits_creategoodrepo import gits_creategoodrepo
from mock import patch

def remove_extras(path):
    files = os.listdir(path)
    for file in files:
        if "py" in file:
            continue
        try:
            shutil.rmtree(file)
        except:
            os.remove(file)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(barre=None, template="test_template", amend=True))
@patch("subprocess.Popen", return_value="0")
def test_gits_creategoodrepo(mock_var1, mock_args):
    """
    Function to test gits creategoodrepo , success case i.e subprocess returns 0 on successful execution of command
    """
    test_result = gits_creategoodrepo(mock_args)
    remove_extras(".")
    if test_result==0:
        assert True, "Normal Case"
    else:
        assert False

@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(barre=None, template="test_template", amend=True))
# @patch("subprocess.Popen", return_value="1")
def test_gits_creategoodrepo(mock_var1):
    """
    Function to test gits creategoodrepo , failure case i.e subprocess will return 1 on command failing to execute
    """
    test_result = gits_creategoodrepo(repo_name = "testrepo")
    remove_extras(".")
    if test_result==0:
        assert True, "Normal Case"
    else:
        assert False