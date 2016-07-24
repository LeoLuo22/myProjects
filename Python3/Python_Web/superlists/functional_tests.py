# -*- coding:utf-8 -*-
__author__ = "Leo Luo"

from selenium import webdriver

brower = webdriver.Firefox()

#Someone heard of a cool online TODO app
#He went to the webpage of this app
brower.get("http://127.0.1.1:8080")

#He noticed that the title and header of this page include "TODO"
assert "To_Do" in brower.title

#The app invites him to input a to-do
#He input "Buy peacock feathers" in a text
#His hobbies are using the flys to fish
#He pressd Enter and the page was refreshed
#The to-do list showed "1: Buy peacock feathers"

#Another text frame shows, and it can input other to-dos
#He inputs "Use peacock feathers to make a fly"
#Refreshed again,His list shows the to-dos
#He wants to know weather the website would remember his list
#He sees the website generate a unique URL
#And some instructions shows
#He viewd the URL and finds that the list exists
#He is satisfacted,go to bed

brower.quit()
