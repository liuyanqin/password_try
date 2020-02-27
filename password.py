cs = 3  #次数
while cs > 0:
	password = input('请输入密码：')
	cs = cs - 1
	if password =='a123456':
		print('登录成功')
		break
	elif cs > 0: #3-cs>0
		print('密码错误，您还有', cs, '次机会')
	else:
		print('密码错误，您已经没有机会了，请您改天再试试吧')

		
