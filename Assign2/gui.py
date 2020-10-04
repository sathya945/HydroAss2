import wqi
import tkinter as tk
from tkinter import ttk 
from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog
import pandas as pd
import homepage

root = tk.Tk()
root.wm_title("Water Quality Index Estimation Tool")
root.geometry("900x600")
tabControl = ttk.Notebook(root) 


home = ttk.Frame(tabControl)
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl) 
tabControl.add(home, text ='HOME') 
tabControl.add(tab1, text ='TASK 1') 
tabControl.add(tab2, text ='TASK 2') 
tabControl.add(tab3, text ='TASK 3') 

tabControl.pack(expand = 1, fill ="both") 

csv =None
csv_q2 = None


def add_tab1(tab1):
	head = tk.Label(tab1, text="TASK 1", font=("Verdana", 20))
	head.place(x=400,y=10)

	attrs = ["pH", "Temperature"," Turbidity","TDS","Nitrates","Fecal Coliform"]
	labs = []
	ets = []
	for i in range(len(attrs)):
		labs.append(tk.Label(tab1, text=attrs[i]))
		ets.append(tk.Entry(tab1))
		labs[i].place(x = 200, y = 50 + (50 * i))
		ets[i].place(x = 450, y = 50 + (50 * i))

	def open_file():
		file = filedialog.askopenfilename(title = "choose your file",filetypes =[('csv files','*.csv')])
		global csv 
		csv = pd.read_csv(file)

	btn = Button(tab1, text ='Choose file', command = lambda:open_file()) 
	# btn.grid(row=6,column=1)
	btn.place(x=420, y=400)
	out_name = tk.Label(tab1, text="Output File Name")
	out_name.place(x=200, y=450)
	ets.append(tk.Entry(tab1))
	ets[-1].place(x=450, y=450)

	classes = ["Very Bad", "Bad", "Medium", "Good", "Excellent"]
	def show_entry_fields():
		qual_ind_vec = []
		qual_cls_vec = []
		if csv is not None:
			for i in range(len(csv)) : 
				print(csv.iloc[i, 0], csv.iloc[i, 2]) 
				qual_ind = wqi.q1_main(csv.iloc[i, 0],csv.iloc[i, 1],csv.iloc[i, 2],csv.iloc[i, 3],csv.iloc[i, 4],csv.iloc[i, 5])
				# tk.Label(tab1,text=qual_ind).grid(row=i,column=7)
				if qual_ind>=0 and qual_ind<25:
					wq_clss = classes[0]
				elif qual_ind>=25 and qual_ind<50:
					wq_clss = classes[1]
				elif qual_ind>=50 and qual_ind<70:
					wq_clss = classes[2]
				elif qual_ind>=70 and qual_ind<90:
					wq_clss = classes[3]
				else:
					wq_clss = classes[4]
				qual_ind_vec.append(qual_ind)
				qual_cls_vec.append(wq_clss)
		
			csv["WQI"] = qual_ind_vec
			csv["WQC"] = qual_cls_vec
			outputfname = ets[-1].get()
			csv.to_csv(outputfname, index=False)
		else:
			evals = [float(et.get()) for et in ets[:-1]]
			qual_ind = wqi.q1_main(evals[0],evals[1],evals[2],evals[3],evals[4],evals[5])
			if qual_ind>=0 and qual_ind<25:
				wq_clss = classes[0]
			elif qual_ind>=25 and qual_ind<50:
				wq_clss = classes[1]
			elif qual_ind>=50 and qual_ind<70:
				wq_clss = classes[2]
			elif qual_ind>=70 and qual_ind<90:
				wq_clss = classes[3]
			else:
				wq_clss = classes[4]
    			
    				
			wq = tk.Label(tab1,text=qual_ind, font=("Verdana",25))
			wq_lab = tk.Label(tab1,text="WQI", font=("Verdana",30))
			wq_class = tk.Label(tab1,text="WQC", font=("Verdana",30))
			wq_class_val = tk.Label(tab1,text=wq_clss, font=("Verdana",25))
			wq.place(x=700, y=300)
			wq_lab.place(x=700, y=250)
			wq_class.place(x=700, y=350)
			wq_class_val.place(x=700, y=400)

	qt = tk.Button(tab1, text='QUIT', command=tab1.quit)
	qt.place(x=500, y=500)
	calc = tk.Button(tab1, text='CALCULATE', command=show_entry_fields)
	calc.place(x=350, y=500)


def add_tab2(tab2):
	head = tk.Label(tab2, text="TASK 2", font=("Verdana", 20))
	head.place(x=400,y=10)
	atts = ["Turbidity", "pH","Color","DO", "BOD","TDS", "Hardness","Cl","No3","So4","Coliform","As","F"]
	classes = ["Very Bad", "Bad", "Medium", "Good", "Excellent"]
	labs = []
	ets= []
	for i in range(0, len(atts)):
		labs.append(tk.Label(tab2, text=atts[i]))
		ets.append(tk.Entry(tab2))
		labs[i].place(x = 200, y = 50 + (30 * i))
		ets[i].place(x = 450, y = 50 + (30 * i))

	def open_file():
		file = filedialog.askopenfilename(title = "choose your file",filetypes =[('csv files','*.csv')])
		global csv_q2
		csv_q2 = pd.read_csv(file)

	btn = Button(tab2, text ='Choose file', command = lambda:open_file()) 
	btn.place(x=420, y=450)
	out_name = tk.Label(tab2, text="Output File Name")
	out_name.place(x=200, y=500)
	ets.append(tk.Entry(tab2))
	ets[-1].place(x=450, y=500)

	def show_entry_fields():
		qual_ind_vec = []
		qual_cls_vec = []
		if csv_q2 is not None:
			for i in range(len(csv_q2)) : 
				# print(csv.iloc[i, 0], csv.iloc[i, 2]) 
				pars = [csv_q2.iloc[i,j] for j in range(0, 17)]
				qual_ind = wqi.q2_main(pars)
				if qual_ind>=0 and qual_ind<25:
					wq_clss = classes[0]
				elif qual_ind>=25 and qual_ind<50:
					wq_clss = classes[1]
				elif qual_ind>=50 and qual_ind<70:
					wq_clss = classes[2]
				elif qual_ind>=70 and qual_ind<90:
					wq_clss = classes[3]
				else:
					wq_clss = classes[4]
				qual_ind_vec.append(qual_ind)
				qual_cls_vec.append(wq_clss)
				# tk.Label(tab1,text=qual_ind).grid(row=i,column=7)
		
			csv_q2["OIP"] = qual_ind_vec
			csv_q2["WQC"] = qual_cls_vec
			outputfname = ets[-1].get()
			csv_q2.to_csv(outputfname, index=False)
		else:
			evals = [float(et.get()) for et in ets[:-1]]
			qual_ind = wqi.q2_main(evals)
			if qual_ind>=0 and qual_ind<25:
				wq_clss = classes[0]
			elif qual_ind>=25 and qual_ind<50:
				wq_clss = classes[1]
			elif qual_ind>=50 and qual_ind<70:
				wq_clss = classes[2]
			elif qual_ind>=70 and qual_ind<90:
				wq_clss = classes[3]
			else:
				wq_clss = classes[4]
    			
    				
			wq = tk.Label(tab2,text=qual_ind, font=("Verdana",25))
			wq_lab = tk.Label(tab2,text="WQI", font=("Verdana",30))
			wq_class = tk.Label(tab2,text="WQC", font=("Verdana",30))
			wq_class_val = tk.Label(tab2,text=wq_clss, font=("Verdana",25))
			wq.place(x=700, y=300)
			wq_lab.place(x=700, y=250)
			wq_class.place(x=700, y=350)
			wq_class_val.place(x=700, y=400)

	qt = tk.Button(tab2, text='QUIT', command=tab2.quit)
	qt.place(x=500, y=540)
	calc = tk.Button(tab2, text='CALCULATE', command=show_entry_fields)
	calc.place(x=350, y=540)
	
homepage.add_home(home)
add_tab1(tab1)
add_tab2(tab2)
root.mainloop()