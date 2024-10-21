import pandas as pd
import re
import os
from datetime import datetime

conversationsDf = pd.DataFrame({
    'date':[],
    'hour':[],
    'sender':[],
    'message':[]
})

os.system('cls')

with open("Conversa do WhatsApp com Cineminha.txt", "r", encoding="utf-8") as file:
    # for txt in a:
    txt = file.read()

    informations = re.findall (r"(\d{2}/\d{2}/\d{4}) (\d{2}:\d{2}) - ([^:]+): (.+)", txt)
    
    for i in informations:
        date, hour, sender, message = i

        newConversation = {
            'date':datetime.strptime(date, '%d/%m/%Y'),
            'hour':datetime.strptime(hour, '%H:%M').time(),
            'sender':sender,
            'message':message
        }        

        conversationsDf = conversationsDf._append(newConversation, ignore_index = True)
        conversationsDf = conversationsDf.reset_index(drop = True)


senders = conversationsDf['sender'].unique().tolist()

conversationsByDate = conversationsDf.groupby(["date", "sender"]).size().reset_index(name="qtty")

print (conversationsByDate)

"""

            
"""