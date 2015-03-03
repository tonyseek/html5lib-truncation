from __future__ import unicode_literals

from html5lib_truncation.utils import truncate_sentence


def test_truncate_sentence():
    s = 'Three Rings for the Elven-kings under the sky'

    assert truncate_sentence(s, 18) == 'Three Rings for'
    assert truncate_sentence(s, 18, break_words=True) == 'Three Rings for th'
    assert truncate_sentence(s, 18, break_words=False) == 'Three Rings for'

    assert truncate_sentence(s, 18, break_words=True, padding=9) == 'Three Rin'
    assert truncate_sentence(s, 18, break_words=False, padding=9) == 'Three'
