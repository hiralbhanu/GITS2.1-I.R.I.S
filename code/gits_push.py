import subprocess
from subprocess import PIPE
import helper

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
            print("Note: Please commit uncommited changes")
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

    except Exception as e:
        print("ERROR: gits push command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
