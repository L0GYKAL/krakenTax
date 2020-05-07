# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 10:54:23 2020

@author: L0GYKAL
"""

import pandas as pd

ledger = pd.read_csv("ledgers.csv")
finalBalances = dict()
fees = dict()

    #collecting the last balance for every currencies
for n in range(ledger["type"].size-1, 0, -1):
    #if ledger["type"][n] not in finalBalances:
    if not pd.isnull(ledger["balance"].iloc[n]) and ledger["asset"][n] not in finalBalances.keys():# and pd.isnull(ledger["balance"].iloc[n]):#ledger["balance"][n] == pd.nan:
        finalBalances[ledger["asset"][n]] = ledger["balance"][n]
    
    
#summing the fees
for n in range(ledger["fee"].size):
    if ledger["asset"][n] not in fees.keys():
        fees[ledger["asset"][n]] = ledger["fee"][n]
    else:
        fees[ledger["asset"][n]] += ledger["fee"][n]

    
    
#printing all the deposits and the withdrawals
for i in range(ledger["type"].size):
    if ledger["type"][i] == "deposit" and not pd.isnull(ledger["balance"].iloc[i]):
        print(str(ledger["amount"][i]) + " of " + str(ledger["asset"][i]) + " deposited at " + str(ledger["time"][i]))
        i += 1
    elif ledger["type"][i] == "withdrawal" and not pd.isnull(ledger["balance"].iloc[i]):
        print(str(ledger["amount"][i]) + " of " + str(ledger["asset"][i]) + " withdrawn at " + str(ledger["time"][i]))
        i+=1    
        
        
        
#printing all the currencies balances
print("The final balances are:\n")
for assetBalance in finalBalances.items():
    if assetBalance[1] != 0:
        print("The final balance of " + str(assetBalance[0]) + " is " + str(assetBalance[1]))
    
print("\n\nYour total  fees are : ")
for asset in fees.items():
    if asset[1] != 0:
        print("The fees in " + str(asset[0]) + " are " + str(asset[1]))

        
    