import pandas as pd
import re
from datetime import datetime
from pathlib import Path

class ReadData:
    def __init__(self):
        self.df = pd.DataFrame({
            'date':[],
            'hour':[],
            'sender':[],
            'message':[]
        })

        self.dataDir = Path ('data/whatsapp-conversations-export.txt')

    def readData(self):
        with open(self.dataDir, "r", encoding="utf-8") as file:
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

                self.df = self.df._append(newConversation, ignore_index = True)
                self.df = self.df.reset_index(drop = True)
        
        return self.df