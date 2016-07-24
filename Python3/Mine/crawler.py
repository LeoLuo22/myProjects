#-*- coding:utf-8 -*-
__author__ = "Leo Luo"

import requests
from bs4 import BeautifulSoup
import collections
import lxml
import os
import sys
from PIL import Image

BASE_URP_URL = "http://bksjw.chd.edu.cn"
LOGIN_URL = "http://bksjw.chd.edu.cn/loginAction.do"
HEAD = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:17.0) Gecko/20100101 Firefox/17.0','Connection': 'Keep-Alive'}
IMG_URL = "http://bksjw.chd.edu.cn/xjInfoAction.do?oper=img" #头像的URL
USER_INFO_URL = "http://bksjw.chd.edu.cn/xjInfoAction.do?oper=xjxx"
GRADE = "http://bksjw.chd.edu.cn/bxqcjcxAction.do"

class iCHD(object):
    def __init__(self, username, user_info=None, session=None):
        self.username = username
        user_info = collections.OrderedDict()
        self.__user_info = user_info
        self.session = requests.Session()

    @property
    def user_info(self):
        return self.__user_info

    @user_info.setter
    def user_info(self, value):
        self.__user_info = value

    def login(self):
        init_session = self.session.get(BASE_URP_URL, headers=HEAD)
        if init_session.status_code == 200:
            print("建立连接成功！")
        data = {'zjh':self.username,'mm':self.username,'dllx':'dldl'}
        index = self.session.post(LOGIN_URL,data=data, headers=HEAD)
        if index.status_code == 200:
            print("登陆成功")
        image = self.session.get(IMG_URL, headers=HEAD)
        global img_content
        """******Student's Photo***************"""
        img_content = image.content
        with open("test.png", "wb") as fh:
            fh.write(img_content)
        im = Image.open("test.png")
        im.show()
        user_info_index = self.session.get(USER_INFO_URL,headers=HEAD)
        soup = user_info_index.text#content.decode('utf-8')
        return soup

    def get_content(self):
        raw_content = collections.OrderedDict()
        grade = self.session.get(GRADE, headers=HEAD)
        user_info = self.session.get(USER_INFO_URL, headers=HEAD)
        grade_content = grade.text
        user_info_content = user_info.text
        raw_content['grade'] = grade_content
        raw_content['user_info'] = user_info_content
        return raw_content

    def parse_user_info(self, user_info_content):
        soup = BeautifulSoup(user_info_content, 'lxml')
        id_num = soup.find_all('td', attrs={'width':'275'})
        user_info_list = []
        for i in id_num:
            user_info_list.append(i.string.strip())
        print(user_info_list)
        print(len(user_info_list))
        user_info = collections.OrderedDict()
        try:
            user_info['学号：'] = user_info_list[0]
            user_info['姓名：'] = user_info_list[1]
            user_info['姓名拼音：'] = user_info_list[2]
            user_info['英文姓名：'] = user_info_list[3]
            user_info['曾用名：'] = user_info_list[4]
            user_info['身份证号：'] = user_info_list[5]
            user_info['性别：'] = user_info_list[6]
            user_info['学生类别：'] = user_info_list[7]
            user_info['特殊学生类型：'] = user_info_list[8]
            user_info['学籍状态：'] = user_info_list[9]
            user_info['收费类别：'] = user_info_list[10]
            user_info['民族：'] = user_info_list[11]
            user_info['籍贯：'] = user_info_list[12]
            user_info['出生日期：'] = user_info_list[13]
            user_info['政治面貌：'] = user_info_list[14]
            user_info['考区：'] = user_info_list[15]
            user_info['毕业中学：'] = user_info_list[16]
            user_info['高考总分：'] = user_info_list[17]
            user_info['录取号：'] = user_info_list[18]
            user_info['高考考生号：'] = user_info_list[19]
            user_info['入学语种考试：'] = user_info_list[20]
            user_info['通讯地址：'] = user_info_list[21]
            user_info['邮编：'] = user_info_list[22]
            user_info['家长信息：'] = user_info_list[23]
            user_info['入学日期：'] = user_info_list[24]
            user_info['系所：'] = user_info_list[25]
            user_info['专业：'] = user_info_list[26]
            user_info['专业方向：'] = user_info_list[27]
            user_info['年级：'] = user_info_list[28]
            user_info['班级：'] = user_info_list[29]
            user_info['是否有学籍：'] = user_info_list[30]
            user_info['是否有国家学籍：'] = user_info_list[31]
            user_info['校区：'] = user_info_list[32]
            user_info['异动否：'] = user_info_list[33]
            user_info['外语语种：'] = user_info_list[34]
            user_info['宿舍地址：'] = user_info_list[35]
            user_info['因材施教：'] = user_info_list[36]
            user_info['培养层次：'] = user_info_list[37]
            user_info['培养方式：'] = user_info_list[38]
            user_info['分流方向：'] = user_info_list[39]
            user_info['是否离校：'] = user_info_list[40]
            user_info['备注：'] = user_info_list[41]
            user_info['备注1：'] = user_info_list[42]
            user_info['备注2：'] = user_info_list[43]
            user_info['备注3：'] = user_info_list[44]
            self.user_info['name'] = user_info_list[1]
        except IndexError as err:
            print("用户不存在!")
        print(len(user_info))
        for key, value in user_info.items():
            print(key, value)
        return 0


def main():
    a = iCHD()
    soup = a.login()
    a.parse_user_info(soup)


if __name__ == "__main__":
    main()
