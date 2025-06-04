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
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36",
    "Referer": "https://www.55188.com/",
    "Host": "www.55188.com",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

        response = session.get(verify_url, headers=headers)
        if keyword in response.text:
            print("✅ Cookie login success")
            return session  # 返回 session 用于后续请求
        else:
            print("❌ Cookie invalid or expired")
            print(response.text[:300])
            return None
    except Exception as e:
        print("❌ Request failed:", e)
        return None

def sign_in(session):
    url = "https://www.55188.com/plugin.php?id=sign&mod=add&jump=1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36",
        "Referer": "https://www.55188.com/",
        "Host": "www.55188.com",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    response = session.get(url, headers=headers)

    if "已经签到" in response.text or "签到成功" in response.text or "签到记录" in response.text:
        print("🎉 签到成功！")
    elif "您今天还没有签到" in response.text:
        print("⚠️ 已打开签到页面，但好像没有执行签到动作")
    else:
        print("⚠️ 无法确认签到状态，返回内容如下：")
        print(response.text[:300])

if __name__ == '__main__':
    cookie = os.environ.get("COOKIE_55188")

    if not cookie:
        raise ValueError("❌ 未设置 COOKIE_55188 环境变量，请检查 GitHub Secrets 设置")

    verify_url = "https://www.55188.com/plugin.php?id=dsu_paulsign:sign"
    keyword = "欢迎回到理想大家庭"

    session = login_with_cookie(cookie, verify_url, keyword)
    if session:
        sign_in(session)
