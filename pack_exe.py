#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# ======================================================
# @File:  : pack_exe
# @Author : forward_huan
# @Date   : 2023/2/15 20:38
# @Desc   :
# ======================================================
import os
from PyInstaller.__main__ import run as start_pack


def build(name=None, is_one_file=True):
    root_path = os.path.dirname(os.path.abspath(__file__))
    dist_path = r"D:\Software"
    out_path = os.path.join(root_path, "out")
    build_path = os.path.join(out_path, "build")
    py_file = os.path.join(root_path, "main.py")
    params = [
        "-y", py_file, "-n", name, "--distpath", dist_path, "--workpath", build_path,
        "--specpath", build_path
    ]
    if is_one_file:
        params.append("-F")
    print(" ".join(params))
    start_pack(params)
    print("打包完成")


if __name__ == '__main__':
    build("PreQtUI", True)
