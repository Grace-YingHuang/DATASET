
dataset="./%s" % "AAN"
file_cit=open(dataset+"/training_cit.txt",'r')
file_cit_per_ref = open(dataset+"/citation_per_ref.txt",'w')
file_count_cited = open(dataset+"/count_cited.txt","w")
file_count_ref = open(dataset+"/count_ref.txt",'w')
# file_cit=open(dataset+"/test.txt",'r')
# file_cit_per_ref = open(dataset+"/test_av.txt",'w')
# file_count_cited = open(dataset+"/test_count.txt","w")

citation = file_cit.readlines()
cnt_doc = len(citation)

cnt_be_cit = 0   #number of documents be cited
cnt_have_ref = 0 #number of docuements have ref
cnt_total = 0    #number of links

count_cited=[0]*cnt_doc
line = ['a']*cnt_doc

for i in range(cnt_doc):
	line[i] = citation[i]
	line[i] = line[i].strip()
	line[i] = line[i].split()
	for j in range(1,len(line[i])):
		count_cited[int(line[i][j])]+=1

for i in range(cnt_doc):
	cnt_total += count_cited[i]
	if count_cited[i] != 0:
		cnt_be_cit += 1
	file_count_cited.write(str(count_cited[i]))
	file_count_cited.write('\n')

print "Number of doucments which are cited at least one time %d" %(cnt_be_cit)	
print "Average cited times per reference %f" %(float(cnt_total)/cnt_be_cit)

for i in range(cnt_doc):
	count_ref = len(line[i]) - 1
	if count_ref !=0:
		cnt_have_ref += 1
	file_count_ref.write(str(count_ref))
	file_count_ref.write('\n')
	
	count_total = 0
	for j in range(1,len(line[i])):
		count_total += count_cited[int(line[i][j])]
	if(count_ref == 0):
		count_av = 0
	else:
		count_av = float(count_total)/count_ref
	file_cit_per_ref.write(str(count_av))
	file_cit_per_ref.write('\n')

print "Number of doucments which have at least one ref %d" %(cnt_have_ref)	
file_cit_per_ref.close()
file_count_cited.close()
file_count_ref.close()
