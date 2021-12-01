#!/usr/bin/env python3



def findDup(l1) :
	l = [] 
	for i in l1 :
		if i not in l :
			l.append(i)

	for j in l :
		if j in l1 :
			l1.remove(j)
	return l1
