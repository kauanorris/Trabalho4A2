import pandas as pd
import re
from datetime import datetime
from pathlib import Path

def readData():
        df = pd.DataFrame({
            'date':[],
            'hour':[],
            'sender':[],
            'message':[]
        })

        with open(Path ('data/whatsapp-conversations-export.txt'), "r", encoding="utf-8") as file:
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

                df = df._append(newConversation, ignore_index = True)
                df = df.reset_index(drop = True)
        
        return df

readData()

    