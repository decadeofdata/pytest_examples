import pytest

def test_modular(together):
    assert together == "you and me"

def test_modular_complete(complete):
    assert complete == "you and me are happy."