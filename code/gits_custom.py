from subprocess import Popen, PIPE, call
import gits_logging
import os


def _create(cmd, path):
    if not os.path.exists(path):
        file1 = open(path, 'w+')
        file1.close()
        EDITOR = os.environ.get('EDITOR', 'vim')
        call([EDITOR, path])
    else:
        print("ERROR: {} command already exists".format(cmd))
        return False


def _update(cmd, path):
    if os.path.exists(path):
        EDITOR = os.environ.get('EDITOR', 'vim')
        call([EDITOR, path])
    else:
        create = input("{} Command does not exists. ".format(cmd) + "Do you want to create {} command?(y/n)".format(cmd))
        if create == 'y' or create == 'Y':
            _create(cmd, path)


def _delete(cmd, path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("ERROR: {} command does not exists".format(cmd))
        return False


def _run(cmd, path):
    file1 = open(path)
    commands = file1.readlines()
    file1.close()
    for cmd in commands:
        print("Running " + cmd)
        process_commands = cmd.split()
        process = Popen(process_commands, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        print(stdout.decode("UTF-8"))


def _reset():
    pass


def _list():
    pass


def gits_custom(args):
    try:
        path = "custom_cmd_" + args.command
        if args.create or args.c:
            _create(args.command, path)
        elif args.update or args.u:
            _update(args.command, path)
        elif args.delete or args.d:
            _delete(args.command, path)
        elif args.reset or args.r:
            _reset()
        elif args.list or args.l:
            _list()
        else:
            _run(args.command, path)
    except Exception as e:
        gits_logging.gits_logger.error(
            "gits custom command caught an exception")
        gits_logging.gits_logger.error("{}".format(str(e)))
        print("ERROR: gits custom command caught an exception")
        print("ERROR: {}".format(str(e)))
        return False
    return True
