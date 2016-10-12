
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

def loadDataSet(path='data'):
	source_list=[]

	for row in open(path+'/10_10_all.csv'):
		(source, destination)=str(row).split(',')[2:4]
		destination_list.append(destination) #getting ip addresses

	destination_dict={}

	for address in destination_list:	

		if address in destination_dict:
			destination_dict[address] += 1

		else:
			destination_dict[address] = 1

	return destination_dict



destinations = loadDataSet()

addresses = []
count = []

for w in sorted(destinations, key=sources.get, reverse=True): #sorts by value number
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

