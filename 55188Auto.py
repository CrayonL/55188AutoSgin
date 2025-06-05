import requests
import os

def sign_in(cookie_str):
    session = requests.Session()
    # 将 cookie 字符串转为字典
    cookie_dict = dict(i.strip().split("=", 1) for i in cookie_str.split(";") if "=" in i)
    session.cookies.update(cookie_dict)

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://www.55188.com/plugin.php?id=sign",
        "Host": "www.55188.com",
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "zh-CN,zh;q=0.9",
    }

    url = "https://www.55188.com/plugin.php?id=sign&mod=add&jump=1"
    res = session.get(url, headers=headers)
    res.encoding = 'gbk'

    if "签到成功" in res.text or "success" in res.text:
        print("🎉 签到成功")
    elif "已经签到" in res.text:
        print("✅ 今天已经签到过了")
    elif "Access Denied" in res.text:
        print("❌ 被拦截了，可能是 Referer 或 Cookie 不正确")
    else:
        print("⚠️ 未知签到状态：")
        print(res.text[:300])


if __name__ == '__main__':
    cookie = os.environ.get("COOKIE_55188")
    sign_in(cookie)
