with open('file.txt','r') as f1:
    lines = f1.readlines()

lines_to_remove = set()
with open('writehp.txt','w') as f2:
    for i in range(len(lines)):
        if "a" in lines[i]:
            f2.write(lines[i])
            lines_to_remove.add(i)

with open('file.txt','w') as f1:
    for i in range(len(lines)):
        if i not in lines_to_remove:
            f1.write(lines[i])