from chardet import detect
from os.path import isfile
count,blanks=0,0
with open("a.txt",'rb')as fp:
	code=detect(fp.read())['encoding']
	print(code)
#detect(fp.read())['encoding']
# 'r',encoding='utf-8'
with open("a.txt",'r',encoding=code)as fp:
	while True:
		line = fp.readline()
		if not line:
			break
		# if(len(line)-1)==0:
		# 	blanks+=1
		if  len(line.strip())==0:
			blanks+=1
		count+=1
print(count,blanks)
#查目录，行，和不同编码下都能运行的条件
path=r"C:\Users\Administrator\Desktop\a.txt"
print(isfile(path))