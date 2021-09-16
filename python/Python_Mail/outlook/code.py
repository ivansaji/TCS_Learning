#imports
import win32com.client
import os,time
import openpyxl as op
from datetime import date

#Establishing Connections
outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")
print("Connection esablished to")
path = r"Z:\share\final\att"
for account in mapi.Accounts:
    print(account.DeliveryStore.DisplayName)

print("********************************************")

#Declaring Different Folders
inbox = mapi.GetDefaultFolder(6)

#modules

def accept_data():
    l=[]
    dat=date.today()
    proc=input("Enter the Process ")
    thr=input("Enter the Threshold ")
    cor=input("Enter the cordinator ")

    l.append(dat)
    l.append(proc)
    l.append(thr)
    l.append(cor)

    return l

def append(attachment):
    #attachment is the name of downloaded Report file
    wb = op.load_workbook(os.path.join(path, str(attachment)))
    ws = wb['Sheet1']
    ws.append(accept_data())
    wb.save(os.path.join(path, "Updated_Report.xlsx"))
    wb.close()

def search(st):
    #search code
    st=str(st)
    messages = inbox.Items
    for msg in messages:
        if(msg.UnRead==True):
            #print only unread messages
            if(msg.Subject.lower()==st.lower()):
                print("From : "+str(msg.Sender))
                print("Body : "+str(msg.body))

                if(msg.Attachments.count>0):
                    #fetching attachments
                    attachments = msg.Attachments
                    # return the first item in attachments
                    attachment = attachments.Item(1)
                    attachment.SaveAsFile(os.path.join(path, str(attachment)))
                    print("Report Downloaded")
          
                msg.UnRead=False
                print("_______________________________")
                append(attachment)

                

        else:
            msg.UnRead=False
        

#main code
st="Alert"
while(1):
    search(st)
    time.sleep(5)