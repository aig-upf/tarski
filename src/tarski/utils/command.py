import errno
import logging
import subprocess
from contextlib import contextmanager
import ctypes
import io
import os
import sys
import tempfile


def count_file_lines(filename):  # Might be a bit faster with a call to "wc -l"
    """ Count the number of lines in a given file """
    i = 0
    with open(filename, encoding='utf8') as f:
        for i, _ in enumerate(f, 1):
            pass
    return i


def remove_duplicate_lines(filename):
    """ Removes in-place any duplicate line in the file. Will also reorder the lines as a side-effect """
    subprocess.call(['sort', '-u', '-o', filename, filename])


def read_file(filename):
    """ Read a file, line by line, ignoring end-of-line characters"""
    with open(filename, encoding='utf8') as f:
        for line in f:
            yield line.rstrip('\n')


def execute(command, **kwargs):
    stdout, stderr = kwargs.get("stdout", None), kwargs.get("stderr", None)
    if isinstance(stdout, str):
        stdout = open(stdout, 'w', encoding='utf8')  # pylint: disable=consider-using-with

    if isinstance(stderr, str):
        stderr = open(stderr, 'w', encoding='utf8')  # pylint: disable=consider-using-with

    cwd = kwargs["cwd"] if "cwd" in kwargs else os.getcwd()

    msg = 'Executing "{}" on directory "{}"'.format(' '.join(command), cwd)
    if stdout:
        msg += '. Standard output redirected to "{}"'.format(stdout.name)
    if stderr:
        msg += '. Standard error redirected to "{}"'.format(stderr.name)
    logging.debug(msg)

    retcode = subprocess.call(command, cwd=cwd, stdout=stdout, stderr=stderr)

    if stdout:
        stdout.close()

    if stderr:
        stderr.close()

    if stderr is not None and os.path.getsize(stderr.name) == 0:  # Delete error log if empty
        os.remove(stderr.name)

    return retcode


def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e:
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occured
