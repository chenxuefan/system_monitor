# -*- coding: utf-8 -*-
"""
# Talk is cheap,show me the codes!

@Author billie
@Time 2020/7/27 7:13 下午
@Describe 

"""
from sysInfo import sysInfo
from xlsxEdit import xlsxEdit
from emailService import email
import schedule

while True:
    #获取系统信息
    allInfo = sysInfo().allInfo
    #得到写入好的xlsx文件
    xlsname = xlsxEdit(data=allInfo).workbook
    #通过邮箱发送
    def send():
        myemail = email()
        myemail.get_msg(att_file_path='./',att_file_name=xlsname)
        myemail.send_email()

    #设定每日定时任务
    schedule.every().day.at("08:00").do(send)
    while True:
        schedule.run_pending()
