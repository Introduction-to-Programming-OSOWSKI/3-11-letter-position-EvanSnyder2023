def letterPos(w, x):

    word = 0
    for i in range(0, len(w)):
        if w[i] == x:
            word = i + 1
            return word
    else:
        return "none"
    

print(letterPos("cea", "a"))