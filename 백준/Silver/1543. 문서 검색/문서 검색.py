doc_s = input()
find_s = input()
cnt = 0
i = 0
while(i < len(doc_s)):
    if doc_s[i:i+len(find_s)] == find_s:
        cnt  += 1
        i += len(find_s)
    else:
        i += 1
print(cnt)