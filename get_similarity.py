import re
import numpy as np
import os
import sys




resume1 = sys.argv[1]
resume2 = sys.argv[2]



							#reading from resume_1 1
with open(resume1, 'r') as myfile:
    data=myfile.read().replace('\n', ' ')


data = data.replace('.' , '')
data = data.replace(',' , '')
data = data.replace(';' , '')
data = data.replace('"' , '')
data = data.replace('<' , '')
data = data.replace('>' , '')
data = data.replace('(' , '')
data = data.replace(')' , '')
data = data.replace('/' , '')
data = data.replace(':' , '')
data = data.replace('-' , ' ')
data = data.replace('&' , '')



noise =['a','i','the','am','are','was','were','in','will','have','did','is','with','of','on'
,'and','to','for','as','be','such','this','at','by','from','school','how','also','it','new']


							#converting String in to list of words
re.findall(r'\S+', data)
data =data.split()



							#removing noise from resume_1 list

resume_1 = [''.join(w for w in place.split() if w.lower() not in noise)
         for place in data
         ]


							#calculating frequency of each word in resume_1
							#initialising dictionary for calculating frequency
dict={}
for i in range (0,len(resume_1)):
	dict[resume_1[i]]=0


for i in range (0,len(resume_1)):
	dict[resume_1[i]]=dict[resume_1[i]]+1


keys=[]

keys=dict.keys()
keywords=[]





							# reading from  resume_2

with open(resume2, 'r') as myfile:
    data_2=myfile.read().replace('\n', ' ')

data_2 = data_2.replace('.' , '')
data_2 = data_2.replace(',' , '')
data_2 = data_2.replace(';' , '')
data_2 = data_2.replace('"' , '')
data_2 = data_2.replace('<' , '')
data_2 = data_2.replace('>' , '')
data_2 = data_2.replace('(' , '')
data_2 = data_2.replace(')' , '')
data_2 = data_2.replace('/' , '')
data_2 = data_2.replace(':' , '')
data_2 = data_2.replace('-' , ' ')
data_2 = data_2.replace('&' , '')
							#converting String in to list of words
re.findall(r'\S+', data_2)
data_2 =data_2.split()



							#removing noise from resume_2 list
resume_2 = [''.join(w for w in place.split() if w.lower() not in noise)
         for place in data_2
         ]


							#calculating frequency of each word in resume_2
							#initialising dictionary for calculating frequency
dict_2={}
for i in range (0,len(resume_2)):
	dict_2[resume_2[i]]=0


for i in range (0,len(resume_2)):
	dict_2[resume_2[i]]=dict_2[resume_2[i]]+1




keys_2=[]
keys_2=dict_2.keys()
keywords_2=[]
match = []

							#calculating  matches in both resume

for i in range (0,len(keys)):
	for j in range (0,len(keys_2)):
		if(keys[i]==keys_2[j]):
			match.append(keys_2[j])



a=[]
b=[]			
match.remove('')
power_key = []

power_key =['JavaScript', 'Java', 'PHP', 'Python', 'C#', 'C++', 'Ruby', 'CSS', 'C', 'human', 'resources', 'Objective-C', 'business', 'manager', 'Coordinated', 'Headed', 'operated', 'Organized', 'Planned', 'Produced', 'Programmed', 'Administered', 'Charted', 'Designed', 'Developed', 'developer', 'Founded', 'Engineered', 'doctored', 'Launched', 'Capitalized', 'Cultivated', 'management', 'Directed', 'Guided', 'hr', 'Hired', 'Mentored', 'managed', 'Recruited', 'organizational', 'Regulated', 'Supervised', 'Trained', 'Advocated', 'Coached', 'Consulted', 'Consulting', 'Consult', 'Interpreted', 'Investigated', 'Surveyed', 'leadership', 'Authored', 'Campaigned', 'Co-authored', 'Composed', 'experienced', 'Convinced', 'Corresponded', 'Counseled', 'Documented', 'Edited', 'Publicized','published']

						#increasing weight of words which lies in power keywords   

for i in range (0,len(power_key)):
	for j in range (0,len(match)):
		if(power_key[i]==match[j]):
			dict[match[j]] = 4*dict[match[j]]
			dict_2[match[j]] = 4*dict_2[match[j]]

				
for i in range(0,len(match)):
	a.append(dict[match[i]])
	b.append(dict_2[match[i]])


#calculating similarity

#total number of words in resume_1 and resume_2
n_resume_1 = np.sum(dict.values())-dict['']
n_resume_2 = np.sum(dict_2.values())-dict_2['']
p = (n_resume_1+n_resume_2)/2

p1=[]
for i in range (0,len(match)):
	if(a[i]<b[i]):
		p1.append(a[i])
	else:
		p1.append(b[i])

sum_1 = np.sum(p1)

similarity=0

similarity = float(sum_1)/float(p)

print similarity		
	





