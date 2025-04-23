'''
This function implements a custom mathematical expression evaluator in Python, mimicking basic functionality of Python’s built-in eval() but with controlled behavior. It parses and computes arithmetic expressions following operator precedence (* and / before + and -).
'''

def eval(x:str)->int|float:
	"""
	Evaluates a mathematical expression given as a string, following basic arithmetic rules (operator precedence: * and / before + and -).
	
	Parameter:
		expression (str): A string containing a mathematical expression (e.g., "3+5*2-6/3").
	Return:
		Returns the computed result as an integer (if whole number) or float (if decimal).
		Returns "syntax error" for invalid expressions (e.g., "3++5", division by zero, or malformed numbers).
	
	"""
	original = str(x)
	try :
		plus=original.split("+")
		minus=[]
		molus=[]
		for i in plus:
			if "-" in i:
				minus=minus+i.split("-")
			else:
				molus=molus+[i]
		div=[]
		for j in minus:
			if "/" in j:
				div=div+j.split("/")
				for i in div:
					if "*" in str(i):
						a=i.split("*")
						res=1
						for k in a:
							res=res*float(k)
						div[div.index(i)]=res
                        
				res=int(div[0])
				for i in div[1::]:
					res=res/float(i)
				minus[minus.index(j)]=res
			else:
				if "*" in str(j):
					b=j.split("*")
					ans=1
					
					for y in b:
						ans=ans*float(y)
					minus[minus.index(j)]=ans
		dov=[]
		for j in molus:
			if "/" in j:
				dov=dov+j.split("/")
				for i in dov:
					if "*" in str(i):
						a=i.split("*")
						res=1
						for k in a:
							res=res*float(k)
						dov[dov.index(i)]=res
                        
				res=int(dov[0])
				for i in dov[1::]:
					res=res/float(i)
				molus[molus.index(j)]=res
			else:
				if "*" in str(j):
					b=j.split("*")
					ans=1

					for y in b:
						ans=ans*float(y)
						
					molus[molus.index(j)]=ans
		plu=0
		for i in molus:
			plu=plu+float(i)
		minu=0
		if len(minus)>0:
			minu=float(minus[0])
			for i in minus[1::]:
				minu=minu-float(i)
		else:
			minu=0

		final=plu+minu
		if ".0" in str(final):
			return (int(final))
		else:
			return(float(final))
                     
	except:
		return "syntax error" 
        
if __name__=="__main__":
	expression = input("EnTer ThE eXpressIon : ")
	result = eval(expression)
	print(result)

