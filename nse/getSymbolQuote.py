#!/usr/bin/env python3
from nsetools import Nse
from pprint import pprint

def initNse():
    nse = Nse()
    return nse

def getValues(nseInit, sticker):
    queryResult = nseInit.get_quote(sticker)
    # We don't want all fields, only certain fields of intrest.
    Fields = ["companyName", "buyPrice1", "buyPrice2", "buyPrice3", "buyPrice4","buyPrice5", "buyQuantity1", "buyQuantity2", "buyQuantity3", "buyQuantity4", "buyQuantity5", "sellPrice1", "sellPrice2", "sellPrice3", "sellPrice4", "sellPrice5", "sellQuantity1", "sellQuantity2", "sellQuantity3", "sellQuantity4", "sellQuantity5", "totalBuyQuantity", "totalSellQuantity", "open", "previousClose", "pricebandlower", "pricebandupper", "quantityTraded"]
    print(','.join(map(str,Fields)))
    results = [queryResult[x] for x in Fields]
    print(",".join(str(x) for x in results))
        

if __name__ == '__main__':
    #Get the symbol from user
    sticker = input("Enter Sticker name: ")
    print(sticker)
    nseInit = initNse()
    # Check weather it is valid code or not
    if nseInit.is_valid_code(sticker):
        getValues(nseInit, sticker)
    else:
        print(sticker + " is not a valid nse code")
