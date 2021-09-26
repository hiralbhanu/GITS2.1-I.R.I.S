
# I.R.I.S
### Ideal ReposItory for Software projects

![GitHub](https://img.shields.io/github/license/sak007/GITS)
[![Build Status](https://travis-ci.com/sak007/GITS.svg?branch=master)](https://travis-ci.com/sak007/GITS)
[![codecov](https://codecov.io/gh/sak007/GITS/branch/master/graph/badge.svg?token=G6RG52G2YO)](https://codecov.io/gh/sak007/GITS/)

[![DOI](https://zenodo.org/badge/295480790.svg)](https://zenodo.org/badge/latestdoi/295480790)

![GitHub issues](https://img.shields.io/github/issues/sak007/GITS)
![GitHub closed issues](https://img.shields.io/github/issues-closed/sak007/GITS)

![Lines of code](https://img.shields.io/tokei/lines/github/sak007/GITS)

# About I.R.I.S
So you want to start a Project. Ever wondered what makes a project repository good?
What makes your project stand apart when collaborating with multiple developers?
Your repo is your resume. But what is a good looking repo?

Worry not. I.R.I.S is here.

I.R.I.S (Ideal ReposItory for Software projects) is a tool which can help developers align their repos as per the standards defined in Software Engineering.

You don't have to worry about whether you missed to add a test case, or scratch your head on what more files/functionalities are needed to make your repository look good.

I.R.I.S streamlines your repository as per the Software Engineering Standards, so that your repository has all the necessary Structure to be called a "Good Repo".

I.R.I.S can be thought of a base repo to make sure your project repo fits the bill.

# Installation for Linux
1. Clone IRIS Repo
2. From the root directory run the following command
    ```
    pip install -r requirements.txt
    ```
3. Go to configurations directory and run the following command

    If you are working on Linux system with a bash terminal or a Windows system using Windows subsystem for linux:
    ```
    bash project_init.sh
    ```
    If you are working on Linux system with a fish terminal:
    ```
    fish project_init.fish
    ```
4. Source the bashrc file
    ```
    source ~/.bashrc
    ```
    
    Note: Open the .bashrc file in User home directory to make sure that the alias command does not have any white spaces in the path. If so, rename the directory to remove the white spaces and re-run the setup.

# Installation for Windows
1. Clone GITS Repo
2. From the root directory run the following command
    ```
    pip install -r requirements.txt
    ```
3. Currently, this project cannot be run on Windows. You need to make use of WSL to work on this project in Windows 
although this fix would only work for systems running Windows 10. If you are using another version of Windows, using a 
virtual machine might be preferred.

    Please refer this link to enable WSL : https://docs.microsoft.com/en-us/windows/wsl/install-win10

# How to Contribute?
Please take a look at our CONTRIBUTING.md where we provide instructions on contributing to the repo and help us in enhancing the current video conferencing platforms.

# Documentation
## Functionalities Implemented
1. [gits profile](https://github.com/harshitpatel96/GITS/blob/master/docs/profile.md)
1. [gits rebase](https://github.com/harshitpatel96/GITS/blob/master/docs/rebase.md)
1. [gits reset](https://github.com/harshitpatel96/GITS/blob/master/docs/reset.md)
1. [gits upstream](https://github.com/harshitpatel96/GITS/blob/master/docs/upstream.md)
1. [gits super reset](https://github.com/harshitpatel96/GITS/blob/master/docs/super_reset.md)
1. [gits commit](https://github.com/harshitpatel96/GITS/blob/master/docs/commit.md)
1. [gits create_branch](https://github.com/harshitpatel96/GITS/blob/master/docs/create_branch.md)
1. [gits logging](https://github.com/harshitpatel96/GITS/blob/master/docs/logging.md)
1. [gits undo](https://github.com/harshitpatel96/GITS/blob/master/docs/undo.md)
1. [gits untrack](https://github.com/harshitpatel96/GITS/blob/master/docs/untrack.md)
1. [gits track](https://github.com/harshitpatel96/GITS/blob/master/docs/track.md)
1. [gits delete](https://github.com/harshitpatel96/GITS/blob/master/docs/delete.md)
1. [gits sync](https://github.com/harshitpatel96/GITS/blob/master/docs/sync.md)
1. [gits switch](https://github.com/harshitpatel96/GITS/blob/master/docs/switch.md)
1. [gits status](https://github.com/harshitpatel96/GITS/blob/master/docs/status.md)
1. [gits branch](https://github.com/harshitpatel96/GITS/blob/master/docs/branch.md)
1. [gits diff](https://github.com/harshitpatel96/GITS/blob/master/docs/diff.md)
1. [gits init](https://github.com/harshitpatel96/GITS/blob/master/docs/init.md)
1. [gits merge](https://github.com/harshitpatel96/GITS/blob/master/docs/merge.md)
1. [gits push](https://github.com/harshitpatel96/GITS/blob/master/docs/push.md)
1. [gits pull](https://github.com/harshitpatel96/GITS/blob/master/docs/pull.md)


## Pydoc implementation
We have tried to write as much documentation as possible. You can use pydoc to go through the documentation. 
For example if you want to go through all the documentation for all files in code/ directory, do the following: 

`cd code`<br>
`python3 -m pydoc -b `

This will open up a browser and you can see all the files. You can click on a particular file to access the 
documentation associated with that file.

This repository is made for CSC 510 Software Engineering Course at NC State University.


## Experimentation setup for phase 3

This project aims to ease the developers efforts while working on their project repos. I.R.I.S makes their work easier and saves time by providing all the necessary default files in the required structure to ensure that the developers can focus on making their project better and not worry about the repository.

Here are few motivation points behind coming up with this idea:
- When working on one of the homeworks for the course, we realised the dearth of project repos which adhere to the standard structure.
- Even if the Idea is good, developers miss out on making a good impression due to the inability to make the projects transferable and easily-usable.

To solve the issues described above, we came up with the project **I.R.I.S** that stands for **Ideal ReposItory for Software projects**.

### Tasks list
You can checkout the Projects Tab in GitHub to see the upcoming tasks for the Project.

### Quantitative measures
Here are some measures that can help compare the results between traditional Git/Github Repo Creation and I.R.I.S
1. The default files created as part of the repo creation.
2. The structure followed for the default files.
3. The default template followed for most files, so that even the most layman developer can ensure that his repo adheres to the Standard.