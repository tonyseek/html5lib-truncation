from __future__ import unicode_literals

import html5lib

from .filters import TruncationFilter


def truncate_html(html, *args, **kwargs):
    """Truncates HTML string.

    :param html: The HTML string or parsed element tree (with
                 :func:`html5lib.parse`).
    :param kwargs: Similar with :class:`.filters.TruncationFilter`.

    :return: The truncated HTML string.
    """
    if hasattr(html, 'getchildren'):
        etree = html
    else:
        etree = html5lib.parse(html)

    walker = html5lib.getTreeWalker('etree')

    stream = walker(etree)
    stream = TruncationFilter(stream, *args, **kwargs)

    serializer = html5lib.serializer.HTMLSerializer()
    serialized = serializer.serialize(stream)

    return u''.join(serialized).strip()
