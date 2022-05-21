filein = open("prompt_wildcards.txt", 'r')
wildcards = []
for line in filein:
    if line == "\n":
        continue
    wildcards.append(line.strip())
filein.close()

wildcards = sorted(wildcards, key=str.casefold)

fileout = open("prompt_wildcards.txt", 'w')
fileout.write("\n".join(wildcards))
fileout.close()
