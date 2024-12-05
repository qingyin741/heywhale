import subprocess

def open_dingtalk():
    # 钉钉的应用路径
    dingtalk_path = r"C:\Program Files (x86)\DingDing\main\current\DingTalk.exe"

    # 尝试打开钉钉
    subprocess.Popen(dingtalk_path)

# 调用函数
open_dingtalk()
