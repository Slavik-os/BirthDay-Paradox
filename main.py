#!/usr/bin/env python3
from datetime import *
import random
from facto import fact 
from findDup import findDup

d_list = []
try :
	def main() :
		while True :
			try : 
				group = int(input(' Generate a Value  : \n >'))
				genDate(group)
				if d_list == [] :
					genDate(group)
				print(f'Change Percentage in group of (group) : ' ,format(findPercent(group),'.1f'),'%')
				print(f'The Dates that repeated are : {d_list} ')
			
			except ValueError:
				
				print('Enter a Valid range of Groups !')	
	# Make random Dates 
	def genDate(n) :
		genDate.dup_b = []
		same_dates = []
		# Date format : 1/Febrary/2012
		for i in range(n) :
			 # Date range :
			 start_date = date(2000,1,1)
			 end_date  = date(2010,2,1)
			 timeBetween = end_date - start_date
			 daysBetween =  timeBetween.days
			 random_number_of_days = random.randrange(daysBetween)
			 d = start_date + timedelta(days=random_number_of_days)
			 d  = d.strftime("%d - %b - %Y")
			 d_list.append(d)
		
		# Get Repeated Dates
		return findDup(d_list)	
		
	def findPercent(d) :
		days_y = 365
		e =(1- (fact(days_y) / fact(days_y - d)) / days_y ** d) *100
		return e 

	if __name__ == '__main__' :
		main()


except KeyboardInterrupt :
	print('quiting ... ')
