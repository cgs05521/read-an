
sum_lan = 0
data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f :
		data.append(line)

for d in data:
	sum_lan += len(d)

print('留言平均長度為：',sum_lan/len(data),'筆資料')


