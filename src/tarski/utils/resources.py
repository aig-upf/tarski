"""
 A timing utility class inspired in Fast Downward's equivalent.
 See http://www.fast-downward.org/
"""
import contextlib
import os
import sys
import time


def get_mem_usage():
    """ Return the memory usage as reported by psutil, or None, if the platform
    does not support psutil, or """
    try:
        import psutil
    except ImportError:
        return None
    return psutil.Process().memory_info().rss


class Timer:
    def __init__(self):
        self.start_time = time.time()
        self.start_clock = self._clock()
        self.start_mem = get_mem_usage()

    @staticmethod
    def _clock():
        times = os.times()
        return times[0] + times[1]

    def __str__(self):
        rss_in_mb = "-"
        current_in_mb = "-"
        if self.start_mem is not None:
            # self.start_mem is None whenever the underlying platform could not import the psutil module,
            # in which case at the moment we're happy simply not to show memory consumption info.
            current = get_mem_usage()
            current_in_mb = current / (1024*1024)
            rss_in_mb = (current - self.start_mem) / (1024*1024)

        return "[%.2fs CPU, %.2fs wall-clock, diff: %.2fMB, curr:  %.2fMB]" % (
            self._clock() - self.start_clock,
            time.time() - self.start_time, rss_in_mb, current_in_mb)


@contextlib.contextmanager
def timing(text, newline=False):
    timer = Timer()
    if newline:
        print(f"{text}...")
    else:
        print(f"{text}...", end=' ')
    sys.stdout.flush()
    yield
    if newline:
        print(f"{text}: {timer}")
    else:
        print(timer)
    sys.stdout.flush()
