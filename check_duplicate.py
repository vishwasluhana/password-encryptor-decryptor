words =  open("result.txt","r")
seen = set()
dups = set()
for word in words.read().split("\""):
    if len(word) == 5:
        if word in seen:
            if word not in dups:
                print(word)
                dups.add(word)
        else:
            seen.add(word)
    else: continue
