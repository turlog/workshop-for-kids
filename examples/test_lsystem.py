from lsystem import generate

def test_no_rules():
    assert generate('A', {}, 1) == 'A'

def test_multiply():
    assert generate('A', {'A': 'AA'}, 8) == 'A'*(2**8)

def test_alternate():
    assert generate('A', {'A': 'AB', 'B': 'AB'}, 4) == 'AB'*8
