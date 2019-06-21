import logging
import os
import subprocess


def count_file_lines(filename):  # Might be a bit faster with a call to "wc -l"
    """ Count the number of lines in a given file """
    i = 0
    with open(filename) as f:
        for i, _ in enumerate(f, 1):
            pass
    return i


def remove_duplicate_lines(filename):
    """ Removes in-place any duplicate line in the file. Will also reorder the lines as a side-effect """
    subprocess.call(['sort', '-u', '-o', filename, filename])


def read_file(filename):
    """ Read a file, line by line, ignoring end-of-line characters"""
    with open(filename) as f:
        for line in f:
            yield line.rstrip('\n')


def execute(command, **kwargs):
    stdout, stderr = kwargs.get("stdout", None), kwargs.get("stderr", None)
    if isinstance(stdout, str):
        stdout = open(stdout, 'w')

    if isinstance(stderr, str):
        stderr = open(stderr, 'w')

    cwd = kwargs["cwd"] if "cwd" in kwargs else os.getcwd()

    msg = 'Executing "{}" on directory "{}"'.format(' '.join(command), cwd)
    if stdout:
        msg += '. Standard output redirected to "{}"'.format(stdout.name)
    if stderr:
        msg += '. Standard error redirected to "{}"'.format(stderr.name)
    logging.info(msg)

    retcode = subprocess.call(command, cwd=cwd, stdout=stdout, stderr=stderr)

    if stdout:
        stdout.close()

    if stderr:
        stderr.close()

    if stderr is not None and os.path.getsize(stderr.name) == 0:  # Delete error log if empty
        os.remove(stderr.name)

    return retcode
