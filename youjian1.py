#POP: Post Office Protocal
#SMTP: Simple Mail Tran
import smtplib
from email.mime.text import MIMEText

from_addr = "1521537244@qq.com"  #发件
to_addr = "1521537244@qq.com"    #收件
psw = 'dwipeizfrmzhgbic'
smtp_server = "smtp.qq.com"

contents = "hello word" 
msg = MIMEText(contents,'plain','utf-8')
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = "Text"


server = smtplib.SMTP(smtp_server,25)
server.login(from_addr,psw)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
