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

    # Step 1: 访问签到页面，看是否含有 #addsign 元素
    page_url = "https://www.55188.com/plugin.php?id=sign"
    page_res = requests.get(page_url, headers=headers, cookies=cookies)
    page_res.encoding = 'gbk'
    
    if 'id="addsign"' not in page_res.text:
        return "✅ 已签到（无 addsign 按钮）"

    # Step 2: 如果有 addsign，说明可以签到，发起签到请求
    sign_url = "https://www.55188.com/plugin.php?id=sign&mod=add&jump=1"
    res = requests.get(sign_url, headers=headers, cookies=cookies)
    res.encoding = 'gbk'
    if 'success' in res.text:
        print("🎉 签到成功！（模拟 JS 行为）")
    else:
        print("⚠️ 未知签到状态：")
        print(res.text[:500])

if __name__ == '__main__':
    cookie = os.getenv("COOKIE_55188")
    if not cookie:
        print("未检测到 COOKIE_55188 环境变量")
    else:
        result = sign_in(cookie)
        print(result)