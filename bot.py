import random
import requests
import os

def luhn_checksum(num_str):
    """محاسبه رقم کنترلی با الگوریتم لوهان (Luhn)"""
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
    """تولید کد شارژ ۱۶ رقمی بدون خط تیره"""
    first_15_digits = ''.join(random.choices('0123456789', k=15))
    check_digit = luhn_checksum(first_15_digits)
    full_code = first_15_digits + str(check_digit)
    return full_code

def send_to_telegram(message):
    """ارسال پیام به تلگرام از طریق ربات"""
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
*کد شارژ 20 هزار تمنی:*

کلیک کنید کپی میشه

کد ایرانسل 🟡: `{irancell}`

کد رایتل 🟣: `{rightel}`

کد همراه اول 🔵: `{hamrah_aval}`

@FreeRechargePackag
"""
    send_to_telegram(message)

if __name__ == "__main__":
    main()
