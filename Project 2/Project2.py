//
// COMP9021 Project 2
//
// Authors:
// Chongshi Wang
//
// Written: 15/05/2019
//

import re

def available_coloured_pieces(file):
	pieces={}
	text = file.read()
	text = text.replace("\n"," ")
	new_text = re.split(">",text)
	new_text.remove(new_text[-1])
	for i in range(1,len(new_text)-1):
		colour = re.findall( 'fill="(.+)"',new_text[i])
		points = re.findall('(\d*) (\d*)\s+[Lz]',new_text[i])
		new_points=[]
		for i in range(len(points)):
			list1 = list(points[i])
			list2=[]
			for i in range(len(list1)):
				list2.append(int(list1[i]))
			new_points.append(tuple(list2))
		pieces[colour[0]] = new_points
	return pieces

def are_valid(coloured_pieces):
	for keys,values in coloured_pieces.items():
		if len(values) < 3:
			return False
		values.append(values[0])
		values.append(values[1])
		for i in range(len(values)-3):
			if convex_polygon(values[i],values[i+1],values[i+2]) != convex_polygon(values[i+1],values[i+2],values[i+3]):
				return False
		for i in range(len(values)-3):
			for j in range(i+1,len(values)-2):
				if values[i]!=values[j+1] and values[i+1]!=values[j]:
					if convex_polygon(values[i],values[i+1],values[j])!=convex_polygon(values[i],values[i+1],values[j+1])\
					and convex_polygon(values[j],values[j+1],values[i])!=convex_polygon(values[j],values[j+1],values[i+1]):
						return False
	return True 

def convex_polygon(point1,point2,point3):
	a = point2[0]*point3[1] + point1[0]*point2[1] + point1[1]*point3[0]
	b = point1[1]*point2[0] + point2[1]*point3[0] + point1[0]*point3[1]
	det = a - b
	if det > 0:
		return 'counterclockwise'
	if det < 0:
		return 'clockwise'
	if det == 0:
		return 'no direction'

def are_identical_sets_of_coloured_pieces(coloured_pieces_1,coloured_pieces2):
	new_pieces1={}
	new_pieces2={}
	for keys1,values1 in coloured_pieces_1.items():
		if keys1 not in coloured_pieces2:
			return False
		list_x1=[]
		list_y1=[]
		for i in range(len(values1)):
			list1 = list(values1[i])
			list_x1.append(list1[0])
			list_y1.append(list1[1])
		min_x1 = int(min(list_x1))
		min_y1 = int(min(list_y1))
		new_points1=[]
		for i in range(len(values1)):
			list_1 = list(values1[i])
			list_1[0] = list_1[0] - min_x1
			list_1[1] = list_1[1] - min_y1
			new_points1.append((list_1[0],list_1[1]))
			new_pieces1[keys1]=new_points1
			
	for keys2,values2 in coloured_pieces2.items():
		if keys2 not in coloured_pieces_1:
			return False
		list_x2 = []
		list_y2 = []
		for i in range(len(values2)):
			list2 = list(values2[i])
			list_x2.append(list2[0])
			list_y2.append(list2[1])
		min_x2 = int(min(list_x2))
		min_y2 = int(min(list_y2))
		new_points2=[]
		for i in range(len(values2)):
			list_2 = list(values2[i])
			list_2[0] = list_2[0] - min_x2
			list_2[1] = list_2[1] - min_y2
			new_points2.append((list_2[0], list_2[1]))
			new_pieces2[keys2]=new_points2
	colours=[]
	if not are_valid(new_pieces1):
		return False
	if not are_valid(new_pieces2):
		return False
	for new_keys1,new_values1 in new_pieces1.items():
		colours.append(new_keys1)
	for i in range(len(colours)):
		if set(new_pieces1[colours[i]]) == set(new_pieces2[colours[i]]):
			return True
	for new_keys1,new_values1 in new_pieces1.items(): 
		new_pieces1[new_keys1] = type1(new_values1)
		if set(new_pieces1[new_keys1]) == set(new_pieces2[new_keys1]):
			return True
	for new_keys1,new_values1 in new_pieces1.items(): 
		new_pieces1[new_keys1] = type2(new_values1)
		if set(new_pieces1[new_keys1]) == set(new_pieces2[new_keys1]):
			return True
	for new_keys1,new_values1 in new_pieces1.items(): 
		new_pieces1[new_keys1] = type3(new_values1)
		if set(new_pieces1[new_keys1]) == set(new_pieces2[new_keys1]):
			return True
	for new_keys1,new_values1 in new_pieces1.items(): 
		new_pieces1[new_keys1] = type2(type1(new_values1))
		if set(new_pieces1[new_keys1]) == set(new_pieces2[new_keys1]):
			return True
	for new_keys1,new_values1 in new_pieces1.items(): 
		new_pieces1[new_keys1] =type1(type3(new_values1))
		if set(new_pieces1[new_keys1]) == set(new_pieces2[new_keys1]):
			return True
	for new_keys1,new_values1 in new_pieces1.items(): 
		new_pieces1[new_keys1] = type2(type3(new_values1))
		if set(new_pieces1[new_keys1]) == set(new_pieces2[new_keys1]):
			return True
	for new_keys1,new_values1 in new_pieces1.items():
		new_pieces1[new_keys1] = type2(type1(type3(new_values1)))
		if set(new_pieces1[new_keys1]) == set(new_pieces2[new_keys1]):
			return True
	return False
		
def type1(points): 
		list_x1=[]
		list_y1=[]
		for i in range(len(points)):
			list1 = list(points[i])
			list_x1.append(list1[0])
			list_y1.append(list1[1])
		min_x1 = int(min(list_x1))
		min_y1 = int(min(list_y1))
		max_x1 = int(max(list_x1))
		max_y1 = int(max(list_y1))
		new_list=[]
		for i in range(len(points)):
			new_list.append((points[i][0],max_y1-points[i][1]))
		return new_list
	
def type2(points): 
		list_x1=[]
		list_y1=[]
		for i in range(len(points)):
			list1 = list(points[i])
			list_x1.append(list1[0])
			list_y1.append(list1[1])
		min_x1 = int(min(list_x1))
		min_y1 = int(min(list_y1))
		max_x1 = int(max(list_x1))
		max_y1 = int(max(list_y1))
		new_list=[]
		for i in range(len(points)):
			new_list.append((max_x1-points[i][0],points[i][1]))
		return new_list

def type3(points): 
		list_x1=[]
		list_y1=[]
		list_x2=[]
		list_y2=[]
		list_x3=[]
		list_y3=[]
		for i in range(len(points)):
			list1 = list(points[i])
			list_x1.append(list1[0])
			list_y1.append(list1[1])
		min_x1 = int(min(list_x1))
		min_y1 = int(min(list_y1))
		max_x1 = int(max(list_x1))
		max_y1 = int(max(list_y1))
		new_list1=[]
		for i in range(len(points)):
			new_list1.append((-points[i][1],-points[i][0]))
		for i in range(len(new_list1)):
			list2=list(new_list1[i])
			list_x2.append(abs(list2[0]))
			list_y2.append(abs(list2[1]))
		max_x2 = int(max(list_x2))
		max_y2 = int(max(list_y2))
		new_list2=[]
		for i in range(len(new_list1)):
			new_list2.append((max_x2+new_list1[i][0],new_list1[i][1]))
		for i in range(len(new_list2)):
			list3 = list(new_list2[i])
			list_x3.append(abs(list3[0]))
			list_y3.append(abs(list3[1]))
		max_x3 = int(max(list_x3))
		max_y3 = int(max(list_y3))
		new_list3=[]
		for i in range(len(new_list2)):
			new_list3.append((new_list2[i][0],max_y3+new_list2[i][1]))
		return new_list3
		
def type4(points): 
		list_x1=[]
		list_y1=[]
		for i in range(len(points)):
			list1 = list(points[i])
			list_x1.append(list1[0])
			list_y1.append(list1[1])
		min_x1 = int(min(list_x1))
		min_y1 = int(min(list_y1))
		max_x1 = int(max(list_x1))
		max_y1 = int(max(list_y1))
		new_list=[]
		for i in range(len(points)):
			new_list.append((max_x1-points[i][1],max_y1-points[i][0]))
		return new_list
	
def type5(points): 
		list_x1=[]
		list_y1=[]
		list_x2=[]
		list_y2=[]
		for i in range(len(points)):
			list1 = list(points[i])
			list_x1.append(list1[0])
			list_y1.append(list1[1])
		min_x1 = int(min(list_x1))
		min_y1 = int(min(list_y1))
		max_x1 = int(max(list_x1))
		max_y1 = int(max(list_y1))
		new_list=[]
		for i in range(len(points)):
			new_list.append((max_y1-points[i][1],points[i][0]))
		for i in range(len(new_list)):
			list2 = list(new_list[i])
			list_x2.append(list2[0])
			list_y2.append(list2[1])
		min_x2 = int(min(list_x2))
		min_y2 = int(min(list_y2))
		max_x2 = int(max(list_x2))
		max_y2 = int(max(list_y2))
		a_list=[]
		for i in range(len(points)):
			a_list.append((max_y2-points[i][0],max_y1-points[i][1]))
		return a_list

def is_solution(tangram,shape):
	area_tangram = 0
	area_shape = 0
	for keys1, values1 in tangram.items():
		values1.append(values1[0])
		area1 = 0
		area2 = 0
		for i in range(len(values1)-1):
			area1 = area1 + values1[i][0]*values1[i+1][1]
		for i in range(len(values1)-1):
			area2 = area2 + values1[i+1][0]*values1[i][1]
		area_1 = abs(area1 - area2)/2
		area_tangram = area_tangram + area_1
	for keys2, values2 in shape.items():
		values2.append(values2[0])
		area3 = 0
		area4 = 0
		for i in range(len(values2)-1):
			area3 = area3 + values2[i][0]*values2[i+1][1]
		for i in range(len(values2)-1):
			area4 = area4 + values2[i+1][0]*values2[i][1]
		area_2 = abs(area3 - area4)/2
		area_shape = area_shape + area_2
	if int(area_shape) != int(area_tangram):
		return False
	for keys1,values1 in tangram.items():
		for item in values1:
			if out_of_bounds(item,values2):
				return False
	return True
    
def out_of_bounds(item, values2):
	pointA = (100000000000,item[1])
	n = 0
	for i in range(len(values2)-1):
		a = max(values2[i][0],values2[i+1][0])
		b = min(values2[i][0],values2[i+1][0])
		c = max(values2[i][1],values2[i+1][1])
		d = min(values2[i][1],values2[i+1][1])
		if item == values2[i] or item == values2[i+1]:
			return False
		if b<item[0]<a and d<item[1]<c and (item[0]-values2[i][0])/(item[1]-values2[i][1]) == (item[0]-values2[i+1][0])/(item[1]-values2[i+1][1]):
			return False
		if item[0]== values2[i][0]==values2[i+1][0] and d<item[1]<c:
			return False
		if item[1]== values2[i][1]==values2[i+1][1] and b<item[1]<a:
			return False
	for i in range(len(values2)-1):
		if convex_polygon(item, pointA, values2[i]) != convex_polygon(item, pointA, values2[i+1])\
		and convex_polygon(values2[i], values2[i+1], item) != convex_polygon(values2[i], values2[i+1], pointA):
			n = n + 1
	if n % 2 != 0:
		return False
	return True