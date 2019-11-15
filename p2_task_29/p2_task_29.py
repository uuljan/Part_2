def text():

    text_1 = 'Как пользоваться? Проверить текст на орфографические ошибки. '
    text_2 = "".join(c for c in text_1 if c not in ('?','.',':', '""'))
    print(text_2)
text()