from readability import Readability


def normalize_text(text):
    if len(text) < 100:
        _text = ''
        for x in '012345678901234567890':
            _text += text + ' '
        text = str(_text)
    return text


def reading_score(text):
    text = normalize_text(text)
    r = Readability(text)
    f = r.flesch()
    return f.score


def ease(text):
    text = normalize_text(text)
    r = Readability(text)
    f = r.flesch()
    return f.ease


def grade_levels(text):
    text = normalize_text(text)
    r = Readability(text)
    f = r.flesch()
    return f.grade_levels
