"""
    发送邮件
"""
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from common.Read_Config import ReadConfig
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header


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
mail_title = 'Python自动发送的邮件'
# 邮件内容
mail_content = '邮件测试内容'

# 创建邮件对象
message = MIMEMultipart()
# 发送方
message['From'] = sender
# 接收方
# message['To'] = ",".join(receiver)
# 接收抄送
message['CC'] = CC
# 主题
message['Subject'] = Header(mail_title, "utf-8")
# 构建纯文本的邮件内容
message.attach(MIMEText(mail_content, 'report', 'utf-8'))

# # 发送附件
# attachment = MIMEApplication(open(REPORT_PATH, 'rb').read())
# attachment["Content-Type"] = 'application/octet-stream'
# # 给附件重命名
# basename = "at_report.report"
# # 注意：此处basename要转换为gbk编码，否则中文会有乱码。
# attachment.add_header('Content-Dispositon', 'attachment', filename=('utf-8', '', basename))
# message.attach(attachment)

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
    if CC.split(',') == '':
        server.sendmail(sender, receiver.split(','), message.as_string())
    else:
        server.sendmail(sender, receiver.split(',')+CC.split(','), message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("无法发送邮件")
finally:
    # 关闭服务器
    server.quit()
