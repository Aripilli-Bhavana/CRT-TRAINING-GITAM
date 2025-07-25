def sub_array_sum(l,target):
    result =[]
    def bt(start,path,total):
        if(total==target):
            result.append(path[:])
            print(result)
            return
        if(total>target):
            return
        for p in range(start, len(l)):
            path.append(l[p])
            bt(p+1,path,total+l[p])
            path.pop()
    bt(0,[],0)
    return result
l=[3,4,5,2]
target=9
r=sub_array_sum(l,target)
print(r)