# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
message_new = 'абв Ура начались абв каникулы'
lst = ' '.join(list(filter(lambda s: 'абв' not in s, message_new.split())))
print(lst)
