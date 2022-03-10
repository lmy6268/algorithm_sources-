from collections import Counter
def solution(id_list, report, k):
    total=len(id_list)
    tmp=[[] for i in range(total)] #list for who reported and who got reported 
    tmp2=[0 for i in range(total)] #list for  each user's reported Count 
    answer=[0 for i in range(total)] # list for How many mails about report process each user 

    for i in report:
        content=i.split()
        idx=id_list.index(content[0])
        tmp[idx].append(content[1])

    tmp=[list(set(i)) for i in tmp] # Can report once per a user
    for i in tmp:
        for key in Counter(i):
            idx=id_list.index(key)
            tmp2[idx]+=1
    
    for i in range(total):
        if tmp2[i]>=k:
            for t in range(total):
                if t!=i and id_list[i] in tmp[t]:
                    answer[t]+=1
    return answer

#testCase
id_list =["con", "ryan"]
report =["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3
#get Result
print(solution(id_list, report, k))
