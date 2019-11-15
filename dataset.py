import numpy as np
import matplotlib.pyplot as plt

fin = open("input.txt", "w")
fres = open("result.txt", "w")


month_modifier = [1,1,1,.9,.9,1,1,1,.8,1,1,.7]

day_modifier  = [.7,1,1,1,1,1,.8]

stand_div_percent = 10

median = [10,20,30,70,100,85,70,55,40,25,20,20,50,60,40,30,20,20,20,60,70,115,110,100,80,60,40,20]

#plt.plot(median)
#plt.show()

day = 0
date = 0
month = 0

for _ in range(0,1080):
	new =[]
	for time_segemt in median:
		noise = 1 + np.random.normal(0,stand_div_percent)/100
		new += [round(time_segemt*month_modifier[month]*day_modifier[day]*noise)]
	

	day_vec=[0]*7
	day_vec[day] = 1

	date_vec = [0]*30
	date_vec[date] = 1

	month_vec = [0]*12
	month_vec[month] = 1

	in_vec = day_vec + date_vec + month_vec

	stnew=''
	for i in new:
		stnew+=str(i)+','

	stin ='' 
	for i in in_vec:
		stin += str(i)+','

	#plt.plot(new)
	#plt.show()

	fres.write(stnew[:-1]+'\n')
	fin.write(stin[:-1]+'\n')

	day = (day+1)%7
	date = (date+1)%30
	month = (month+1)%12


fin.close()
fres.close()


