def divisibleSumPairs(n, k, ar):
    count = 0 
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i < j:
                suma = ar[i] + ar[j]
                if suma % k == 0:
                    count+=1