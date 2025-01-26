import tkinter as tk
import random
import threading
import time
# 全局变量，用于表示机器人是否正在点击
is_robot_clicking = False
# 定义机器人点击的函数
def robot_click(mode):
    global is_robot_clicking
    is_robot_clicking = True
    min_clicks = 0
    max_clicks = 0
    if mode == "困难":
        min_clicks = 6
        max_clicks = 8
    elif mode == "中等":
        min_clicks = 4
        max_clicks = 6
    else:
        min_clicks = 1
        max_clicks = 4

    click_count = 0
    start_time = time.time()
    while is_robot_clicking and time.time() - start_time < 60:
        click_count += 1
        time.sleep(1)
        click_speed = random.randint(min_clicks, max_clicks)
        click_count += click_speed
        root.after(0, lambda: update_count_label(click_count))
    is_robot_clicking = False
# 更新显示点击数量的标签
def update_count_label(count):
    count_label.config(text=f"机器人点击次数: {count}")
# 用户点击困难模式按钮的处理函数
def user_click_hard():
    global user_hard_click_count
    user_hard_click_count += 1
    global is_robot_clicking
    if is_robot_clicking:
        is_robot_clicking = False
        time.sleep(1)  # 等待1秒确保之前的线程停止
    threading.Thread(target = robot_click, args = ("困难",)).start()
# 用户点击中等模式按钮的处理函数
def user_click_medium():
    global user_medium_click_count
    user_medium_click_count += 1
    global is_robot_clicking
    if is_robot_clicking:
        is_robot_clicking = False
        time.sleep(1)
    threading.Thread(target = robot_click, args = ("中等",)).start()
# 用户点击普通模式按钮的处理函数
def user_click_easy():
    global user_easy_click_count
    user_easy_click_count += 1
    global is_robot_clicking
    if is_robot_clicking:
        is_robot_clicking = False
        time.sleep(1)
    threading.Thread(target = robot_click, args = ("普通",)).start()
# 比较结果并显示
def compare_results(mode):
    global is_robot_clicking
    is_robot_clicking = False
    user_count = 0
    if mode == "困难":
        user_count = user_hard_click_count
    elif mode == "中等":
        user_count = user_medium_click_count
    else:
        user_count = user_easy_click_count
    if user_count > click_count:
        result_label.config(text = "你赢了!")
    elif user_count < click_count:
        result_label.config(text = "你输了!")
    else:
        result_label.config(text = "平局!")
# 创建主窗口
root = tk.Tk()

# 初始化用户点击次数
user_hard_click_count = 0
user_medium_click_count = 0
user_easy_click_count = 0

# 创建模式选择按钮
hard_button = tk.Button(root, text="困难", command = lambda: [user_click_hard(), compare_results("困难")])
medium_button = tk.Button(root, text="中等", command = lambda: [user_click_medium(), compare_results("中等")])
easy_button = tk.Button(root, text="普通", command = lambda: [user_click_easy(), compare_results("普通")])

hard_button.pack()
medium_button.pack()
easy_button.pack()

# 创建显示机器人点击次数的标签
count_label = tk.Label(root, text="机器人点击次数: 0")
count_label.pack()

# 创建显示结果的标签
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
