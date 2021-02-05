def letterPos(w, x):

    count = 0
    for i in range(0,len(w)+ 1):
        if w[i- 1] == x:
            count = i
            return count
    else:
        return "none"
    

print(letterPos("sunshine", "n"))