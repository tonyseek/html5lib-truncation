html5lib-truncation
===================

``html5lib-truncation`` is an implementation of html5lib filter, which can
truncate HTML to specific length in display, but never breaks HTML tags.

There is a shortcut function, the simplest way to use it::

    >>> from html5lib_truncation import truncate_html
    >>>
    >>> html = u'<p>A <a href="#">very very long link</a></p>'
    >>> truncate_html(html, 8)
    u'<p>A <a href=#>very</a>'
    >>> truncate_html(html, 8, break_words=True)
    u'<p>A <a href=#>very ve</a>'
    >>> truncate_html(html, 20, end='...')
    u'<p>A <a href=#>very very...</a>'
    >>> truncate_html(html, 20, end='...', break_words=True)
    u'<p>A <a href=#>very very lon...</a>'


Installation
------------

::

    pip install html5lib-truncation

Don't forget to put it into your ``requirements.txt`` or ``setup.py``.


API Overview
------------

The core API of html5lib-truncation is the filter::

    import html5lib
    from html5lib_truncation import TruncationFilter

    etree = html5lib.parse(u'<p>A <a href="#">very very long link</a></p>')
    walker = html5lib.getTreeWalker('etree')

    stream = walker(etree)
    stream = TruncationFilter(stream, 20, end='...', break_words=True)

    serializer = html5lib.serializer.HTMLSerializer()
    serialized = serializer.serialize(stream)

    print(u''.join(serialized).strip())

The output is ``<p>A <a href=#>very very lon...</a>``.


Issues
------

If you want to report bugs or other issues, please create issues on
`GitHub Issues <https://github.com/tonyseek/html5lib-truncation/issues>`_.


Contributes
-----------

You can send a pull reueqst on
`GitHub <https://github.com/tonyseek/html5lib-truncation/pulls>`_.
