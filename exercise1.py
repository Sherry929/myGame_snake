
b = {
'Adam': 95,
'Lisa': 85,
'Bart': 59
}

def adata(list):
    if len(list) == 0:
        print("The list length is empty !!!")
        return
    data = {}
    for i, v in enumerate(list):
        uid = v["userid"]
        if data.has_key(uid):
            data[uid].append(list[i])
        else:
            lists = []
            lists.append(list[i])
            data[uid] = lists
    return data
adata(list=b)
"""
list1=[1,2,3,4,5]
for i in enumerate(list1):
    print(i)
"""