"""
Testy do przykładowego modułu
"""

# pylint: disable=import-outside-toplevel


def test_say_hello():
    """
    Test jednostkowy przykładowej funkcji
    """
    from hello import say_hello
    assert say_hello('Python') == 'Hello Python :)'
