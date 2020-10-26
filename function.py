#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import re
import os
from random import randint


def get_page_url(name):
    """返回一个完整的少前萌百页面url"""
    url = 'https://zh.moegirl.org/%E5%B0%91%E5%A5%B3%E5%89%8D%E7%BA%BF:' + urllib.parse.quote(name)
    return url


def get_ua():
    """获取一个新ua"""
    return USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]


def get_page_html(url, ua):
    """获取html页面字符串"""
    headers = {'User-Agent': ua}
    req = urllib.request.Request(url, headers=headers)
    page = urllib.request.urlopen(req)
    html = page.read()
    page.close()
    return html


def get_voice_url(html_code, folder_name):
    """获取音频文件url并存放于voice_url.txt文件中"""
    reg = r'https:\\/\\/.+?\.(?:mp3|ogg)'  # 正则表达式
    reg_data = re.compile(reg)  # 编译一下，运行更快
    data_list = reg_data.findall(html_code)  # 进行匹配
    unfin_file = open(folder_name + '/' + "url_unfinished.txt", 'w')
    for data in data_list:
        data = data.replace('\\', '')
        unfin_file.write(data + '\n')
    unfin_file.close()
    fin_file = open(folder_name + '/' + "url_finished.txt", 'w')
    fin_file.close()


def get_voice(url, headers, folder_name, file_name, flags):
    """下载单个语音文件"""
    req = urllib.request.Request(url, headers=headers)
    page = None
    try:
        page = urllib.request.urlopen(req, timeout=12)
        html = page.read()
    except Exception:  # 超时
        page.close()
        return False
    else:
        if flags.exit_thread_flag:
            return True
        file = open(folder_name + '/' + file_name, 'wb')
        file.write(html)
        file.close()
        page.close()
        return True


def update(file_name):
    """更新文件，删除首行"""
    with open(file_name, 'r') as old_file, open(file_name, 'r+') as new_file:
        old_file.readline()
        next_line = old_file.readline()
        while next_line:  # 连续覆盖剩余行，后面所有行上移一行
            new_file.write(next_line)
            next_line = old_file.readline()
        new_file.truncate()


def mkdir(path):
    """创建文件夹"""
    path = path.strip()   # 去除首位空格
    path = path.rstrip("\\")  # 去除尾部 \ 符号
    is_exists = os.path.exists(path)  # 判断路径是否存在
    if not is_exists:  # 如果不存在则创建目录
        os.makedirs(path)


# 用户代理（ua）
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]


