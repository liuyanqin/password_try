cs = 0  #次数
while cs < 3:
	password = input('请输入密码：')
	cs = cs + 1
	if password =='a123456':  #密码正确
		print('登录成功')
		break
	else:   #密码错误
		if  cs == 1:
			print('密码错误，您还有两次机会')
		elif  cs == 2:
			print('密码错误，您还有一次机会')
		else:
			print('密码错误，请改天再试')

		
