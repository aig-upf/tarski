import errno
import logging
import os
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


libc = ctypes.CDLL(None)
c_stdout = ctypes.c_void_p.in_dll(libc, 'stdout')


@contextmanager
def stdout_redirector(stream):
    # From: https://eli.thegreenplace.net/2015/redirecting-all-kinds-of-stdout-in-python/
    # The original fd stdout points to. Usually 1 on POSIX systems.
    original_stdout_fd = sys.stdout.fileno()

    def _redirect_stdout(to_fd):
        """Redirect stdout to the given file descriptor."""
        # Flush the C-level buffer stdout
        libc.fflush(c_stdout)
        # Flush and close sys.stdout - also closes the file descriptor (fd)
        sys.stdout.close()
        # Make original_stdout_fd point to the same file as to_fd
        os.dup2(to_fd, original_stdout_fd)
        # Create a new sys.stdout that points to the redirected fd
        sys.stdout = io.TextIOWrapper(os.fdopen(original_stdout_fd, 'wb'))

    # Save a copy of the original stdout fd in saved_stdout_fd
    saved_stdout_fd = os.dup(original_stdout_fd)
    tfile = None
    try:
        # Create a temporary file and redirect stdout to it
        tfile = tempfile.TemporaryFile(mode='w+b')
        _redirect_stdout(tfile.fileno())
        # Yield to caller, then redirect stdout back to the saved fd
        yield
        _redirect_stdout(saved_stdout_fd)
        # Copy contents of temporary file to the given stream
        tfile.flush()
        tfile.seek(0, io.SEEK_SET)
        stream.write(tfile.read())
    finally:
        if tfile:
            tfile.close()
        os.close(saved_stdout_fd)
