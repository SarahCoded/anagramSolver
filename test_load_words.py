from main import load_words
import pytest

def test_start():
    assert b'Anagram testing is running'

def test_empty_anagrams():
    assert load_words(0, '') == []
    assert load_words(5, 'aaaaa') == []

def test_error_throw():
    with pytest.raises(TypeError):
        load_words()

def test_anagrams():
    assert load_words(1, ''.join(sorted('a'))) == ['a']
    assert load_words(4, ''.join(sorted('asrt'))) == ['arts', 'rats', 'star', 'tars', 'tsar']
    assert load_words(4, ''.join(sorted('trsa'))) == ['arts', 'rats', 'star', 'tars', 'tsar']
    assert load_words(6, ''.join(sorted('neslit'))) == ['enlist', 'inlets', 'listen', 'silent', 'tinsel']
    assert load_words(8, ''.join(sorted('leassenm'))) == ['lameness', 'maleness', 'nameless', 'salesmen']
