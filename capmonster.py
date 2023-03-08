from capmonster_python.turnstile import TurnstileTask


def cap_get_token():
    with open("captcha-key.txt", 'r') as f:
        captcha_key = f.read()
    if '\n' in captcha_key:
        captcha_key = captcha_key[:-1]
    capmonster = TurnstileTask(captcha_key)
    task_id = capmonster.create_task("https://form.waitlistpanda.com/go/aOfkJhcpwDHpJVkzO6FB?ref=QXEMoSDtjW1kxzG83LWa",
                                     "0x4AAAAAAABCOgX4x6RvmA0a")
    result = capmonster.join_task_result(task_id)
    return result['token']