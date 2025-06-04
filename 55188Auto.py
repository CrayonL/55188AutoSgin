# -*- coding:utf-8 -*-
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
    cookie = "passport2bbs=pfJTp8aScNazKYCGmTMpBU2JZW46lY2oldpVTa2p54SMFX1eaQ5R5WQNTPseqiYd; cdb2_auth=iCeohzTEXNZAL9AD5UyLjzv3wVZ5%2BplYCwuhgRiGL%2FY1HnVTQLu%2BBTq%2BVuGnr6E0Ig; vOVx_56cc_auth=3828i61AuOpPr7trSRcSym58Dsn8FV20lGaeEvBXUYd5BskLruqW0ikWlUO2KsuyrIeZf4RWp2Elh5cTrXsYwQgVdm6X; vOVx_56cc_sid=mjAJiK; vOVx_56cc_plugin_sign_cookie=9c74b5def39f2c33e3f3618b409f4f6c; vOVx_56cc_lastact=1749032182%09home.php%09follow"

    if not cookie:
        raise ValueError("❌ 未设置 COOKIE，请检查输入")

    verify_url = "https://www.55188.com/plugin.php?id=sign"
    keyword = "理想股票技术论坛"  # 登录后页面中出现的关键词

    session = login_with_cookie(cookie, verify_url, keyword)
    if session:
        sign_in(session)
