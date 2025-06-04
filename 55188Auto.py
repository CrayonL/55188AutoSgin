# -*- coding:utf-8 -*-
import requests
import os

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

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.55188.com/",
        "Host": "www.55188.com",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    try:
        response = session.get(verify_url, headers=headers)
        response.encoding = 'gbk'
        if keyword in response.text:
            print("✅ Cookie login success")
            return session
        else:
            print("❌ Cookie invalid or expired")
            print("👇 返回内容预览：")
            print(response.text[:300])
            return None
    except Exception as e:
        print("❌ Request failed:", e)
        return None

def sign_in(session):
    sign_url = "https://www.55188.com/plugin.php?id=sign&mod=add&jump=1"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.55188.com/plugin.php?id=sign",
        "Host": "www.55188.com",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    response = session.get(sign_url, headers=headers)
    response.encoding = 'gbk'

    if "status" in response.text and "success" in response.text:
        print("🎉 签到成功！status: success")
    elif "已经签到" in response.text:
        print("✅ 今天已经签到过了")
    else:
        print("⚠️ 无法确认签到状态，返回内容如下：")
        print(response.text[:300])

if __name__ == '__main__':
    # 👇 在这里粘贴你的 Cookie 字符串
    cookie = os.environ.get("COOKIE_55188")
    if not cookie:
        raise ValueError("❌ 未设置 COOKIE，请检查输入")

    verify_url = "https://www.55188.com/plugin.php?id=sign"
    keyword = "理想股票技术论坛"  # 登录后页面中出现的关键词

    session = login_with_cookie(cookie, verify_url, keyword)
    if session:
        sign_in(session)
