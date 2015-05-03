import os
from deployos import call_in_dir
from deploynpm import resolve_in_node_modules


def _gulp_in_dir(working_dir, args):
    gulp_cmd = resolve_in_node_modules(working_dir, "gulp")
    call_in_dir(working_dir, gulp_cmd, args)


def gulp(working_dir, *args):
    _gulp_in_dir(working_dir, list(args))
