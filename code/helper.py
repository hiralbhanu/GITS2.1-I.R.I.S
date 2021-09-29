#!/usr/bin/python3

from subprocess import PIPE
import subprocess

import git
from pathlib import Path


def get_current_branch():
    """
    This function returns current checked out branch.
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("rev-parse")
        subprocess_command.append("--abbrev-ref")
        subprocess_command.append("HEAD")
        process = subprocess.Popen(
            subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        branch = stdout.decode('UTF-8')
        return branch.rstrip()
    except:
        print("Error occured while getting current branch name!")
        return None


def get_trunk_branch_name():
    """
    This function returns the name of the trunk branch for the project
    """
    try:
        subprocess_command = list()
        subprocess_command.append("git")
        subprocess_command.append("branch")
        process = subprocess.Popen(
            subprocess_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        all_branches = stdout.decode('UTF-8')
        list_of_branch_names = all_branches.split()
        list_of_branch_names.remove('*')
        if "master" in list_of_branch_names:
            return "master"
        elif "main" in list_of_branch_names:
            return "main"
        else:
            print("h")
            return list_of_branch_names[0]

    except:
        print("error occured while getting trunk branch name!")
        return None


def get_push_createtests():
    # Creating tests
    # Get the commited files
    repo = False
    try:
        repo = git.Repo("")
    except Exception:
        print("Couldn't find valid repo. Skipping tests creation...")
        pass
    if repo:
        lastcommit = repo.head.commit
        commited_files = None
        for commit in list(repo.iter_commits()):
            if commit == lastcommit:
                commited_files = commit.stats.files
        # If commited files are found, check them one by one and ensure tests exist under /test
        if commited_files:
            for commited_file in commited_files:
                file_path = str(commited_file)
                print("Checking if tests exist for: " + file_path)
                # Ignore files already in the test folder
                if(file_path.startswith("test")):
                    continue
                # Check if its a python type file
                test_file_path = ""

                tokenized_path = str(file_path).split("/")
                if(len(tokenized_path) > 1):
                    test_file_path = Path("test/" + "/".join(tokenized_path[:-1]) + "/test_" + tokenized_path[-1])
                else:
                    test_file_path = Path("test/test_" + file_path)
                if(file_path.endswith(".py") and not test_file_path.is_file()):
                    # Ensure proper test file exists
                    print("Creating test files")
                    test_file_path.parent.mkdir(parents=True, exist_ok=True)
                    f = open(test_file_path, "w")
                    f.write("#Test for " + file_path)
                    f.close()
