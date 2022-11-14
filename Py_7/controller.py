import view as vw
import csv as log

def Data_view():
    data = vw.get_Data()
    log.Data_csv(data)
    log.Data_txt(data)
    return data
