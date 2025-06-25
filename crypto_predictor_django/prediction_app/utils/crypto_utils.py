# your_app/utils/crypto_utils.py
import csv
from pathlib import Path
from django.conf import settings

def load_crypto_choices():
    csv_path = Path(settings.BASE_DIR) / 'data' / 'cryptocurrencies.csv'
    choices = []
    
    try:
        with open(csv_path, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                crypto = row['Crypto'].strip().upper()
                currency = row['Currency'].strip().upper()
                pair = f"{crypto}-{currency}"
                choices.append((pair, pair))  # (value, label)
                
        if not choices:
            raise ValueError("CSV file is empty")
            
        return sorted(choices)
        
    except FileNotFoundError:
        # Fallback hardcoded values
        return [
            ('0X0-USD', '0X0-USD'),
            ('3ULL26863-USD', '3ULL26863-USD'),
            ('5IRE-USD', '5IRE-USD'),
            ('A8-USD', 'A8-USD'),
            ('ABYSS-USD', 'ABYSS-USD'),
            ('ACE28674-USD', 'ACE28674-USD')
        ]
    except Exception as e:
        return [('ERROR', f'Error: {str(e)}')]