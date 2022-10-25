
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []
res = []
# ******************************
# Make your Code
# ******************************

# print the words that has 'a', 'r', 'e' in sequence

for word in words:
    idxlst = [word.find(are[j]) for j in range(len(are))]

    if -1 not in idxlst:
        res.append(word)

    idxlst = []

print(res)