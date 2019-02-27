
import hashlib
import sys


def int_to_bytes(value):
    return value.to_bytes((value.bit_length() + 7) // 8, 'big', signed=True) or b'\0'


def consistent_hash(iterable):
    h = hashlib.sha256()
    for elem in iterable:
        if isinstance(elem, str):
            h.update(elem.encode())

        elif isinstance(elem, int):
            h.update(int_to_bytes(elem))

        elif isinstance(elem, type):
            h.update(str(elem).encode())

        elif hasattr(elem, "__hash__"):
            h.update(int_to_bytes(object.__hash__(elem)))

        else:
            h.update(str(elem).encode())
    return int(h.hexdigest(), base=16) & (2**sys.hash_info.width - 1)
