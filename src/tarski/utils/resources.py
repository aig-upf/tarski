"""
 A timing utility class inspired in Fast Downward's equivalent.
 See http://www.fast-downward.org/
"""
import contextlib
import os
import sys
import time
import psutil


class Timer(object):
    def __init__(self):
        self.start_time = time.time()
        self.start_clock = self._clock()
        self.start_mem = psutil.Process().memory_info().rss

    @staticmethod
    def _clock():
        times = os.times()
        return times[0] + times[1]

    def __str__(self):
        rss_in_mb = (psutil.Process().memory_info().rss - self.start_mem) / (1024*1024)
        return "[%.3fs CPU, %.3fs wall-clock, %.3fs MB]" % (
            self._clock() - self.start_clock,
            time.time() - self.start_time, rss_in_mb)


@contextlib.contextmanager
def timing(text, block=False):
    timer = Timer()
    if block:
        print(f"{text}...")
    else:
        print(f"{text}...", end=' ')
    sys.stdout.flush()
    yield
    if block:
        print(f"{text}: {timer}")
    else:
        print(timer)
    sys.stdout.flush()
