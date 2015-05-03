import os
import subprocess


def _get_exec_extensions():
    if os.name == "nt":
        return os.getenv("PATHEXT").split(os.pathsep)
    else:
        return [""]


def _resolve_path(command):
    extensions = _get_exec_extensions()

    def is_exec(filenanme):
        return os.path.isfile(filenanme) and os.access(filenanme, os.X_OK)

    fpath, fname = os.path.split(command)

    if fpath:
        if is_exec(command):
            return command
    else:
        resolve_dirs = os.getenv("PATH").split(os.pathsep)

        for resolve_dir in resolve_dirs:
            dir_and_command = os.path.join(resolve_dir, command)

            for extension in extensions:
                command_path = dir_and_command + extension
                if is_exec(command_path):
                    return command_path

    return None


def call(command, args):
    command_path = _resolve_path(command)

    if not command_path:
        command_path = command

    subprocess.check_call([command_path] + args)


def call_in_dir(working_dir, command, args):
    original_dir = os.getcwd()
    os.chdir(working_dir)

    try:
        call(command, args)

    finally:
        os.chdir(original_dir)
