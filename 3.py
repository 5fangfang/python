# try:
# 	open("a.txt")
# except:
# 	print("NO such file or directory!")
# finally:
# 	print("Clear up!")
#功能异常处理
file_path = r'C:\Users\Administrator\Desktop\root\dir1\cp3_data_size.c'
# try:
# 	f=open(file_path)#变量
# except:
# 	print("No such file or directory!")
# finally:
# 	f.close()
# 	print("File closed!")
#自动抛出异常
# with open(file_path) as f:
# 	pass
def line_count(file_path):
	code_line,blank_line =0,0
	with open(file_path,'r') as fp:
	    while 1:
		    line = fp.readline()
		    if not line:
			    break
		    else:
		        code_line+=1
	print(code_line,"Lines")
line_count(file_path)