
import csv
import matplotlib.pyplot as plt
import collections #


# take in a csv



# empty dictionary

# for source in file:
# 	if source is in dictionary
# 	increase dictionary count by 1

# 	elif source is not in dictionary
# 	add to dicionary
# 	set count to 1

tups = []
def loadDataSet(path='data'):
	source_list=[]

	for row in open(path+'/10_10_all.csv'):
		(source, destination)=str(row).split(',')[2:4]
		source_list.append(source) #getting ip addresses

	source_dict={}

	for address in source_list:	

		if address in source_dict:
			source_dict[address] += 1

		else:
			source_dict[address] = 1


	return source_dict



sources = loadDataSet()

addresses = []
count = []

for w in sorted(sources, key=sources.get, reverse=True): #sorts by value number
  addresses.append(w)
  count.append(sources[w])

# take first 5 dictionary keys
# plot their values

# x = ip addresses
# y = numbers

plt.xlabel(addresses[:5])
plt.ylabel(count[:5])
plt.plot(count[:5], 'ro--')

plt.show()

