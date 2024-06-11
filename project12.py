with open('project12.txt',encoding="utf8") as f:
    lyrics=f.read()
lyrics=lyrics.lower()
lyrics_list=[]
banned=[' ','.','.',',','?','!','\n']
lyrics_word=''
for w in lyrics:
    if w not in banned:
        lyrics_word += w
    else:
        if lyrics_word:
            lyrics_list.append(lyrics_word)
        lyrics_word=""
from collections import Counter
lyrics_word=Counter(lyrics_list)
print(lyrics_word)