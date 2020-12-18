#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 02:29:17 2020

@author: samkilar
"""
import ssl
import socket
import datetime
import requests
import json

# add new websites to below list
sites = ( 
            'www.google.co.in',
            'in.finance.yahoo.com',
         )

alert_before_days = 5

def ssl_expire_date(target_host):
    '''
    Check target_host cert and return remaining days
    '''
    cert_date_fmt = r'%b %d %H:%M:%S %Y %Z'
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=target_host)
    conn.settimeout(15.0)   # 15 sec connection timeout

    try:
        conn.connect((target_host, 443))
    except Exception as e:
        print('Exception occurred while connecting to {0}:'.format(target_host))
	#print(e)

    remote_cert = conn.getpeercert()
    return datetime.datetime.strptime(remote_cert['notAfter'], cert_date_fmt).date()

def main():
    today = datetime.datetime.utcnow().date()
    for site in sites:
        expire_date = ssl_expire_date(site)
        print(site,expire_date)
        if (expire_date - today ).days < alert_before_days:
            print(site,expire_date,today)
            
if __name__ == '__main__':
    main()
