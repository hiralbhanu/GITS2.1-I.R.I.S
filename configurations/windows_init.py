import os

macrosFile = open("macros.doskey", "w")
n = macrosFile.write("gits=python \"" + os.path.abspath(os.path.join(os.getcwd(), os.pardir)) + "\code\gits.py\" $*")
macrosFile.close()

gitPath = os.path.join(os.getcwd(), ".gits")
os.mkdir(gitPath)

logPath = os.path.join(gitPath, "logs")
os.mkdir(logPath)

autoRunFile = open("autoRun.bat", "w")
n = autoRunFile.write("reg add \"HKEY_LOCAL_MACHINE\Software\Microsoft\Command Processor\" /v Autorun /d \"doskey /macrofile=" + os.getcwd() + "\macros.doskey\" /f")
autoRunFile.close()
