pages = 15
articles = [2,2,3,4]
values = [2,4,4,5]

matrix = [[0 for x in range(pages + 1)] for y in range(len(articles))] 

def maxLearning(i, p):
    if matrix[i][p]:
        return matrix[i][p]
    if i == 0 or p == 0:
        result = 0
    elif (articles[i] * 2) > p:
        result = maxLearning(i -1, p)
    else:
        temp1 = maxLearning(i -1, p)
        temp2 = values[i] + maxLearning(i -1, p - (articles[i] * 2))
        result = max(temp1, temp2)
    matrix[i][p] = result
    return result

print(maxLearning(len(articles) -1, pages))