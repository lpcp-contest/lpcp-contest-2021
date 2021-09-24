#!/usr/bin/env python3
"""
Example input:

3 2
1 1 1 2
3 3 2 2
3 3 2 1
9
2 5
1 5
1 4
3 1
4 1
5 3
3 5
2 4
3 4
"""
import fileinput #line:22
import re #line:23
import sys #line:24
def pretty_print (O0O0O00OO0O0OOOO0 ,OOO000O0O0O0O0000 ,f =None ,t =None ,n =None ):#line:27
    if len(sys.argv) >= 2 and sys.argv[1] == '--quiet': return
    print (f'#### STEP {O0O0O00OO0O0OOOO0} ####')#line:28
    for O00OOO0OO0O00OOO0 in range (len (OOO000O0O0O0O0000 )):#line:29
        OOO0O00OOO000O0OO =[str (O00O0O000OO0000O0 )for O00O0O000OO0000O0 in OOO000O0O0O0O0000 [O00OOO0OO0O00OOO0 ]]#line:30
        if O00OOO0OO0O00OOO0 ==f :#line:31
            OOO0O00OOO000O0OO .append ('>>>'+f' {OOO000O0O0O0O0000[t][-1]}'*n )#line:32
        elif O00OOO0OO0O00OOO0 ==t :#line:33
            OOO0O00OOO000O0OO .append ('<<<')#line:34
        print (f"{O00OOO0OO0O00OOO0+1}: "+' '.join (OOO0O00OOO000O0OO ))#line:35
    print ()#line:36
filled ,empty =[int (OOOO00OOOOO0OO0OO )for OOOO00OOOOO0OO0OO in input ().split ()]#line:39
bottle =[]#line:40
for _ in range (filled ):#line:41
    bottle .append ([int (OO00OO00OOO0OO0O0 )for OO00OO00OOO0OO0O0 in input ().split ()])#line:42
for _ in range (empty ):#line:43
    bottle .append ([])#line:44
n_pairs =int (input ())#line:46
pairs =[]#line:47
for _ in range (n_pairs ):#line:48
    pairs .append ([int (OO0000OO0OOO0O0O0 )-1 for OO0000OO0OOO0O0O0 in input ().split ()])#line:49
    if pairs [-1 ][0 ]==pairs [-1 ][1 ]:#line:50
        sys .exit (f"Invalid pair: identity ({pairs[-1][0]+1}, {pairs[-1][1]+1}) is not permitted.")#line:51
    if pairs [-1 ][0 ]not in range (len (bottle )):#line:52
        sys .exit (f"Invalid pair: first element of ({pairs[-1][0]+1}, {pairs[-1][1]+1}) is out of range.")#line:53
    if pairs [-1 ][1 ]not in range (len (bottle )):#line:54
        sys .exit (f"Invalid pair: second element of ({pairs[-1][0]+1}, {pairs[-1][1]+1}) is out of range.")#line:55
pretty_print (0 ,bottle )#line:57
for step in range (len (pairs )):#line:58
    f ,t =pairs [step ]#line:59
    if len (bottle [f ])==0 :#line:60
        sys .exit (f"Wrong pair: ({f+1}, {t+1}) but bottle {f+1} is empty.")#line:61
    if len (bottle [t ])==4 :#line:62
        sys .exit (f"Wrong pair: ({f+1}, {t+1}) but bottle {t+1} is full.")#line:63
    if len (bottle [t ])>0 and bottle [t ][-1 ]!=bottle [f ][-1 ]:#line:64
        sys .exit (f"Wrong pair: ({f+1}, {t+1}) but top elements have different colors.")#line:65
    c =bottle [f ][-1 ]#line:66
    n =0 #line:67
    while bottle [f ]and bottle [f ][-1 ]==c and len (bottle [t ])<4 :#line:68
        bottle [t ].append (bottle [f ].pop ())#line:69
        n +=1 #line:70
    pretty_print (step +1 ,bottle ,f ,t ,n )#line:71
for i in range (len (bottle )):#line:73
    b =bottle [i ]#line:74
    if len (b )==0 :#line:75
        continue #line:76
    if len (b )==4 and all (O0OO0O0OOOO0O0000 ==b [0 ]for O0OO0O0OOOO0O0000 in b ):#line:77
        continue #line:78
    sys .exit (f"Wrong final state: bottle {i+1} is neither empty nor filled with the same color.")#line:79
print ("CORRECT!")
