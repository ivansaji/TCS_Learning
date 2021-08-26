#imports
import win32com.client
import os,time

#pip install pywin32

#update the attachment folder("att") path here
path = r"Z:\share\Tasks\Python2\Task 1 - Search and Download Report\att"

#Establishing Connections
outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")
print("Connection esablished to")

for account in mapi.Accounts:
    print(account.DeliveryStore.DisplayName)

print("********************************************\nWaiting for incoming Reports")

#Declaring Different Folders
inbox = mapi.GetDefaultFolder(6)

#modules

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

                

        else:
            msg.UnRead=False
        

#main code
st="Alert"
while(1):
    search(st)
    time.sleep(5)