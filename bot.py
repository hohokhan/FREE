import random
import requests
import os

def luhn_checksum(num_str):
    total = 0
    reverse_digits = num_str[::-1]
    for i, digit in enumerate(reverse_digits):
        n = int(digit)
        if i % 2 == 0:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return (10 - (total % 10)) % 10

def generate_charge_code():
    first_15_digits = ''.join(random.choices('0123456789', k=15))
    check_digit = luhn_checksum(first_15_digits)
    full_code = first_15_digits + str(check_digit)
    formatted = '-'.join([full_code[i:i+4] for i in range(0, 16, 4)])
    return formatted

def send_to_telegram(message):
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

def main():
    irancell = generate_charge_code()
    rightel = generate_charge_code()
    hamrah_aval = generate_charge_code()

    message = f"""\
*کد شارژ جدید:*

`کد ایرانسل:` `{irancell}`
`کد رایتل  :` `{rightel}`
کد همراه اول: `{hamrah_aval}`
"""
    send_to_telegram(message)

if __name__ == "__main__":
    main()
