import requests
import json
import pandas as pd
from constant import token

# This function returns the trades by a particular address

def getTrades():
    url = "https://streaming.bitquery.io/eap"

    payload = json.dumps({
        "query": """query MyQuery {
            Solana {
                DEXTrades(
                    where: {
                        Trade: {Buy: {Account: {Address: {is: "GFTZytvemcb5QamsHCvFRLX3cYwRoabvbk8Mynmg9gWF"}}}},
                        Transaction: {Result: {Success: true}}
                    }
                ) {
                    Trade {
                        Buy {
                            Amount
                            Currency {
                                Name
                                Symbol
                                MintAddress
                            }
                            Price
                        }
                        Dex {
                            ProtocolName
                            ProgramAddress
                            ProtocolFamily
                        }
                        Sell {
                            Currency {
                                MintAddress
                                Name
                                Symbol
                            }
                            Price
                            Amount
                        }
                    }
                    Transaction {
                        Signature
                    }
                }
            }
        }""",
        "variables": "{}"
    })

    headers = {
        'Content-Type': 'application/json',
        'X-API-KEY': 'BQYuTITWanwYGz0YLGdcWSADO74o5RTX',
        'Authorization': token
    }

    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# Currently this function doesn't actually execute a trade but you can checkout libraries and sdks like solana-py for execution part
# Although it stores the trade data in an excel sheet for later reference 
# Documentation for reference - https://michaelhly.com/solana-py/   
 
def executeTrades(trades_data):
    if not trades_data or "data" not in trades_data or "Solana" not in trades_data["data"]:
        print("No trade data found.")
        return

    dex_trades = trades_data["data"]["Solana"]["DEXTrades"]
    
    # Prepare the data for DataFrame
    trade_records = []
    for trade in dex_trades:
        buy_currency = trade['Trade']['Buy']['Currency']
        sell_currency = trade['Trade']['Sell']['Currency']
        dex_info = trade['Trade']['Dex']
        transaction_info = trade['Transaction']

        trade_records.append({
            'Buy Amount': trade['Trade']['Buy']['Amount'],
            'Buy Currency Name': buy_currency['Name'],
            'Buy Currency Symbol': buy_currency['Symbol'],
            'Buy Mint Address': buy_currency['MintAddress'],
            'Buy Price': trade['Trade']['Buy']['Price'],
            'Sell Amount': trade['Trade']['Sell']['Amount'],
            'Sell Currency Name': sell_currency['Name'],
            'Sell Currency Symbol': sell_currency['Symbol'],
            'Sell Mint Address': sell_currency['MintAddress'],
            'Sell Price': trade['Trade']['Sell']['Price'],
            'Dex Protocol Name': dex_info['ProtocolName'],
            'Dex Program Address': dex_info['ProgramAddress'],
            'Dex Protocol Family': dex_info['ProtocolFamily'],
            'Transaction Signature': transaction_info['Signature']
        })

    # Create a DataFrame and save it to an Excel file
    df = pd.DataFrame(trade_records)
    excel_file = 'trades_data.xlsx'
    df.to_excel(excel_file, index=False)
    print(f"Data saved to {excel_file}")

# Fetch trades data
trades_data = getTrades()

# Execute trades to save data to Excel
executeTrades(trades_data)
