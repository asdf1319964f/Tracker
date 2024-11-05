import requests

# 文件 URLs 列表
urls = [
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_best.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_udp.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_http.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_https.txt",
    "https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all_ws.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/best.txt",
    "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/http.txt"
]

# 合并内容保存的文件名
output_file = "all.txt"

# 打开输出文件并写入内容
with open(output_file, 'w', encoding='utf-8') as file:
    for url in urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # 检查请求是否成功
            file.write(response.text + "\n")  # 写入内容并添加换行符
        except requests.exceptions.RequestException:
            # 发生错误时不做任何处理
            pass
