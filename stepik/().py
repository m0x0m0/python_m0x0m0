def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return (text == '')

print(is_correct_bracket(input()))