A = [6,5,3,-100,5,1,4]
st = 'hello, world'

ivan = {
	"name" : "ivan" ,
	"age" : 34,
	"children" : [{
	"name" : "vasja" ,
	"age" : 12,
	}, {
	"name" : "petja" ,
	"age" : 10,
	}],
}
darja = {
	"name" : "darja" ,
	"age" : 41,
	"children" : [{
	"name" : "kirill" ,
	"age" : 21,
	}, {
	"name" : "pavel" ,
	"age" : 15,
	}],
}
emps = [ivan, darja]

#for i in range(len(A)):
#    print(A[i])
print('min(YourMassive):')
#print(min(A))
m = 0
i = 1

while i < len(A):
    if A[i] < A[m]:
        m = i
    i += 1

print (A[m])

print('\n')

def srednee(lst):
   return (sum(lst)) / len(lst)

print('srednee(YourMassive):')
print(srednee(A))

def reverse(st):
    out1 = st[::-1]
    print(out1)

print('\n')
print('your reverse string:')
reverse(st)

def filter_children(emps1):
	filter1 = []
	for i in emps1:
		for j in i['children']:
			if j['age'] > 18:
				filter1.append(i['name'])
				break
	return filter1

print('\n')
print('yourSearchWorker(s):')
print(filter_children(emps))