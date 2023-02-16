#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# ======================================================
# @File:  : main
# @Author : forward_huan
# @Date   : 2023/2/15 20:23
# @Desc   :
# ======================================================
import argparse
import os
import re
import threading

from pip._vendor.distlib.compat import raw_input

template = """import sys
from #PACKAGE# import #CLASS_NAME#
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)
ui = #UI_DESIGNER#(#PARAMS#)
if isinstance(ui, QWidget):
    win = ui
else:
    win = QWidget()
    ui.setupUi(win)
win.show()
sys.exit(app.exec_())
"""


def get_version():
    return "1.0.0.0"


def parse_args():
    parse = argparse.ArgumentParser(description="PyQt5界面预览工具")
    parse.add_argument(
        "-f", "--file_path", type=str, required=True, help="PyQt5 UI界面的Python文件")
    parse.add_argument(
        "-r", "--root_path", type=str, required=True, default=".", help="项目根目录")
    parse.add_argument(
        "-p", "--params", type=str, nargs="+", default=[], help="UI界面文件中所需的参数")
    parse.add_argument(
        "-v", "--version", action='version', version=get_version(), help="显示版本号")
    return parse.parse_args()


def get_class_name(codes):
    class_names = []
    for line in codes:
        t_line = str(line).strip()
        if t_line.startswith("class"):
            class_names.append(t_line[5:t_line.find("(")].strip())
    return class_names


def trans(item):
    if isinstance(item, str):
        return f'"{item}"'
    return str(item)


def get_package(file_path: str, root_path: str):
    f_path = re.sub(r"([\\|/])+", ".", file_path)
    r_path = re.sub(r"([\\|/])+", ".", root_path)
    return f_path[len(r_path) + 1:-3]


def get_template(file_path, root_path, class_name, params):
    return template \
        .replace("#UI_DESIGNER#", class_name) \
        .replace("#PARAMS#", ",".join([trans(item) for item in params])) \
        .replace("#PACKAGE#", get_package(file_path, root_path)) \
        .replace("#CLASS_NAME#", class_name)


def run(python_path, py_path):
    try:
        os.system(f"{python_path} {py_path}")
    except Exception as ex:
        print(str(ex))


def run_ui(file_path: str, root_path, params: list):
    print("-" * 20)
    print("启动预览文件", file_path)
    print("项目根路径", root_path)
    print("参数配置", params)
    try:
        if not file_path.endswith("py"):
            raise Exception(f"该文件不是Python可执行文件")
        with open(file_path, "r", encoding="utf8")as f:
            temp = f.readlines()
        class_names = get_class_name(temp)
        class_name = class_names[0]
        if len(class_names) > 1:
            name_str = '\n'.join([f'{i} {name}' for i, name in enumerate(class_names)])
            msg = f"请选择需要加载的类序号\n{name_str}\n"
            class_name = class_names[int(raw_input(msg))]
        py_path = os.path.join(root_path, "PreQtUI.py")
        python_path = os.path.join(root_path, r"venv\Scripts\python.exe")
        if not os.path.exists(python_path):
            python_path = "python"
        with open(py_path, "w", encoding="utf8")as f:
            f.write(get_template(file_path, root_path, class_name, params))
        threading.Thread(target=run, args=(python_path, py_path)).start()
    except Exception as ex:
        print(str(ex))


if __name__ == '__main__':
    try:
        args = parse_args()
        run_ui(args.file_path, args.root_path, args.params)
    except Exception as e:
        print(str(e))
