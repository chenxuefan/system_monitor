# -*- coding: utf-8 -*-
"""
# Talk is cheap,show me the codes!

@Author billie
@Time 2020/7/19 9:17 下午
@Describe 

"""
# -*- coding: utf-8 -*-
'''
@Author billie
@Date 2020/5/14 13:32
@Describe 

'''
import smtplib  # 发邮件
from email.mime.multipart import MIMEMultipart # 用于构建邮件对象
from email.header import Header # 用于构建邮件头
from email.mime.text import MIMEText # 用于构建内容文本
from email.mime.image import MIMEImage #
from email.mime.audio import MIMEAudio #
from email.mime.application import MIMEApplication #
import psutil,threading,schedule,time

class email():
    def __init__(self):
        # -----------------------基本信息------------------------
        # 服务器，端口
        self.host = 'smtp.qq.com'
        self.port = 465
        # 发送者，授权码（非密码）
        self.sender = '2380540710@qq.com'
        self.password = 'ghioratrikzeebbj'
        # 接收者
        self.receivers = ['2380540710@qq.com', '2478477118@qq.com']  # 添加多个账户时采用列表形式
        # 邮件内容
        self.msg = MIMEMultipart() # 构造一个MIMEMultipart对象代表邮件本身
        # ------------------------------------------------------

    def get_msg(self,att_file_path=None,att_file_name=None):

        # 构建邮件头
        self.msg['From'] = Header('人人都爱小雀斑','utf-8')  # 发件人的名称或地址
        self.msg['To'] = Header('billie','utf-8')  # 发件人邮箱地址
        self.msg['Subject'] = Header('no theme','utf-8')  # 主题

        # 1、邮件文本内容
        '''
        构建文本：MIMEText(_text=text, _subtype='plain', _charset='utf-8')
        '''
        # 1.1、发送内容为字符串文本
        text = ''
        # 构建纯文本的邮件内容，plain代表纯文本11
        string_of_email = MIMEText(_text=text, _subtype='plain', _charset='utf-8')#内容，内容类型，编码

        # 1.2、发送内容为html格式
        html = '''
            <p>点击一下</p>
            <p><a href="http://billie52707.cn/">每天好心情！</a></p>
        '''
        html_of_email = MIMEText(html,'html','utf-8')

        # 添加内容文本到邮件
        self.msg.attach(html_of_email)

        # 2、携带附件
        '''
        MIME有很多种类型，如果附件是图片格式，我要用MIMEImage，如果是音频，要用MIMEAudio，如果是word、excel，得上google去查。
        最懒的方法就是，不管什么类型的附件，都用MIMEApplication，MIMEApplication默认子类型是application/octet-stream。
        
        # 2.1、附件为txt
        with open('./file/test.txt','rb') as f:
            att_txt_of_email = MIMEText(_text=f.read(),
                                        _subtype='base64',
                                        _charset='utf-8')
            # att_txt_of_email['Content-Type'] = 'application/octet-stream'
            # att_txt_of_email['Content-Disposition"'] = 'attachment;filename="test.txt"'
            att_txt_of_email.add_header('Content-Disposition', 'attachment', filename='test.txt')

        # 2.2、附件为图片
        with open('./file/big sur.jpeg','rb') as f:
            att_image_of_email = MIMEImage(_imagedata=f.read(),
                                           _subtype='base64',
                                           _charset='utf-8')
            # att_image_of_email['Content-Type'] = 'application/octet-stream'
            # att_image_of_email['Content-Disposition"'] = 'attachment;filename="big sur.jpg"'
            att_image_of_email.add_header('Content-Disposition', 'attachment', filename='big sur.jpg')

        # 2.3、附件为音频
        with open('./file/RADWIMPS-デート.flac','rb') as f:
            att_audio_of_email = MIMEAudio(_audiodata=f.read(),
                                           _subtype='base64',
                                           _charset='utf-8')
            att_audio_of_email.add_header('Content-Disposition', 'attachment', filename='RADWIMPS-デート.flac')
        '''

        # 2.4、附件为任意类型
        try:
            with open('{}{}'.format(att_file_path,att_file_name),'rb') as f:
                att_application_of_email = MIMEApplication(_data=f.read(),
                                                           _subtype='base64')
                att_application_of_email.add_header('Content-Disposition','attachment',filename=att_file_name)

            # 添加附件到邮件
            # msg.attach(att_txt_of_email)
            # msg.attach(att_image_of_email)
            # msg.attach(att_audio_of_email)
            self.msg.attach(att_application_of_email)
        except:pass


    def send_email(self):
        # ----------------------登录并发送------------------------
        try:
            # 开启发信服务
            server = smtplib.SMTP_SSL(self.host)
            # 连接服务与端口
            server.connect(self.host, self.port)
            # 登录发信邮箱
            server.login(self.sender, self.password)
            # 发送邮件（发信人，接收者，邮件内容）
            server.sendmail(from_addr=self.sender,
                            to_addrs=self.receivers,
                            msg=self.msg.as_string())
            print('[{}]email already sent!'.format(time.strftime('%Y-%m-%d %H:%M:%S')))
            # 关闭服务器
            server.quit()
            # 设定间隔时间发送
            # threading.Timer(1000,send_email).start()
        except smtplib.SMTPException as e:
            print(e)



