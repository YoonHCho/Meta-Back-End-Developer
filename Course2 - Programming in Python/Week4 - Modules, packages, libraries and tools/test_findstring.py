import findstring
import pytest

def test_ispresent():
    assert findstring.ispresent('Al')

def test_nodigit():
    assert findstring.nodigit("N7")