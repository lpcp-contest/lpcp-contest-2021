#!/usr/bin/env python3
"""
Example input:

5 2
1 2 3 4
5 3 2 2
4 3 1 5
4 3 4 5
1 5 2 1
20
2 6
2 6
2 7
4 2
1 4
1 7
1 6
5 1
6 5
3 2
3 1
3 7
4 3
4 3
5 6
5 6
5 2
4 7
5 1
4 3
"""
import fileinput #line:35
import re #line:36
import sys #line:37
def pretty_print (OOO0O0O000OO0O0OO ,OOOOO00O0O0OO00OO ,f =None ,t =None ):#line:40
    if len(sys.argv) >= 2 and sys.argv[1] == '--quiet': return
    print (f'#### STEP {OOO0O0O000OO0O0OO} ####')#line:41
    for OO0OO000O0OO00OOO in range (len (OOOOO00O0O0OO00OO )):#line:42
        O0OO00O00O0OO000O =[str (OO0OOO0O0O00O0O0O )for OO0OOO0O0O00O0O0O in OOOOO00O0O0OO00OO [OO0OO000O0OO00OOO ]]#line:43
        if OO0OO000O0OO00OOO ==f :#line:44
            O0OO00O00O0OO000O .append (f'>>> {OOOOO00O0O0OO00OO[t][-1]}')#line:45
        elif OO0OO000O0OO00OOO ==t :#line:46
            O0OO00O00O0OO000O .append ('<<<')#line:47
        print (f"{OO0OO000O0OO00OOO+1}: "+' '.join (O0OO00O00O0OO000O ))#line:48
    print ()#line:49
filled ,empty =[int (O0O0OOO0OO0O0OOO0 )for O0O0OOO0OO0O0OOO0 in input ().split ()]#line:51
bottle =[]#line:52
for _ in range (filled ):#line:53
    bottle .append ([int (OO0000OO0O0OO0O0O )for OO0000OO0O0OO0O0O in input ().split ()])#line:54
for _ in range (empty ):#line:55
    bottle .append ([])#line:56
n_pairs =int (input ())#line:58
pairs =[]#line:59
for _ in range (n_pairs ):#line:60
    pairs .append ([int (O0O0O0OO0O0O0OO00 )-1 for O0O0O0OO0O0O0OO00 in input ().split ()])#line:61
    if pairs [-1 ][0 ]==pairs [-1 ][1 ]:#line:62
        sys .exit (f"Invalid pair: identity ({pairs[-1][0]+1}, {pairs[-1][1]+1}) is not permitted.")#line:63
    if pairs [-1 ][0 ]not in range (len (bottle )):#line:64
        sys .exit (f"Invalid pair: first element of ({pairs[-1][0]+1}, {pairs[-1][1]+1}) is out of range.")#line:65
    if pairs [-1 ][1 ]not in range (len (bottle )):#line:66
        sys .exit (f"Invalid pair: second element of ({pairs[-1][0]+1}, {pairs[-1][1]+1}) is out of range.")#line:67
pretty_print (0 ,bottle )#line:69
for step in range (len (pairs )):#line:70
    f ,t =pairs [step ]#line:71
    if len (bottle [f ])==0 :#line:72
        sys .exit (f"Wrong pair: ({f+1}, {t+1}) but bottle {f+1} is empty.")#line:73
    if len (bottle [t ])==4 :#line:74
        sys .exit (f"Wrong pair: ({f+1}, {t+1}) but bottle {t+1} is full.")#line:75
    if len (bottle [t ])>0 and bottle [t ][-1 ]!=bottle [f ][-1 ]:#line:76
        sys .exit (f"Wrong pair: ({f+1}, {t+1}) but top elements have different colors.")#line:77
    bottle [t ].append (bottle [f ].pop ())#line:78
    pretty_print (step +1 ,bottle ,f ,t )#line:79
for i in range (len (bottle )):#line:81
    b =bottle [i ]#line:82
    if len (b )==0 :#line:83
        continue #line:84
    if len (b )==4 and all (O0OO0OOO000O0O0O0 ==b [0 ]for O0OO0OOO000O0O0O0 in b ):#line:85
        continue #line:86
    sys .exit (f"Wrong final state: bottle {i+1} is neither empty nor filled with the same color.")#line:87
print ("CORRECT!")
