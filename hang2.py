import random
choice=1
while(choice!='N'):
	lister=[]
	f=open('Words.txt','r')
	lister=f.readlines()

	word=random.choice(lister)

	g_word=[]

	s_word=[]

	hanglist=[
	' 	____________________\n 	|	||\n 	|	||\n 	|	||\n',	
				' 	|  _____||______\n	|  |           |\n	|  |   0  0    |\n	|  |           |\n	|  |   \__/    |\n	|   \_________/\n',
				' 	| \    |__|    /\n 	|  \___|__|___/\n	|      |__|\n	|      |__|\n	|      |__|\n	|      |__|\n',
				'	|     /    \ \n	|    /      \ \n	|   /        \ \n	| _/          \_ \n',
				''
			]

	def checkChar(char,s_word,g_word):
		count=0
		flag=0
		for ele in s_word:
			if ele==char:
				g_word[count]=char
				flag=1
			count+=1
		if flag==0:
			return 0	
		return g_word	
		
	
	for char in word:
		if(char!='\n'):	
			s_word.append(char)
			g_word.append('_ ')
		
	print(''.join(g_word))
	
	ip=0
	
	chances=0
	
	while(chances<4):
		ip=input('Guess: ')
		if ip in g_word:
			print('ALREADY GUESSED!!!')	
		elif ip not in 'abcdefghijklmnopqrstuvwxyz':
			print('ENTER AN APLPHABET')
		elif (checkChar(ip,s_word,g_word)==0):
			chances+=1
			for i in range(chances):
				print(hanglist[i],end='')
			if chances==4:
				print('YOU LOSE!!!')
				print('CORRECT WORD IS:'+ ''.join(s_word))
				break
		else:
			g_word=checkChar(ip,s_word,g_word)
			print(''.join(g_word))
			for i in range(chances):
					print(hanglist[i],end='')
			if '_ ' not in g_word :
				print('WIN!!!')
				break
	
	choice=input('CONTINUE?(Y or N)')
		