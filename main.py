import requests
from anticaptcha import ac_get_token
from capmonster import cap_get_token
from fake_useragent import UserAgent
from web3.auto import w3
import random
import string
import threading
import json as js
import time

# Option
capmonster = 0
ref_code = 'aD4PQAWTQPgii1LqyQWw'
number_of_threads = 1
#--------------------


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def main():
    while True:
        account = w3.eth.account.create()
        address = account.address
        url = 'http://audience-consumer-api.zootools.co/v3/lists/aOfkJhcpwDHpJVkzO6FB/members'
        if proxies_list:
            proxies = {
                'http': 'http://' + proxies_list.pop(0)
            }
        else:
            proxies = None
        if capmonster:
            captchaToken = cap_get_token()
        else:
            captchaToken = ac_get_token()

        header = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
            'authorization': 'Bearer',
            'content-length': '575',
            'content-type': 'application/json',
            'origin': 'https://form.waitlistpanda.com',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'user-agent': UserAgent().random
        }
        json = {
            'captchaToken': captchaToken,
            'cryptoAddress': address,
            'email': generate_random_string(15) + '@gmail.com',
            'referral': ref_code
        }
        res = requests.post(url=url, headers=header, json=json, proxies=proxies)
        if res.status_code < 400:
            jres = js.loads(res.text)
            if jres['nextStep'] == 'confirmation':
                print('+1 реф\n')
        else:
            print('Слишком много запросов с одного ip')
            time.sleep(20)
            continue


if __name__ == '__main__':
    with open("proxies.txt", "r") as f:
        proxies_list = [row.strip() for row in f] * 100
    for i in range(number_of_threads):
        threading.Thread(target=main).start()

