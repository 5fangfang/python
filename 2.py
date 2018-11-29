import os
root_path = os.getcwd()
offset = len(root_path.split("\\"))
# print(root_path)
for root,dirs,files in os.walk(root_path):
	current_dir=root
	path_list = current_dir.split("\\")
	indent_level = len(path_list)-offset
	print("\t"*indent_level,"\\"+path_list[-1])
	#print(length,len(length))
	for f in files:
		file_name =os.path.splitext(f)[0]
		print("\t"*(indent_level+1),file_name)
		#splitexi把文件名和扩展名分离
	# print(dirs)
	# os.path.splitext()
   

	# print(root)
	# length = root
