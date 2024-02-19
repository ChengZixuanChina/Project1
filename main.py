# -*- coding:utf-8 -*-
# @Time    : 2024/2/19 20:26
# @Author  : ChengZixuanChina
# @File    : $main.py
import datetime
import logging
import os

if not os.path.exists("./log"):
    os.mkdir("./log")

log = logging.getLogger()
# 此处进行Logging.basicConfig() 设置，后面设置无效
logging.basicConfig(filename=f"./log/{datetime.date.today()}-log.log",
                    format='%(asctime)s [%(name)s] (%(levelname)s) %(message)s - %(funcName)s',
                    level=logging.DEBUG,
                    encoding="utf-8")


def main():
    log.info("starting main")


if __name__ == '__main__':
    main()
