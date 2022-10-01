import random

new_tests = []
for i in range(10):
    min_value = random.randint(-1000,-1)
    max_value = random.randint(0,1000)
    new_list = [random.randint(min_value,max_value) for x in range(min_value,max_value)]
    new_tests.append(new_list)
with open("tests.txt","a") as f:
    for test in new_tests:
        f.writelines(f"{','.join(str(e) for e in test)} {random.randint(min_value,max_value)}\n")