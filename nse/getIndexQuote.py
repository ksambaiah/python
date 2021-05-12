#!/usr/bin/env python3
from nsetools import Nse
from pprint import pprint

def initNse():
    nse = Nse()
    return nse

def getIndexQuote(nseInit):
    # We don't want all fields, only certain fields of intrest.
    print("========= Index Related information =========")
    fields = ["name,"lastPrice","change","pChange"]
    print(','.join(map(str,fields)))
    indexes = ['NIFTY 50', 'NIFTY NEXT 50', 'NIFTY BANK', 'NIFTY PHARMA', 'NIFTY IT', 'NIFTY SMLCAP 100']
    for index in indexes:
        queryResult = nseInit.get_index_quote(index)
        print(",".join(str(queryResult[x]) for x in fields))
        

if __name__ == '__main__':
    #We get Index (only limited) quotes
    nseInit = initNse()
    getIndexQuote(nseInit)
