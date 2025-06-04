# -*- coding:utf-8 -*-
import os
import requests

# 将 cookie 字符串转换为字典形式
def cookie_str_to_dict(cookie_str):
    cookie_dict = {}
    for item in cookie_str.split(';'):
        if '=' in item:
            key, value = item.strip().split('=', 1)
            cookie_dict[key] = value
    return cookie_dict

# 使用 cookie 登录验证
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
            print(response.text[:300])  # debug 预览部分内容
            return False
    except Exception as e:
        print("❌ Request failed:", e)
        return False

# 主执行入口
if __name__ == '__main__':
    # 从 GitHub Actions 的环境变量中读取 cookie
    cookie = os.environ.get("COOKIE_55188")

    if not cookie:
        raise ValueError("❌ 未设置 COOKIE_55188 环境变量，请检查 GitHub Secrets 设置")
    verify_url = "https://www.55188.com/usercp.php"  # 这是 55188 登录后的页面，可以换成你想验证的地址
    login_with_cookie(cookie, verify_url, keyword)
