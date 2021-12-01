#!/usr/bin/env python3

def fact(n) :
	
	f =1  
	if n == 0 or n ==1 :
		return 1 
	else :
		for i in range(1,n+1) :
			f*=i
		return f
