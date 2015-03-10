from __future__ import unicode_literals

import pytest
import html5lib


html = '''<p>Return a truncated copy of the string. The length is specified
with the first parameter which defaults to <tt class="docutils literal">
<span class="pre">255</span></tt>. If the second parameter is
<tt class="docutils literal"><span class="pre">true</span></tt> the filter
will cut the text at length. Otherwise it will discard the last word. If
the text was in fact truncated it will append an ellipsis sign
(<tt class="docutils literal"><span class="pre">"..."</span></tt>). If you
want a different ellipsis sign than <tt class="docutils literal">
<span class="pre">"..."</span></tt> you can specify it using the third
parameter.</p>'''


@pytest.fixture
def etree():
    return html5lib.parse(html)
