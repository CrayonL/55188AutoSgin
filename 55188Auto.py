import requests
import os

def sign_in(cookie_str):
    cookies = dict(i.strip().split("=", 1) for i in cookie_str.split(";") if "=" in i)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://www.55188.com/plugin.php?id=sign",
        "Host": "www.55188.com",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }
    url = "https://www.55188.com/plugin.php?id=sign&mod=add&jump=1"
    res = requests.get(url, headers=headers, cookies=cookies)
    res.encoding = 'gbk'
    text = res.text
    if "success" in text:
        print("🎉 签到成功")
    elif "Access Denied" in text:
        print("❌ 被拦截了，可能是 Referer 或 Cookie 不正确")
    else:
        print("⚠️ 未知签到状态：")
        print(text[:1000])

if __name__ == '__main__':
    cookie = os.environ.get("COOKIE_55188")
    sign_in(cookie)
