
from datetime import datetime

content = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <title>小熊家安全觀測中心</title>
    <style>
        body {{
            background-color: #111;
            color: #eee;
            font-family: "Noto Sans TC", sans-serif;
            padding: 2em;
            line-height: 1.6;
        }}
        h1 {{ color: #f44; }}
        h2 {{ border-bottom: 1px solid #444; padding-bottom: 0.2em; margin-top: 2em; }}
        .alert {{ font-size: 1.2em; font-weight: bold; color: #f99; }}
        .orange {{ color: #fa3; }}
        a {{ color: #6cf; }}
    </style>
</head>
<body>
    <h1>小熊家安全觀測中心</h1>
    <p>更新日期：{datetime.today().strftime("%Y-%m-%d")}</p>
    <div class="section">
        <h2>📍 今日台灣戰爭風險評估</h2>
        <p class="alert orange">🟠 高風險：共機活動增多，美日軍演頻繁，中國強硬表態。</p>
        <ul>
            <li>共機13架次進入 ADIZ</li>
            <li>沖繩周邊美日聯演持續</li>
            <li>中國外交部發出警告</li>
        </ul>
    </div>
    <div class="section">
        <h2>🛫 外國撤僑與警報觀察（台灣 & 杜拜）</h2>
        <h3>台灣</h3>
        <ul>
            <li>美國維持第2級警示</li>
        </ul>
        <h3>杜拜</h3>
        <ul>
            <li>各大使館未升級警告</li>
        </ul>
    </div>
</body>
</html>"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
