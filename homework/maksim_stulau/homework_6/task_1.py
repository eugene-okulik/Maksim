"""Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову)
в тексте “Etiam incident neque erat, quis molestie enim imperdiet vel.
Integer urna nisl, facilitates vitae semper at, dignissim vitae libero” и
после этого выводит получившийся текст на экран.
Знаки препинания не должны оказаться внутри слова.
Если после слова идет запятая или точка, этот знак препинания должен идти после того же слова,
но уже преобразованного."""

text = "Etiam incident neque erat, quis molestie enim imperdiet vel. \
        Integer urna nisl, facilitates vitae semper at, dignissim vitae libero"

new_text = text.split()
out_text = []
for i in new_text:
    if "," in i:
        i = i.replace(",", "ing,")
    elif "." in i:
        i = i.replace(".", "ing.")
    else:
        i = i + "ing"
    out_text.append(i)

print(out_text)
