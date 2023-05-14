d = {}
for s in open("table.txt", "r").read().split(","):
    k, v = s.split(":")
    d[k] = v

print(d)