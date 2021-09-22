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
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_template(mock_var1, mock_args):
    """
    Function to test gits creategoodrepo , success case
    """
    test_result = gits_creategoodrepo(mock_args)
    remove_extras(".")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False
