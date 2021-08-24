path = r".\att\Report.xlsx"

#imports
import openpyxl as op

#modules
def accept_data():
    l=[]
    date=input("Enter the date ")
    proc=input("Enter the Process ")
    thr=input("Enter the Threshold ")
    cor=input("Enter the cordinator ")

    l.append(date)
    l.append(proc)
    l.append(thr)
    l.append(cor)

    return l

def append():
    wb = op.load_workbook(path)
    ws = wb['Sheet1']
    ws.append(accept_data())
    wb.save(r".\att\Updated_Report.xlsx")
    wb.close()

append()