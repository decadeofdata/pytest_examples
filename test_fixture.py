import pytest

@pytest.fixture
def one():
   return 1

def test_we_are(one):
   assert one == 1

def test_we_are_not(one):
   assert one == 2

