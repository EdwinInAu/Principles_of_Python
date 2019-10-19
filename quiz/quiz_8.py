# A polynomial object can be created from a string that represents a polynomial
# as sums or differences of monomials.
# - Monomials are ordered from highest to lowest powers.
# - All factors are strictly positive, except possibly for the leading factor
# - For nonzero powers, factors of 1 are only implicit.
# A single space surrounds + and - signs between monomials.

# Written by Chongshi Wang and Eric Martin for COMP9021

import re 
from copy import deepcopy
class Polynomial:
	def __init__(self, polynomial = None):
		result = {}
		self.polynomial = result
		if polynomial is None:
			self.polynomial = {0:0}
		else: 	
			polynomial = polynomial.replace(' ','')
			polynomial = polynomial.replace('-','+-')
			polynomial = re.sub(r'x(?!\^)','x^1',polynomial)
			polynomial = re.sub(r'(?<!\d)x','1x',polynomial)
			c = polynomial.split('+')
			for item in c:
				if item == '':
					c.remove(item)
			a=[] 
			b=[]#key
			for item in c:
				a.append(re.findall('(\-?\d+)x',item))
				b.append(re.findall('\^(\d+)',item))
			for i in range(len(b)):
				if b[i] == []:
					b[i].append(0)
				b[i][0]= int(b[i][0])
			for i in range(len(a)):
				if a[i] == []:
					a[i].append(c[i])
				a[i][0]= int(a[i][0])
			u=[]
			p=[]#key
			for item in a:
				u.append(item[0])
			for item in b:
				p.append(item[0])
			for i in range(len(u)):
				if p[i] not in result.keys():
					result[p[i]] = u[i]
				else:
					result[p[i]] += u[i]
			result = order_dict(result)
			self.polynomial = result
	def __add__(self, other):
		new_polynomial = deepcopy(self.polynomial)
		if new_polynomial != {0:0}:
			for key,value in other.polynomial.items():
				if key in new_polynomial:
					new_polynomial[key] += other.polynomial[key]
				elif key not in new_polynomial:
					new_polynomial[key] = other.polynomial[key]
			new_polynomial = order_dict(new_polynomial)
			new = Polynomial()
			new.polynomial = new_polynomial
			return new
		else:
			old = Polynomial()
			old.polynomial = other.polynomial
			return old
	def __mul__(self, other):
		new_polynomial = deepcopy(self.polynomial)
		a = []
		b = []
		new_dict={}
		for key1,value1 in new_polynomial.items():
			for key2,value2 in other.polynomial.items():
				n = key1 + key2
				if n not in new_dict.keys():
					new_dict[n]= new_polynomial[key1] * other.polynomial[key2]
				else:
					new_dict[n] += new_polynomial[key1] * other.polynomial[key2]
		new_dict = order_dict(new_dict)
		new = Polynomial()
		new.polynomial = new_dict
		return new
	def __str__(self):
		if self.polynomial != {0:0}:
			a=[]
			r=''
			for keys,values in self.polynomial.items():
				a.append(keys)
			if len(a)==1:
				if a[0] == 0:
					r = r + str(self.polynomial[a[0]])
				if a[0] == 1:
					if self.polynomial[a[0]] == 1:
						r = r + 'x'
					if self.polynomial[a[0]] == -1:
						r = r + '-x'
					if self.polynomial[a[0]] != 1 and  self.polynomial[a[0]] != -1:
						r = r + str(self.polynomial[a[0]]) + 'x'
				if a[0] > 1:
					if self.polynomial[a[0]] == 1:
						r = r + 'x^' + str(a[0])  
					if self.polynomial[a[0]] == -1:
						r = r + '-x^' + str(a[0])
					if self.polynomial[a[0]] != 1 and  self.polynomial[a[0]] != -1:
						r = r + str(self.polynomial[a[0]]) + 'x^' + str(a[0])
			if len(a)>1:
				for i in range(len(a)-1):
					if a[i] == 1:
						if self.polynomial[a[i]] == 1:
							r = r + 'x'
							if self.polynomial[a[i+1]]>0:
								r = r + '+'	
						if self.polynomial[a[i]] == -1:
							r = r + '-x'
							if self.polynomial[a[i+1]]>0:
								r = r + '+'	
						if self.polynomial[a[i]] != 1 and  self.polynomial[a[i]] != -1:
							r = r + str(self.polynomial[a[i]]) 
							r = r + 'x'
							if self.polynomial[a[i+1]]>0:
								r = r + '+'
					if a[i] == 0:
						if str(self.polynomial[a[i]])!= 0:
							r = r + str(self.polynomial[a[i]]) 
					if a[i] != 0 and a[i] != 1:
						if self.polynomial[a[i]] == -1:
							r = r + '-x^'
							r = r + str(a[i])
							if self.polynomial[a[i+1]]>0:
								r = r + '+'
						if self.polynomial[a[i]] == 1:
							r = r + 'x^'
							r = r + str(a[i])
							if self.polynomial[a[i+1]]>0:
								r = r + '+'
						if self.polynomial[a[i]] != 1 and  self.polynomial[a[i]] != -1:
							r = r + str(self.polynomial[a[i]])
							r = r + 'x^'
							r = r + str(a[i])
							if self.polynomial[a[i+1]]>0:
								r = r + '+'
			if len(a)>1:
				if a[-1] == 0:
					if self.polynomial[a[-1]]!=0:
						r = r  + str(self.polynomial[a[-1]])							
				if a[-1] == 1:
					if self.polynomial[a[-1]] == 1:
						r = r +'x'
					if self.polynomial[a[-1]] == -1:
						r = r +'-x'
					else:
						r = r  + str(self.polynomial[a[-1]]) + 'x'
				if a[-1] > 1:	
					if self.polynomial[a[-1]] == 1:
						r = r +'x^' + str(a[-1])
					if self.polynomial[a[-1]] == -1:
						r = r +'-x^' + str(a[-1])
					if self.polynomial[a[i]] != 1 and  self.polynomial[a[i]] != -1:
						r = r  + str(self.polynomial[a[-1]]) + 'x^' + str(a[-1])
			if len(a)>1:
				a = r[1:]
				a = a.replace('+',' + ')
				a = a.replace('-',' - ')
				return r[0]+a
			if len(a)==1:
				return r
		else:
			return '0'
			
def order_dict(a):
	y = []
	for keys,values in a.items():
		y.append(keys)
		y.sort(reverse = True)
	return{i:a[i] for i in y}