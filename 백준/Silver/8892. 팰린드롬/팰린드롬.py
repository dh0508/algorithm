import sys
def input():
    return sys.stdin.readline()

def is_palindrome(word):
    return word == word[::-1]


T = int(input())
for _ in range(T):
    k = int(input())
    words = [input().strip() for _ in range(k)]
    found = False

    for i in range(k):
        for j in range(k):
            if i != j:
                combined = words[i] + words[j]
                if is_palindrome(combined):
                    print(combined)
                    found = True
                    break
        if found:
            break
    if not found:
        print(0)