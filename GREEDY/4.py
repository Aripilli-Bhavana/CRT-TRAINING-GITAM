def event_count(e): #[(1,2),(3,4),(0,6),(5,7),(8,9),(5,9)]
    e.sort(key=lambda x: x[1])  # Sort by end time
    result = [] #[(1,2),(3,4),(5,7),(8,9)]
    et=e[0][1]#2
    result.append(et)
    for p in range(1,len(e)): #(1,6)#(1,2,3,4,5,6)--> (1,2,3,4,5)
        if(e[p][0]>et):
            result.append(e[p])
            et = e[p][1]
    print("Selected events:", result)
    return len(result)

start=[1,3,0,5,8,5]
end=[2,4,6,7,9,9]
e=list(zip(start, end))
c=event_count(e)
print("Maximum number of events that can be attended:", c)