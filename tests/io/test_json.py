
import pytest
import tarski as tsk
from tarski.io import JsonWriter


def test_writer_creation():
    w = JsonWriter("test_output")


def test_empty_language():
    w = JsonWriter("test_output")
    lang = tsk.language()

    w.write(lang)

