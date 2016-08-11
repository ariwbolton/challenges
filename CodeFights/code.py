import re
from math import sqrt

'''
math =
imp.load_source("/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/math.so")

sqrt = math.sqrt
'''

def math(expression):
	e = expression.replace("^", "**")
	n = re.sub(r"(\d+)", modify, e)
	return int(eval(n[:-1]))

def modify(s):
	return "float(" + s.group(0) + ")"
	
print math('(10^3-500)/(10^2)=') == 5
print math('2+2=') == 4
print math('(10^3-500)/(10^2)=') == 5
print math('sqrt(28+8-9)=') == 5
print math('75*(sqrt(82)-9)=') == 4
print math('-5*(-5)=') == 25
print math('5*(-5)=') == -25
print math('(10^2)/10=') == 10
