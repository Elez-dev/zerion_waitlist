import requests
from anticaptcha import ac_get_token
from capmonster import cap_get_token
from fake_useragent import UserAgent
from web3.auto import w3
import random
import string
import threading
import json as js

# Option
capmonster = 1
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
        url = 'https://audience-consumer-api.zootools.co/v3/lists/aOfkJhcpwDHpJVkzO6FB/members'

        if capmonster == True:
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
        res = requests.post(url=url, headers=header, json=json)
        jres = js.loads(res.text)
        if jres['nextStep'] == 'confirmation':
            print('+1 реф\n')


if __name__ == '__main__':
    for i in range(number_of_threads):
        thred = threading.Thread(target=main).start()

