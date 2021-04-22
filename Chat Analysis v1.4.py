import re
import functools
import operator

import emoji

file=open('chat.txt',encoding="utf8")
op = open('output.txt','w')


p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29=dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict(),dict()
#currently supports up to 30 participants, add more dictionaries (p30,p31....) to increase capacity
#and add to list below
ppld=[p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29]

ppl=dict()  # dictionary of participants

people=list()  # list of participants

for line in file:
    line=line.rstrip()           # for chats exported from apple devices, this will need some modification,
    line=line.split(' - ')       # try replacing ' - ' with ']
    try:
        remtime=line[1]         # removes time stamp
    except:
        continue
    msg=remtime.split(': ')     # seperates messages from senders
    try: (sender,text)=msg[0],msg[1]
    except: continue
    ppl[sender]=ppl.get(sender,0)+1     # counts number of messages per participant
    people=list(ppl)
    for word in words:       # to obtain most  common words that messages start with, set word=words[0].lower
                word=word.lower()    # converts all words to lovercase eg. to prevent Hi and hi from being counted as distinct
                if len(word)>0:      # if you want a minimum character count to words, set this as that number, otherwise 0
                    ppld[i][word]=ppld[i].get(word,0)+1

                # to obtain most  common words that messages start with, uncomment the below loop and comment the for loop above
                # word=words[0].lower()
                # if len(word)>0:      # if you want a minimum character count to words, set this as that number, otherwise 0
                #     ppld[i][word]=ppld[i].get(word,0)+1


# arranging the information #
n=10                        # number of results desired per participant
tmp=list()
op.write(str(ppl))              # prints list of participants
op.write('\n')
for i in range(len(people)):
    tmp.clear()
    op.write('\n')
    op.write(str(people[i]))    # prints participant name
    op.write('\n')
    tmp = list()
    for k,v in ppld[i].items():
        newtup=(v,k)
        tmp.append(newtup)
    tmp=sorted(tmp, reverse=True)
    for v,k in tmp[:n]:
        try:
            op.write(str(k))    # prints the count of how many times the word was used
            op.write(':')
            op.write(str(v))    # prints the word
            op.write('\n')
        except:
            continue
