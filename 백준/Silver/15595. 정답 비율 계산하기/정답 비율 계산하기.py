import sys
def input():
    return sys.stdin.readline()


n = int(input())
correct_users_count = 0
total_wrong_attempts = 0
user_attempts = {}
solved_users = set()

for _ in range(n):
    data = input().strip().split()
    user_id = data[1]
    result = data[2]

    if user_id == 'megalusion':
        continue

    if user_id not in user_attempts:
        user_attempts[user_id] = 0

    if result == '4':
        if user_id not in solved_users:
            solved_users.add(user_id)
            correct_users_count += 1
            total_wrong_attempts += user_attempts[user_id]
    else:
        if user_id not in solved_users:
            user_attempts[user_id] += 1

if correct_users_count == 0:
    print(0)
else:
    print((correct_users_count / (correct_users_count + total_wrong_attempts)) * 100)
