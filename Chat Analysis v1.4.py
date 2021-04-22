import re
import functools
import operator

import emoji

file=open('chat.txt',encoding="utf8")
op = open('output.txt','w')
#text=file.read()
#text=demoji.replace(txt)

p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29=dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict()

ppld=[p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29]

ppl=dict()

people=list()
#print(text)

#print(file)

for line in file:
    line=line.rstrip()
    line=line.split(' - ')
    #print((line))
    try:
        remtime=line[1]
    except:
        continue
    msg=remtime.split(': ')
    try: (sender,text)=msg[0],msg[1]
    except: continue
    ppl[sender]=ppl.get(sender,0)+1
    people=list(ppl)
    for i in range(len(people)):
        if '<Media' in text: continue
        elif people[i] in sender:
            em_split_emoji = emoji.get_emoji_regexp().split(text)
            em_split_whitespace = [substr.split() for substr in em_split_emoji]
            words = functools.reduce(operator.concat, em_split_whitespace)
            word=words[0].lower()
            ppld[i][word]=ppld[i].get(word,0)+1

n=10
tmp=list()
op.write(str(ppl))
op.write('\n')
for i in range(len(people)):
    tmp.clear()
    op.write('\n')
    op.write(str(people[i]))
    op.write('\n')
    tmp = list()
    for k,v in ppld[i].items():
        newtup=(v,k)
        tmp.append(newtup)
    tmp=sorted(tmp, reverse=True)
    for v,k in tmp[:n]:
        try:
            op.write(str(k))
            op.write(':')
            op.write(str(v))
            op.write('\n')
        except:
            continue
