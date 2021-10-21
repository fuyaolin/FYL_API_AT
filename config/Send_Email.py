"""
    发送邮件
"""
# -*- coding: utf-8 -*-
import smtplib
import os
from email.mime.text import MIMEText
from common.ReadConfigFile import ReadConfig
from common.ReadPath import EXCEL_PATH
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header


def sendmail():
    # smtp服务器，端口
    smtp_server = ReadConfig().get_smtp_server
    smtp_port = ReadConfig().get_smtp_port
    # 发件人
    sender = ReadConfig().get_email_sender
    username = ReadConfig().get_email_sender_username
    password = ReadConfig().get_email_sender_password
    # 收件人
    receiver = ReadConfig().get_email_receiver
    # 抄送人
    CC = ReadConfig().get_email_CC
    # 邮件主题
    mail_title = '自动化测试邮件'
    # 邮件内容
    mail_content = '自动化测试已完成，请查看127.0.0.1：'

    # 创建邮件对象
    message = MIMEMultipart()
    # 发送方
    message['From'] = sender
    # 接收方
    message['To'] = receiver
    # 接收抄送
    message['CC'] = CC
    # 主题
    message['Subject'] = Header(mail_title, "utf-8")

    # # # 发送附件
    # enclosure_basename = "at_report.xlsx"
    # path = os.path.join(EXCEL_PATH, "ceshi.xlsx")
    # enclosure = MIMEApplication(open(path, 'rb').read())
    # enclosure["Content-Type"] = 'application/octet-stream'
    # # 注意：此处basename要转换为gbk编码，否则中文会有乱码。
    # enclosure.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', enclosure_basename))

    # 构建纯文本的邮件内容;第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码
    message.attach(MIMEText(mail_content, 'plain', 'utf-8'))
    # message.attach(enclosure)

    # 开启发信服务
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.connect(smtp_server, smtp_port)
    try:
        # 0是关闭，1是开启debug
        server.set_debuglevel(0)
        # 跟服务器打招呼，告诉它我们准备连接，最好加上这行代码
        server.ehlo(smtp_server)
        # 登录发信邮箱
        server.login(username, password)
        # 发送邮件
        if len(CC.split(',')) == 0:
            server.sendmail(sender, receiver, message.as_string())
        else:
            server.sendmail(sender, receiver+CC, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("无法发送邮件,error:", e)
    finally:
        # 关闭服务器
        server.quit()


if __name__ == '__main__':
    sendmail()