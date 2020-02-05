import csv
import matplotlib.pyplot as plt

def sort_dict(dictionary):
	x = zip(dictionary.values(), dictionary.keys())
	y = list(x)
	z = sorted(y, reverse=True)
	return z

groups = []

with open('top10_history.csv', 'r') as f:
	reader = csv.reader(f)
	for i, value in enumerate(reader):
		num = int(len(value)/3)
		if i > 0:
			groups_copy = value
			for i in range(num):				
				group = groups_copy[0:3]
				groups.append(group)
				groups_copy = groups_copy[3:]

count = dict()

for i in groups:
	if i[1] in count.keys():
		count[i[1]] += 1
	else:
		count[i[1]] = 1


result = sort_dict(count)
xticks = []
total_num = []

for i in result:
	total_num.append(i[0])
	xticks.append(i[1])

print(total_num)
print(xticks)

plt.bar(xticks[0: 20], height=total_num[0: 20])
plt.xticks(xticks[0: 20], rotation=60)
plt.savefig('top20', dpi=150)



