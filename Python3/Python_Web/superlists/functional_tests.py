# -*- coding:utf-8 -*-
__author__ = "Leo Luo"

from selenium import webdriver

brower = webdriver.Firefox()
brower.get("http://127.0.1.1:8080")
assert "Django" in brower.title
