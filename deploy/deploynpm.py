import os
from deployos import call_in_dir


def _node_in_dir(working_dir, script_file, args):
    call_in_dir(working_dir, "node", [script_file] + args)


def _npm_in_dir(working_dir, args):
    npm_script = os.getenv("NPM_JS_PATH")

    if npm_script:
        _node_in_dir(working_dir, npm_script, args)
    else:
        call_in_dir(working_dir, "npm", args)


def resolve_in_node_modules(working_dir, command):
    node_modules_bin_dir = os.path.join(working_dir, "node_modules", ".bin")
    command_file = os.path.join(node_modules_bin_dir, command)

    if os.name == "nt":
        command_file += ".cmd"

    if os.path.isfile(command_file) and os.access(command_file, os.X_OK):
        return command_file

    return command


def npm_install(working_dir, production = False):
    npm_args = ["install"]

    if production:
        npm_args += ["--production"]

    _npm_in_dir(working_dir, npm_args)
