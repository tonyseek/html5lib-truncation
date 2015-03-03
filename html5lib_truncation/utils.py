from __future__ import unicode_literals


def truncate_sentence(text, max_chars, break_words=False, padding=0):
    """Truncates a sentence.

    :param max_chars: The maximum characters of truncated sentence.
    :param break_words: If you wish to truncate given sentence strictly even
                        if it breaks a word, set it to ``True``. It defaults
                        to ``False`` which means truncating given sentence
                        shorter but never breaking words.
    :param padding: The padding size for truncating. It is usually used to
                    keep spaces for some ending characters such as ``"..."``.
    :return: The truncated sentence.
    """
    if break_words:
        return text[:-abs(max_chars - len(text)) - padding]

    words = []
    for word in text.split():
        predicted_len = (
            sum(map(len, words)) +  # length of words
            len(word) +  # length of next word
            len(words) - 1 +  # length of spaces
            padding)
        if predicted_len >= max_chars:
            break
        words.append(word)
    return ' '.join(words)
