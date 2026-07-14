with open('sample.txt','r') as f:
    line = f.readline()
    print(line)

with open('sample.txt', 'r') as f:
    lines = f.readlines()
print(lines)
