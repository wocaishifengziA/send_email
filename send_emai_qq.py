import smtplib
from email.mime.text import MIMEText
from email.header import Header

settings = {}


def setup(mail_host, mail_user, mail_pass):
    global settings
    settings = {
        "mail_host": mail_host,  # 服务器
        "mail_user": mail_user,  # 用户名
        "mail_pass": mail_pass   # 口令
    }


def send_email_notify(recv_addr, topic, message):
    """
    使用QQ邮箱发送邮件
    :param recv_addr: 接收地址
    :param topic: 主题
    :param message: 内容
    :return:
    """

    # 第三方 SMTP 服务 QQ
    mail_host = settings["mail_host"]  # 设置服务器
    mail_user = settings["mail_user"]  # 用户名
    mail_pass = settings["mail_pass"]  # 口令

    sender = mail_user       # 发送邮箱
    receivers = [recv_addr]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(message, 'plain', 'utf-8')
    message['From'] = Header("", 'utf-8')
    message['To'] = Header(recv_addr, 'utf-8')

    subject = topic
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

