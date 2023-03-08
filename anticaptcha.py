from anticaptchaofficial.turnstileproxyless import *


def ac_get_token():
    with open("captcha-key.txt", 'r') as f:
        captcha_key = f.read()
    if '\n' in captcha_key:
        captcha_key = captcha_key[:-1]
    solver = turnstileProxyless()
    solver.set_verbose(1)
    solver.set_key(captcha_key)
    solver.set_website_url("https://form.waitlistpanda.com/go/aOfkJhcpwDHpJVkzO6FB?ref=QXEMoSDtjW1kxzG83LWa")
    solver.set_website_key("0x4AAAAAAABCOgX4x6RvmA0a")
    solver.set_soft_id(0)
    token = solver.solve_and_return_solution()
    if token != 0:
        return token
    else:
        return None
