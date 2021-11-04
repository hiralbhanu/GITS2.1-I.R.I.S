import argparse
import os
import sys

sys.path.insert(1, os.getcwd())

from gits_version import gits_version
from mock import patch, Mock


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_version_happy_case(mock_var, mock_args):
    """
    Function to test gits version, failure case
    """
    try:
        mocked_pipe = Mock()
        attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
        mocked_pipe.configure_mock(**attrs)
        mock_var.return_value = mocked_pipe

        mock_args = parse_args(mock_args)
        test_result = gits_version(mock_args)
        if type(test_result) == str:
            assert True, "Normal Case"
        else:
            assert False
    except Exception as e:
        print(e)
        print("Failed")
