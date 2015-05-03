import os
from deployos import call


def _get_kudusync_cmd():
    kudusync_cmd = os.getenv("KUDU_SYNC_CMD")

    if not kudusync_cmd:
        raise EnvironmentError("KUDU_SYNC_CMD environment variable not defined.")

    return kudusync_cmd


def _get_manifest_paths():
    next_manifest_path = os.getenv("NEXT_MANIFEST_PATH")
    previous_manifest_path = os.getenv("PREVIOUS_MANIFEST_PATH")

    if not next_manifest_path:
        raise EnvironmentError("NEXT_MANIFEST_PATH environment variable not defined.")

    if not previous_manifest_path:
        previous_manifest_path = next_manifest_path

    return (previous_manifest_path, next_manifest_path)


def _sync(source_dir, target_dir, ignores, with_manifest):
    kudusync_cmd = _get_kudusync_cmd()
    kudusync_args = ["--from", source_dir, "--to", target_dir]

    if ignores:
        ignores_str = ";".join(ignores)
        kudusync_args += ["--ignore", ignores_str]

    if with_manifest:
        previous_manifest_path, next_manifest_path = _get_manifest_paths()
        kudusync_args += ["--previousManifest", previous_manifest_path, "--nextManifest", next_manifest_path]
    else:
        kudusync_args += ["--ignoremanifest"]

    call(kudusync_cmd, kudusync_args)

    return

def sync(source_dir, target_dir, ignores = None):
    _sync(source_dir, target_dir, ignores, False)


def sync_with_manifest(source_dir, target_dir, ignores = None):
    _sync(source_dir, target_dir, ignores, True)
