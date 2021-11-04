# About gits creategoodrepo
This command creates a new repository on the user's local and Github initialized with the Good Repo template. The Good Repo template contains templates for files like contributing.md and codeofconduct.md and file structure to nudge the user towards maintaining the "goodness" of the repo.

# Location of Code
The code that implements this gits functionality is located [here](https://github.com/sak007/GITS/blob/create_repo/code/gits_creategoodrepo.py)

# Code Description
## Functions
1. gits_creategoodrepo(args):
This function takes one mandatory argument as an input. 
This argument is **new repo name** which is the name of the new repo the user wants to create with the good repo template.
The default good repo template is set up as a public github template available here - [Good Repo Template](https://github.com/sak007/goodRepo_template).
It also asks the user to enter the license which he wants in repository from the list of licenses provided. The list includes MIT, Apache and GNU license.

# How to run it? (Small Example)
In a new folder (where there are no other git repos), you can create a new good repo with the following command:

- Create good repo
```
$ gits creategoodrepo <reponame>
```
It will create and initialize a new good repository inside current directory.
