def reverse_words(text: str):
    if '  ' in text: return '  '.join([t[::-1] for t in text.split()])
    elif ' ' in text: return ' '.join([t[::-1] for t in text.split()])
    else: return ''.join([t[::-1] for t in text.split()])
