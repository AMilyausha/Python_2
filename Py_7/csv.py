from datetime import datetime as dt

def Data_csv(data):
    with open ('log.csv', 'a',  encoding = 'utf-8') as file:
        file.write('{}\n'
                    .format(";".join(data)))
def Data_txt(data):
    with open ('log.txt', 'a',  encoding = 'utf-8') as file:
        file.write('{}\n'
                    .format(";".join(data)))
