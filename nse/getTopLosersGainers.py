#!/usr/bin/env python3
from nsetools import Nse

def initNse():
    nse = Nse()
    return nse

def getTopLosses(nseInit):
    queryResult = nseInit.get_top_losers()
    # We don't want all fields, only certain fields of intrest.
    Fields = ["symbol", "openPrice", "ltp", "netPrice", "tradedQuantity"]
    print(','.join(map(str,Fields)))
    for listResult in queryResult:
        results = [listResult[x] for x in Fields]
        print(",".join(str(x) for x in results))

def getTopGainers(nseInit):
    queryResult = nseInit.get_top_gainers()
    Fields = ["symbol", "openPrice", "ltp", "netPrice", "tradedQuantity"]
    print("=====================================")
    print("===========Top Gainers===============")
    print(','.join(map(str,Fields)))
    for listResult in queryResult:
        results = [listResult[x] for x in Fields]
        print(",".join(str(x) for x in results))
        

        

if __name__ == '__main__':
    print("This program prints top losers of NSE and top gainers")
    nseInit = initNse()
    getTopLosses(nseInit)
    getTopGainers(nseInit)
