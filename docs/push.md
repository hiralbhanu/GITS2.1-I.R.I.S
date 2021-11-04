# About gits push
This function allows user to push local commits to remote branch. While pushing the commit, it checks whether the good repo files are present in the committed repository.

# Location of Code
The code that implements this gits functionality is located [here](https://github.com/harshitpatel96/GITS/blob/master/code/gits_push.py)

# Code Description
## Functions
1. gits_push(args):
This function takes option argument **rebase** as input. When you use **rebase**, gits first pulls the specified remote branch and rebase's current branch on top of the last commit on remote branch. Upon a push to the repository, the repository score will be displayed on the terminal in the form of a grade (A+, A, B+, B, ...). The grade is calculated based on the presence of files like CONTRIBUTING.md, LICENSE, README.md, Number of issues closed in the last 30 days etc.

# How to run it? (Small Example)
You can use this command in two different ways.
1) Simple push
```
gits push
```
2) Using rebase
```
gits push --rebase branchname
```
After using this command, your local branch would be pushed to the remote branch.
