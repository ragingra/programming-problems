pages = 15

articles = [2,2,3,4]

values = [2,4,4,5]

def maxLearning(i, p):
    if i == 0 or p == 0:
        return 0
    elif (articles[i] * 2) > p:
        return maxLearning(i -1, p)
    else:
        temp1 = maxLearning(i -1, p)
        temp2 = values[i] + maxLearning(i -1, p - (articles[i] * 2))
        return max(temp1, temp2)
    

print(maxLearning(len(articles) -1, pages))