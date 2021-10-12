import win32com.client as client

# startup outlook instance
outlook = client.Dispatch('Outlook.Application')

# get namespace so that we can access folders
namespace = outlook.GetNameSpace('MAPI')

# get the inbox folder, specifically
inbox = namespace.Folders['Inbox'] 

