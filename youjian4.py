import smtplib
from email.mime.text import MIMEText#构建正文
from email.header import Header#文件名

from_addr = "1521537244@qq.com"
to_addr = '1521537244@qq.com'    #自己发送给自己
psw='dwipeizfrmzhgbic'    #在邮箱里点击设置，账户，然后登陆授权码之后获得的
smtp_server="smtp.qq.com"


with open("test.txt",'r',encoding="utf-8") as fp:
	contents=fp.read()
print(contents)    #把邮件变成了网页版的（即html）



contents= "<h1>美少女嗨嗨嗨</h1>"#发送内容
msg=MIMEText(contents,'html','utf-8')    #plain普通版的，html是加粗版的
msg['From']=from_addr
msg['To']=to_addr
msg['Subject']="宇宙无敌青春美少女"

server=smtplib.SMTP(smtp_server,25)
server.login(from_addr,psw)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()  #退出服务器
