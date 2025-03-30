import sys
def input():
    return sys.stdin.readline()


d = {"CU":"see you",
     ":-)":"I’m happy",
     ":-(":"I’m unhappy",
     ";-)":	"wink",
     ":-P":"stick out my tongue",
     "(~.~)":"sleepy",
     "TA":"totally awesome",
     "CCC":"Canadian Computing Competition",
     "CUZ":"because",
     "TY":"thank-you",
     "YW":"you're welcome",
     "TTYL":"talk to you later"}
while True:
    a = str(input().strip())
    try:
        print(d[a])
    except:
        print(a)
    if a == "TTYL":
        break