from collections import defaultdict

def chainedWords(words):
    # Fill this in.
    word = defaultdict(list)
    for i in range(len(words)):
        for j in range(len(words)):
            if i == j:
                continue
            else:
                if words[j][0] == words[i][-1]:
                    word[words[i]].append(words[j])
    print(word)
    for a in words:
        if a in str(word.values()):
            continue
        else:
            return False
    return True

print(chainedWords(['apple', 'eggs', 'snack', 'karat', 'tuna']))
# True
