import win32com.client

outlook = win32com.client.Dispatch('outlook.application')
mapi = outlook.GetNamespace("MAPI")

print("Connection esablished to")

for account in mapi.Accounts:
	print(account.DeliveryStore.DisplayName)

print("********************************************")

st=str(input("Enter the subject to search "))
inbox = mapi.GetDefaultFolder(6)

messages = inbox.Items

#messages = messages.Restrict("[Subject] = 'Test'")

for msg in messages:
    if msg.Subject.lower()==st.lower():
        print("From : "+str(msg.Sender))
        print("Body : "+str(msg.body))
        print("_______________________________")
