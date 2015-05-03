import os
from deployos import call_in_dir
from deploynpm import resolve_in_node_modules


def _bower_in_dir(working_dir, args):
    bower_cmd = resolve_in_node_modules(working_dir, "bower")
    call_in_dir(working_dir, bower_cmd, args)


def bower_install(working_dir):
    _bower_in_dir(working_dir, ["install"])
