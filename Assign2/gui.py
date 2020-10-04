import wqi
import tkinter as tk
from tkinter import ttk 
from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
tabControl = ttk.Notebook(root) 
  
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl) 
tabControl.add(tab1, text ='TASK 1') 
tabControl.add(tab2, text ='TASK 2') 
tabControl.add(tab3, text ='TASK 3') 

tabControl.pack(expand = 1, fill ="both") 

csv =None
csv_q2 = None

def add_tab1(tab1):
	tk.Label(tab1, text="pH").grid(row=0)
	tk.Label(tab1, text="Tempurature").grid(row=1)
	tk.Label(tab1, text="Turbidity").grid(row=2)
	tk.Label(tab1, text="TDS").grid(row=3)
	tk.Label(tab1, text="Nitrates").grid(row=4)
	tk.Label(tab1, text="Fecal coliform").grid(row=5)
	
	e1 = tk.Entry(tab1)
	e2 = tk.Entry(tab1)
	e3 = tk.Entry(tab1)
	e4 = tk.Entry(tab1)
	e5 = tk.Entry(tab1)
	e6 = tk.Entry(tab1)
	e7 = tk.Entry(tab1)
	
	
	e1.grid(row=0, column=2)
	e2.grid(row=1, column=2)
	e3.grid(row=2, column=2)
	e4.grid(row=3, column=2)
	e5.grid(row=4, column=2)
	e6.grid(row=5, column=2)
	e7.grid(row=7, column=2)

	def open_file():
		file = filedialog.askopenfilename(title = "choose your file",filetypes =[('csv files','*.csv')])
		global csv 
		csv = pd.read_csv(file)

	btn = Button(tab1, text ='Choose file', command = lambda:open_file()) 
	btn.grid(row=6,column=1)
	tk.Label(tab1, text="Output File Name").grid(row=7)


	def show_entry_fields():
		try:
			qual_ind = wqi.q1_main(float(e1.get()),float(e2.get()),float(e3.get()),float(e4.get()),float(e5.get()),float(e6.get()))
			tk.Label(tab1,text=qual_ind).grid(row=0,column=4)
		except:
			print("pls fill values")
		
		qual_ind_vec = []
		if csv is not None:
			for i in range(len(csv)) : 
				print(csv.iloc[i, 0], csv.iloc[i, 2]) 
				qual_ind = wqi.q1_main(csv.iloc[i, 0],csv.iloc[i, 1],csv.iloc[i, 2],csv.iloc[i, 3],csv.iloc[i, 4],csv.iloc[i, 5])
				# tk.Label(tab1,text=qual_ind).grid(row=i,column=7)
				qual_ind_vec.append(qual_ind)
		
			csv["WQI"] = qual_ind_vec
			outputfname = e7.get()
			csv.to_csv(outputfname, index=False)

	tk.Button(tab1, 
			  text='Quit', 
			  command=tab1.quit).grid(row=9, 
										column=0, 
										sticky=tk.W, 
										pady=4)
	tk.Button(tab1, 
			  text='Show', command=show_entry_fields).grid(row=9, 
														   column=1, 
													   sticky=tk.W, 
													   pady=4)

def add_tab2(tab2):
	atts = ["Turbidity", "pH","Color","DO", "BOD","TDS", "Hardness","Cl","No3","So4","Coliform","As","F"]
	for i in range(0, len(atts)):
		tk.Label(tab2, text=atts[i]).grid(row=i)
	
	ets= []
	for i in range(0, len(atts)):
		ets.append(tk.Entry(tab2))
	
	for i,et in enumerate(ets):
		et.grid(row=i, column=2)
	
	ets.append(tk.Entry(tab2))
	ets[-1].grid(row=14, column=1)
	# ets.grid(row=14, column=1)

	def open_file():
		file = filedialog.askopenfilename(title = "choose your file",filetypes =[('csv files','*.csv')])
		global csv_q2
		csv_q2 = pd.read_csv(file)
		# print(csv_q2.head())

	btn = Button(tab2, text ='Choose file', command = lambda:open_file()) 
	btn.grid(row=13,column=1)
	tk.Label(tab2, text="Output File Name").grid(row=14)

	def show_entry_fields():
		qual_ind_vec = []
		if csv_q2 is not None:
			for i in range(len(csv_q2)) : 
				# print(csv.iloc[i, 0], csv.iloc[i, 2]) 
				pars = [csv_q2.iloc[i,j] for j in range(0, 13)]
				qual_ind = wqi.q2_main(pars)
				# tk.Label(tab1,text=qual_ind).grid(row=i,column=7)
				qual_ind_vec.append(qual_ind)
		
			csv_q2["OIP"] = qual_ind_vec
			outputfname = ets[-1].get()
			csv_q2.to_csv(outputfname, index=False)
		else:
			tot = len(ets)-1
			params = [float(i.get()) for i in ets[:tot-1]]
			qual_ind = wqi.q2_main(params)
			tk.Label(tab2,text=qual_ind).grid(row=0,column=4)

	tk.Button(tab2, 
			  text='Quit', 
			  command=tab2.quit).grid(row=len(atts)+4, 
										column=0, 
										sticky=tk.W, 
										pady=4)
	tk.Button(tab2, 
			  text='Show', command=show_entry_fields).grid(row=len(atts)+4, 
														   column=1, 
													   sticky=tk.W, 
													   pady=4)
	
add_tab1(tab1)
add_tab2(tab2)
root.mainloop()