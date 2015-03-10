from __future__ import unicode_literals

from html5lib import getTreeWalker
from html5lib_truncation import truncate_html, TruncationFilter


result_a = (
    '<p>Return a truncated copy of the string. The length is specified with '
    'the first parameter which <tt class="docutils literal">\n'
    '<span class=pre></span></tt>\n'
    '<tt class="docutils literal"><span class=pre></span></tt> '
    '<tt class="docutils literal"><span class=pre></span></tt> '
    '<tt class="docutils literal">\n'
    '<span class=pre></span></tt>')
result_b = (
    '<p>Return a truncated copy of the string. The length is specified\n'
    'with the first parameter which defa <tt class="docutils literal">\n'
    '<span class=pre></span></tt>\n'
    '<tt class="docutils literal"><span class=pre></span></tt> '
    '<tt class="docutils literal"><span class=pre></span></tt> '
    '<tt class="docutils literal">\n'
    '<span class=pre></span></tt>')
result_c = (
    '<p>Return a truncated copy of the string. The length is specified with '
    'the first parameter... <tt class="docutils literal">\n'
    '<span class=pre></span></tt>\n'
    '<tt class="docutils literal"><span class=pre></span></tt> '
    '<tt class="docutils literal"><span class=pre></span></tt> '
    '<tt class="docutils literal">\n'
    '<span class=pre></span></tt>')
result_d = (
    '<p>Return a truncated copy of the string. The length is specified\n'
    'with the first parameter whic... <tt class="docutils literal">\n'
    '<span class=pre></span></tt>\n'
    '<tt class="docutils literal"><span class=pre></span></tt> '
    '<tt class="docutils literal"><span class=pre></span></tt> '
    '<tt class="docutils literal">\n'
    '<span class=pre></span></tt>')


def test_truncation(etree):
    assert truncate_html(etree, 98) == result_a
    assert truncate_html(etree, 98, break_words=True) == result_b
    assert truncate_html(etree, 98, end='...') == result_c
    assert truncate_html(etree, 98, end='...', break_words=True) == result_d


def test_truncation_with_string():
    assert truncate_html(result_a, 98) == result_a


def test_iterable(etree):
    walker = getTreeWalker('etree')
    stream = walker(etree)
    stream = TruncationFilter(stream, 98, end='...')

    assert stream.tree is etree

    iterator = iter(stream)
    assert iterator is not stream
    assert iter(iterator) is iterator
