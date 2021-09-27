import subprocess
from subprocess import PIPE
import helper
import git
from pathlib import Path

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

        print("Pushing local commits")
        push_commits = ["git", "push"]
        process2 = subprocess.Popen(push_commits, stdout=PIPE, stderr=PIPE)

        stdout, stderr = process2.communicate()
        print(stdout.decode("utf-8"))

        #Creating tests
        #Ensure test folder exists
        Path("test").mkdir(parents=True, exist_ok=True)

        #Get the commited files
        repo = git.Repo("")
        lastcommit = repo.head.commit
        commited_files = None
        for commit in list(repo.iter_commits()):
            if commit==lastcommit:
                commited_files =commit.stats.files
        #If commited files are found, check them one by one and ensure tests exist under /test
        if commited_files:
            for commited_file in commited_files:
                file_path = str(commited_file)
                print("Checking if tests exist for: "+file_path)
                #Ignore files already in the test folder
                if(file_path.startswith("test")):
                    continue
                #Check if its a python type file
                if(file_path.endswith(".py") and not Path("test/"+file_path).is_file()):
                    #Ensure proper test file exists
                    print("Creating test files")
                    Path("test/"+file_path).parent.mkdir(parents=True, exist_ok=True)
                    f = open("test/"+file_path, "w")
                    f.write("#Test for "+file_path)
                    f.close()
                    
                
    except Exception as e:
        print("ERROR: gits push command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False

    return True
