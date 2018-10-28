import random
def custom_roommate(me, others):
    students= others
    for i in range(0,5):
        results=[]
        active_user_ans = me[i]
        for s in students:
            s_ans=s[i]
            diff = abs(active_user_ans - s_ans)
            similarity_score=pow(2,-diff)
            results.append((s,similarity_score))
        results.sort(key=(lambda x:x[1]), reverse=True)
        if len(results)<3:
            students=[x[0] for x in results[:len(results)]]
        else:
            students=[x[0] for x in results[:len(results)//2]]
        return students[:5]

others=[[random.randint(1,4) for j in range(0,5)] for i in range(0,50)]
me=[2,3,3,1,1]
ans=custom_roommate(me,others)
print(me,"\n")
for line in ans:
    print(line)