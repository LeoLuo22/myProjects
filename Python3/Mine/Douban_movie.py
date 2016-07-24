# -*- coding:utf-8 -*-
__author__ = "Leo Luo"

import requests
from bs4 import BeautifulSoup
import collections

BASE_URL = "https://www.douban.com/accounts/login?source=movie"
LOGIN_URL = "https://accounts.douban.com/login"
MOVIE = "https://movie.douban.com/"
HEAD = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Host':'www.douban.com',
'Pragma':'no-cache',
'Referer':'https://movie.douban.com/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

session = requests.Session()
session.get("https://movie.douban.com/", headers=HEAD)

def login(data):
    login = session.post(LOGIN_URL, headers=HEAD, data=data)
    r = session.get(MOVIE, headers=HEAD)
    print(r.text)


def main():
    data = collections.OrderedDict()
    data['source'] = 'movie'
    data['redir'] = 'https://movie.douban.com/'
    email = input("请输入用户名：")
    data['form_email'] = email
    password = input("请输入密码：")
    data['form_password'] = password
    data['login'] = '登录'
    login(data)

if __name__ == "__main__":
    main()








