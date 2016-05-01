dataset="./%s" % "AAN"
file_cit=open(dataset+"/testset_cit.txt",'r')
file_count_cited=open(dataset+"/count_cited.txt",'r')
file_out = open(dataset+"/testet_per_ref.txt",'w')

citation = file_cit.readlines()
count_cited = file_count_cited.readlines()

count_zero = 0

for i in range(len(citation)):
	tmp = 0
	line = citation[i]
	line = line.strip()
	line = line.split()
	if len(line) == 0:
		count_zero += 1
		file_out.write("no ref"+'\n')
	else:
		for j in range(len(line)):
			tmp += int(count_cited[int(line[j])])
		per_ref = float(tmp) / len(line)
		file_out.write(str(per_ref)+'\n')

print count_zero
file_out.close()
