#!/usr/bin/env python3
from tkinter import *
from datetime import *
import random
from facto import fact
from findDup import findDup


class Program :

	def __init__(self,master) :
		self.master = master
		master.geometry('600x550')

		master.Text = Label(master,text='Enter a value : ')
		master.Text.grid(row=0,column=0,padx=10,pady=10,sticky="nsew")

		master.e = Entry(master,text='testing')
		master.e.grid(row=0,column=1,pady=10,sticky="nsew")
		
		master.button = Button(master,text='Calculate',command= lambda:self.out(int(master.e.get())))
		master.button.grid(row=0,column=3)

		master.text = Text(master,width=50, height=20)
		master.text.grid(row=2,column=1,sticky="nsew")


	def out(self,e) :
		self.master.text.delete('1.0',END)
		self.genDate(e)
		p = format(self.findPercent(e),".2f")
		p = f'Percentage : {p}%'
		d = d_list	
		if d == [] :
			self.master.text.insert(END,f'Percentage : {p} \n No duplicated BirthDays where found !')
		else :
			self.master.text.insert(END,f'\n {p}')
			for i in d :
				self.master.text.insert(END,f'\n {i}')

	def genDate(self,n) :
		global d_list
		d_list = []
		dup_b = []
		same_dates = []
		# Date format : 1/Febrary/2012
		for i in range(n) :
			 # Date range :
			 start_date = date(1999,1,1)
			 end_date  = date(2002,2,1)
			 timeBetween = end_date - start_date
			 daysBetween =  timeBetween.days
			 random_number_of_days = random.randrange(daysBetween)
			 d = start_date + timedelta(days=random_number_of_days)
			 d  = d.strftime("%d - %b - %Y")
			 d_list.append(d)

		# Get Repeated Dates
		return findDup(d_list)
	def findPercent(self,d) :
		days_y = 365
		f =(1- (fact(days_y) / fact(days_y - d)) / days_y ** d) *100
		return f



root = Tk()

program = Program(root)
root.mainloop()
