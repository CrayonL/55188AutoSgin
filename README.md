---

````markdown
# 📌 55188 自动签到脚本（基于 GitHub Actions）

本项目使用 Python + GitHub Actions 实现每日自动访问 [55188 股市论坛](https://www.55188.com) 并完成签到操作。

无需本地部署，绑定 Cookie 后即可每天自动运行。

---

## ✅ 功能说明

- 自动访问签到页面：`plugin.php?id=sign`
- 判断是否已经签到（根据签到按钮 DOM 判断）
- 若未签到，则访问 `plugin.php?id=sign&mod=add&jump=1` 发起签到请求
- 支持 GitHub Actions 自动定时运行（每天一次）
- 控制台输出签到结果：已签、成功、异常或拦截

---

## 🧾 使用方法（GitHub Actions 自动运行）

### 1. Fork 本仓库

点击右上角 `Fork` 按钮，将项目复制到你自己的 GitHub 帐号。

### 2. 获取Cookie

- 进入www.55188.com`
- f12 进入网络(network)刷线一下页面
-  选择文档(document),只有一个www.55188.com的文档,单击
- 选择标头(Headers) → 找到响应标头(ReuestHeaders) → 找到Cookie复制备用

### 3. 设置 Cookie（GitHub Secrets）

进入你的 Fork 后仓库：

- 打开 `Settings` → `Secrets and variables` → `Actions`
- 点击 `New repository secret`
  - Name：`COOKIE_55188`
  - Value：粘贴你的完整 Cookie 字符串(第二步获取的cookie)

### 3. 启用 GitHub Actions

首次 Fork 后，请确保在仓库的 `Actions` 页面点击 `Enable workflows` 以启用自动任务。

系统会自动每天运行一次签到任务。

---

## 📅 调度频率修改（可选）

如需修改自动运行频率，请编辑 `.github/workflows/sign.yml` 文件中的以下内容：

```yaml
schedule:
  - cron: '0 0 * * *'  # 每天 UTC 0 点运行，可改为你希望的时间
````

> 你可以使用网站 [crontab.guru](https://crontab.guru) 来生成合适的时间表达式。

---

## 📦 本地运行（可选）

如希望在本地测试脚本，确保已安装 Python 3：

```bash
pip install requests
python sign_55188.py
```

将 Cookie 写入环境变量或代码中运行。

---

## ⚠️ 注意事项

* Cookie 有效期有限，建议每隔一段时间重新更新
* 若网站改版或出现验证码，则脚本可能失效
* 本项目仅供学习与自动化实践使用，请勿用于违规行为

---

## 🧑‍💻 作者

Crayon
脚本由 Python 编写，部署自动化使用 GitHub Actions 实现。

````
