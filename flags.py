from function import *


class Flags:
    """标识类，记录程序运行过程中的各种状态标识"""
    def __init__(self):
        # 下载/暂停状态标识，True-进行下载/False-暂停
        self.con_pau_flag = False
        # 子线程退出标识
        self.exit_thread_flag = False
        # 用户代理
        self.ua = get_ua()
        # 子线程
        self.t = None
        # 下载中标识
        self.downloading = False
