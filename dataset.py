import numpy as np
import matplotlib.pyplot as plt

f = open("dataset.txt", "w")

label = 'sun,mon,tue,wed,thu,fri,sat'

for i in range(30):
	label += ','+ str(i+1)

label += ',jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec'

for i in range(0,28):

	label += ',' + (str(6+i//2) if i%2==0 else (str(6 + i//2) + ':30'))

f.write(label+'\n')

month_modifier = [1,1,1,.9,.9,1,1,1,.8,1,1,.7]

day_modifier  = [.7,1,1,1,1,1,.8]

stand_div_percent = 10

median = [10,20,30,70,100,85,70,55,40,25,20,20,50,60,40,30,20,20,20,60,70,115,110,100,80,60,40,20]

#plt.plot(median)
#plt.show()

day = -1
date = -1
month = -1

for i in range(0,1080):

	day = (day+1)%7
	date = (date+1)%30
	if i%12 ==0:
		month = (month+1)%12

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

	f.write(stin+stnew[:-1]+'\n')





f.close()



