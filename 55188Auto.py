# -*- coding:utf-8 -*-
import os
import requests

def cookie_str_to_dict(cookie_str):
    cookie_dict = {}
    for item in cookie_str.split(';'):
        if '=' in item:
            key, value = item.strip().split('=', 1)
            cookie_dict[key] = value
    return cookie_dict

def login_with_cookie(cookie_str, verify_url, keyword):
    session = requests.session()
    cookie_dict = cookie_str_to_dict(cookie_str)
    session.cookies.update(cookie_dict)

    try:
        response = session.get(verify_url)
        if keyword in response.text:
            print("✅ Cookie login success")
            return True
        else:
            print("❌ Cookie invalid or expired")
            print(response.text[:300])  # debug preview
            return False
    except Exception as e:
        print("❌ Request failed:", e)
        return False

if __name__ == '__main__':
    cookie
