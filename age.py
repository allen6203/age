driving = input('請問有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('你怎麼可以開車')
elif driving == '沒有':
	if age >= 18:
		print('你可以考駕照了 怎麼不考')
	else:
		print('過幾年就可以考駕照了')