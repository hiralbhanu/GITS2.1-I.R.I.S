# GITS2.1 - I.R.I.S

### GITS2.1 - I.R.I.S (Ideal ReposItory for Software projects)

![GitHub](https://img.shields.io/github/license/jayrshah98/GITS2.1-I.R.I.S)
[![codecov](https://codecov.io/gh/jayrshah98/GITS2.1-I.R.I.S/branch/master/graph/badge.svg?token=I3KHGTAQLU)](https://codecov.io/gh/jayrshah98/GITS2.1-I.R.I.S)
[![DOI](https://zenodo.org/badge/419548765.svg)](https://doi.org/10.5281/zenodo.5630948)
[![GitHub issues](https://img.shields.io/github/issues/jayrshah98/GITS2.1-I.R.I.S)](https://github.com/jayrshah98/GITS2.1-I.R.I.S/issues?q=is%3Aopen+is%3Aissue)
[![GitHub closed issues](https://img.shields.io/github/issues-closed/jayrshah98/GITS2.1-I.R.I.S)](https://github.com/jayrshah98/GITS2.1-I.R.I.S/issues?q=is%3Aissue+is%3Aclosed)
![Lines of code](https://img.shields.io/tokei/lines/github/jayrshah98/GITS2.1-I.R.I.S)
[![Respost - Write comment to new Issue event](https://github.com/jayrshah98/GITS2.1-I.R.I.S/actions/workflows/Respost.yml/badge.svg)](https://github.com/jayrshah98/GITS2.1-I.R.I.S/actions/workflows/Respost.yml)
[![Style Checker and Prettify Code](https://github.com/jayrshah98/GITS2.1-I.R.I.S/actions/workflows//Style_Checker_and_Prettify_Code.yml/badge.svg)](https://github.com/jayrshah98/GITS2.1-I.R.I.S/actions/workflows//Style_Checker_and_Prettify_Code.yml)
![version](https://img.shields.io/badge/version-1.0-blue)
[![Greetings](https://github.com/jayrshah98/GITS2.1-I.R.I.S/actions/workflows/greetings.yml/badge.svg)](https://github.com/jayrshah98/GITS2.1-I.R.I.S/actions/workflows/greetings.yml)
[![Close as a feature](https://github.com/jayrshah98/GITS2.1-I.R.I.S/actions/workflows/close_as_a_feature.yml/badge.svg)](https://github.com/jayrshah98/GITS2.1-I.R.I.S/actions/workflows/close_as_a_feature.yml)
![GitHub contributors](https://img.shields.io/github/contributors/jayrshah98/GITS2.1-I.R.I.S)

Project Video : https://user-images.githubusercontent.com/43321682/140435660-cc44525f-014d-434f-9aec-0fb14e30473f.mp4

# About GITS2.1 - I.R.I.S

"Your repo is your resume. But what is a good looking repo?"

So you want to start a Project on Github. Ever wondered what makes a project repository good?
What makes your project stand apart when collaborating with multiple developers?
What would ensure that your project is well documented and readable to other developers who might try to work on this in the future?

    bash requirements.sh

Worry not. I.R.I.S is here.

I.R.I.S (Ideal ReposItory for Software projects) is a tool which can help developers align their repos as per the standards defined in Software Engineering.

You don't have to worry about missing a test case, or scratch your head on what more files or functionalities are needed to make your repository look good.

2. Currently, this project cannot be run on Windows. You need to make use of WSL to work on this project in Windows

I.R.I.S streamlines your repository as per the Software Engineering Standards, so that your repository has all the necessary Structure to be called a "Good Repo".

I.R.I.S can be thought of a base repo to make sure your project repo fits the bill.

![](https://media.giphy.com/media/Lp8kVSwaSU6V9oATDM/giphy.gif)

# Video for Delta Features

https://user-images.githubusercontent.com/47474447/141851475-3eb31270-a38e-4cd6-bf7f-7b536fd5c10a.mp4

# Installation Setup

## On Linux/MacOS Machines

1. Clone GITS Repo
2. From the root directory run the following command
   ```
   pip install -r requirements.txt
   ```
3. Go to configurations directory and run the following command:

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

   ##

## Installation for Windows

1.  Clone GITS Repo
2.  From the root directory run the following command
    ```
    pip install -r requirements.txt
    ```
3.  Currently, this project cannot be run on Windows. You need to make use of WSL to work on this project in Windows
    although this fix would only work for systems running Windows 10. If you are using another version of Windows, using a
    virtual machine might be preferred.

        Please refer this link to enable WSL : https://docs.microsoft.com/en-us/windows/wsl/install-win10

# How to Contribute?

Please take a look at our CONTRIBUTING.md where we provide instructions on contributing to the repo and help us in enhancing the current video conferencing platforms.

# Documentation

## Functionalities Implemented

0. Use custom commands to work with Git from your command line.
1. Create Default files on startup according to the Stucture.
2. Files will be auto generated with template to give the developers an idea on what needs to be filled. Also, the user is given a choice to add license in his repo from the list provided.
3. Score Calculation to see how much the repo matches with the ideal repo structure.
4. Created commands to show version of Git, count commits, list all custom created commands.
5. Create a custom command to work with Git and make development fun.

## Experimentation setup for Phase 2

(Please check the Projects Tab to see how you can make the project better)

This project aims to ease the developers efforts while working on their project repos. I.R.I.S makes their work easier and saves time by providing all the necessary default files in the required structure to ensure that the developers can focus on making their project better and not worry about the repository.

Here are few motivation points behind coming up with this idea:

- Sometimes when you're working with different files and branches, there are way too many commands which need to be updated in an order. Using a custom command, which can do multiple commands at the same time in a specific order saves time and effort from the developer.
- When working on one of the homeworks for the course, we realised the dearth in project repos which adhere to the standard structure.
- Even if the Idea is good, developers miss out on making a good impression due to the inability to make the projects transferable and easily-usable.

To solve the issues described above, we came up with the project **I.R.I.S** that stands for **Ideal ReposItory for Software projects**.

### Tasks list

You can checkout the Projects Tab in GitHub to see the upcoming tasks for the Project.

## Delta for Phase 2

- [x] Initally , the software could only be implemented on MacOs or Linux Machines. Now we have made sure the commands can be executed on windows and that the software can be executed on windows platform as well.
- [x] Also made an executable to setup the project on command line for ease of use for the user.

## Future Scope

- [ ] Can add more git custom commands to improve quality of life.

### Quantitative measures

Here are some measures that can help compare the results between traditional Git/Github Repo Creation and I.R.I.S

1. The default files created as part of the repo creation.
2. The structure followed for the default files.
3. The default template followed for most files, so that even the most layman developer can ensure that his repo adheres to the Standard.

# Team Members

This repository is made for CSC-510 Software Engineering Course at NC State University for Fall 2021.

<table>
  <tr>
    <td align="center"><a href="https://github.com/ineelshah"><img src="https://avatars.githubusercontent.com/u/40118578?v=4" width="75px;" alt=""/><br /><sub><b>Neel Shah</b></sub></a></td>
    <td align="center"><a href="https://github.com/PvPatel-1001"><img src="https://avatars.githubusercontent.com/u/69849039?v=4" width="75px;" alt=""/><br /><sub><b>Parth Patel</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/ameyatathavadkar"><img src="https://avatars.githubusercontent.com/u/25223347?v=4" width="75px;" alt=""/><br /><sub><b>Ameya Tathavadkar</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/jayrshah98"><img src="https://avatars.githubusercontent.com/u/41386638?s=400&u=b323434b42507c474829a804556d69da82d48c3f&v=4" width="75px;" alt=""/><br /><sub><b>Jay Shah</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/Harshil-Shah99"><img src="https://avatars.githubusercontent.com/u/38115399?v=4" width="75px;" alt=""/><br /><sub><b>Harshil Shah</b></sub></a><br /></td>
  </tr>
</table>
