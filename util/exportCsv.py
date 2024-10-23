import pandas as pd
from pathlib import Path

def exportCsv(df):
    df.to_csv(Path('exports/whatsapp-conversations-export.csv'), index=False)