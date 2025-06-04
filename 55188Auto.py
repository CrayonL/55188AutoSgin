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
            return session  # 返回 session 用于后续请求
        else:
            print("❌ Cookie invalid or expired")
            print(response.text[:300])
            return None
    except Exception as e:
        print("❌ Request failed:", e)
        return None

def sign_in(session):
    url = "https://www.55188.com/plugin.php?id=dsu_paulsign:sign&operation=qiandao&inajax=1"
    data = {
        'formhash': '',  # 稍后填
        'qdmode': 1,
        'todaysay': '早上好，签到来了！',
        'fastreply': 1
    }

    # 获取 formhash
    homepage = session.get("https://www.55188.com/plugin.php?id=dsu_paulsign:sign")
    if "formhash" in homepage.text:
        import re
        match = re.search(r'name="formhash" value="(\w+)"', homepage.text)
        if match:
            data['formhash'] = match.group(1)
        else:
            print("❌ 未能提取 formhash")
            return
    else:
        print("❌ 页面中未包含 formhash，可能未登录")
        return

    # 提交签到请求
    response = session.post(url, data=data)
    if "签到成功" in response.text or "已经签到" in response.text:
        print("🎉 签到成功！")
    else:
        print("❌ 签到失败，返回内容：")
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
