import subprocess
from subprocess import PIPE
import helper
from github import Github
import os
import datetime
import git
from tabulate import tabulate

readme_present = 0
license_present = 0
citation_present = 0
contribution_present = 0
gitignore_present = 0
coc_present = 0


def issue_checker(info):
    try:
        start_date = datetime.datetime.now() - datetime.timedelta(30)
        gh_token = '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'
        token = os.getenv('GITHUB_TOKEN', gh_token)
        g = Github(token)
        username = info[0][15:]
        print(type(username))
        repo_ = info[1][:-4]
        print(type(repo_))
        link = str(username + "/" + repo_)
        print(link)
        repo = g.get_repo(link)
        print(repo)
        issues = repo.get_issues(state="closed", since=start_date)
        if len(issues.get_page(0)) >= 1:
            return 1
        return 0

    except Exception as e:
        logging.error("Failed", exc_info=True)


def file_checker():
    count = 0
    cwd = os.getcwd()
    g = git.cmd.Git(cwd)
    file_list = []
    file_list = g.ls_files().split("\n")
    for file in file_list:
        if(file == 'README.md'):
            count += 1
            readme_present = 1
        if(file == 'CONTRIBUTING.md'):
            count += 1
            contribution_present = 1
        if(file == 'LICENSE'):
            count += 1
            license_present = 1
        if(file == 'CITATION.md'):
            count += 1
            citation_present = 1
        if(file == 'CODE_OF_CONDUCT.md'):
            count += 1
            coc_present = 1
        if(file == '.gitignore'):
            count += 1
            gitignore_present = 1

    return count


def calculate_grade(score):
    if score >= 95:
        grade = 'A+'
    elif score in range(90, 95):
        grade = 'A'
    elif score in range(85, 90):
        grade = 'B+'
    elif score in range(80, 85):
        grade = 'B'
    elif score in range(75, 80):
        grade = 'C+'
    elif score in range(70, 75):
        grade = 'C'
    elif score in range(65, 70):
        grade = 'D+'
    elif score in range(60, 65):
        grade = 'D'
    else:
        grade = 'F'

    return grade


def gits_push(args):
    """
    This function is used to push local changes to remote branch.
    Usage: gits push
    """
    try:
        untracked_file_check_status = ["git", "status", "--porcelain"]
        process0 = subprocess.Popen(untracked_file_check_status,
                                    stdout=PIPE, stderr=PIPE)

        stdout, stderr = process0.communicate()
        print(stdout.decode("utf-8"))

        if stdout != b'':
            print("Note: Please commit the uncommited changes with path: " + stdout.decode("utf-8"))
            return False

        _ = helper.get_current_branch()

        if args.rebase is not False:
            print("Pulling changes from Upstream source branch and rebasing it")
            pull_rebase = ["git", "pull", "--rebase", "origin", args.rebase]
            process1 = subprocess.Popen(pull_rebase, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process1.communicate()
            print(stdout.decode("utf-8"))

        # Checking whether below files are present in the committed repository
        req_files = ['README.md', 'CONTRIBUTING.md', 'CODE_OF_CONDUCT.md', 'LICENSE', 'CITATION.md', '.gitignore']
        current_files_command = ["git", "ls-tree", "--full-tree", "-r", "--name-only", "HEAD"]
        process3 = subprocess.Popen(current_files_command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process3.communicate()

        committed_files = stdout.decode("utf-8")
        missing_files = []

        for file in req_files:
            if file not in committed_files:
                missing_files.append(file)

        if missing_files:
            print('Warning! ' + ','.join(missing_files) + ' missing in the repository')

        print("Pushing local commits")
        push_commits = ["git", "push"]
        process2 = subprocess.Popen(push_commits, stdout=PIPE, stderr=PIPE)

        stdout, stderr = process2.communicate()
        print(stdout.decode("utf-8"))
        x = helper.get_repo_name()
        issue_score = issue_checker(x)
        file_count = file_checker()

        total_score = ((issue_score + file_count) / 8) * 100

        grade = calculate_grade(total_score)

        print("Repository grade is :", grade)

        table = [['README.md', '1', readme_present], ['CONTRIBUTING.md', '1', contribution_present], ['CODE_OF_CONDUCT.md', '1', coc_present], ['LICENSE.md', '1', license_present], ['CITATION.md', '1', citation_present], ['.gitignore', '1', gitignore_present], ['Issues Closed (Last 30 days)', '1', issue_score], ['TOTAL SCORE', (issue_score + file_count), total_score]]
        print("\n")
        print(tabulate(table, headers=['Item', 'Weight', 'Score']))
        print("\n")

    except Exception as e:
        print("ERROR: gits push command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
