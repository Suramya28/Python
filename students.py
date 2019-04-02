students = {
            "Alice": {"id": "ID0001", "age":26, "grade":"A"},
            "Bob": {"id": "ID0002", "age":27, "grade":"B"},
            "Claire": {"id": "ID0003", "age":17, "grade":"C"},
            "Dan": {"id": "ID0004", "age":21, "grade":"D"},
            "Emma":{"id": "ID0005", "age":22, "grade":"E"}
            }

students2 = {
            "Alice": {"id": "ID0001", "age":26, "grade":"A"},
            "Bob": {"id": "ID0002", "age":27, "grade":"B"},
            "Claire": {"id": "ID0003", "age":17, "grade":"C"},
            "Dan": {"id": "ID0004", "age":21, "grade":"D"},
            "Emma":{"id": "ID0005", "age":22, "grade":"E"}
            }

print(students["Dan"]["age"])

print(students["Emma"]["id"], students["Emma"]["grade"])


s1=['ax','by']
s2=['cz']

s3=zip(*zip(students,students2))
print(list(s3))

for i in range(5):
    print(i)

di=students["Alice"]
print(di)




y=dict(x=5, y=0)

print(y)
