# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from asyncio import Task
from unittest import result

with open ("Task5.txt","r") as file:
    Task5 = file.readline()
    list = Task5
        
def compression(my_string: str) -> str:
    count = 1
    result = ''
    for i in range(1,len(my_string)):
        if my_string[i-1] == my_string[i] :
            count+=1
        else:
            result += f'{count}{my_string[i-1]}'
            count = 1
    result += f'{count}{my_string[i]}'
    return result

def decompression (my_string:str)->str:
    num = ""
    result = ""
    for i in my_string:
        if ord('0') <= ord(i) <= ord('9'):
            num += i
        else:
            result += i * int(num)
            num = ""
    return result
  
my_string  = list
print(list)
com = compression (my_string)
print(com)
decom = decompression (com)
print(decom)

with open('Task6.txt', 'w', encoding='utf-8') as file:
    file.write(com)