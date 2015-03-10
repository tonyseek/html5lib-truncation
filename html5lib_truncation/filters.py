from __future__ import unicode_literals

from .utils import truncate_sentence


class TruncationFilter(object):
    """The filter of html5lib for truncating documents.

    Just like the other filters defined in :mod:`html5lib.filters`, this
    class's instances could be used with filter-wrapped or raw stream.

    :param source: The source stream.
    :param max_chars: The maximum characters on display after truncated.
    :param break_words: ``True`` if breaking words is allowed. It is defaults
                        to ``False`` which means last broken word will be
                        dropped in truncating.
    :param end: The end characters such as a ellipsis ``"..."``.
    """

    def __init__(self, source, max_chars, break_words=False, end=''):
        self.source = source
        self.max_chars = max_chars
        self.break_words = break_words
        self.end = end

    def __iter__(self):
        return TruncationIterator(self)

    def __getattr__(self, name):
        return getattr(self.source, name)


class TruncationIterator(object):
    """The truncation iterator. It is stateful."""

    def __init__(self, master):
        self.master = master
        self.source = iter(master.source)
        self.total_tags = 0
        self.total_chars = 0

    @property
    def overflow(self):
        return self.total_chars + len(self.master.end) > self.master.max_chars

    @property
    def all_tags_closed(self):
        return self.total_tags <= 0

    def next(self):
        return self.__next__()

    def __iter__(self):
        return self

    def __next__(self):
        token = next(self.source)

        if token['type'] == 'StartTag':
            self.total_tags += 1

        if token['type'] == 'EndTag':
            self.total_tags -= 1

        if token['type'] == 'Characters':
            self.total_chars += len(token['data'])
            if self.overflow:
                token = dict(token)
                overflow_chars = (
                    self.total_chars - self.master.max_chars +
                    len(self.master.end))
                token['data'] = truncate_sentence(
                    text=token['data'],
                    max_chars=len(token['data']) - overflow_chars,
                    break_words=self.master.break_words,
                    padding=len(self.master.end))
                if token['data']:
                    token['data'] += self.master.end

        if self.overflow and self.all_tags_closed:
            raise StopIteration

        return token
