#!/usr/bin/env python3
from nsetools import Nse
from pprint import pprint

nse = Nse()
print("Get quote for Infosys")
q = nse.get_quote('infy')
pprint(q)
print("Get all quotations for Index")
print(nse.get_index_list())

print("Top gainers today")
print(nse.get_top_gainers())


