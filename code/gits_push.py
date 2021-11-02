import subprocess
from subprocess import PIPE
import helper
from tabulate import tabulate

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
                     
        grade = calculate_grade(total_score)

        print("Repository grade is :", grade)

        table = [['README.md', '1', readme_present],
                    ['CONTRIBUTING.md', '1', contribution_present], ['CODE_OF_CONDUCT.md', '1', coc_present],
                    ['LICENSE.md', '1', license_present], ['CITATION.md', '1', citation_present],
                    ['.gitignore', '1', gitignore_present], ['Issues Closed (Last 30 days)', '1', issue_score],
                    ['TOTAL SCORE', (issue_score + file_count), total_score]
                    ]
        print("\n")
        print(tabulate(table, headers = ['Item', 'Weight', 'Score']))
        print("\n")


    except Exception as e:
        print("ERROR: gits push command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
