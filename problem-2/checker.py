#!/usr/bin/env python3
"""
Example input:

3
20 11 21
41 41 10
32 52 22
15
1 1
1 1
1 1
1 2
1 3
1 3
1 3
2 1
2 1
2 3
3 1
3 1
3 3
3 3
3 3
"""
import fileinput #line:26
import re #line:27
import sys #line:28
def pretty_print (O0000OO00OO0O00O0 ,OO0O0OO0OOOO000O0 ,cut =None ):#line:31
    if cut is None :#line:32
        cut =[]#line:33
    print (f'#### STEP {O0000OO00OO0O00O0} ####')#line:34
    for OOO0O0O0000OOO0OO in range (1 ,len (OO0O0OO0OOOO000O0 )):#line:35
        O0OOO000OOOOO0O0O =[]#line:36
        for O00O000000O00O000 in range (1 ,len (OO0O0OO0OOOO000O0 [OOO0O0O0000OOO0OO ])):#line:37
            OO0000O0OO000OOOO =OO0O0OO0OOOO000O0 [OOO0O0O0000OOO0OO ][O00O000000O00O000 ]if OO0O0OO0OOOO000O0 [OOO0O0O0000OOO0OO ][O00O000000O00O000 ]!=0 else '.'#line:38
            if (OOO0O0O0000OOO0OO ,O00O000000O00O000 )in cut :#line:39
                O0OOO000OOOOO0O0O .append (f"[{OO0000O0OO000OOOO}]")#line:40
            else :#line:41
                O0OOO000OOOOO0O0O .append (f" {OO0000O0OO000OOOO} ")#line:42
        print (''.join (O0OOO000OOOOO0O0O ))#line:43
    print ()#line:44
def inline (O0O0O00000O000OO0 ,OO00O0OOO0OOO0OOO ):#line:47
    if O0O0O00000O000OO0 [0 ]==OO00O0OOO0OOO0OOO [0 ]:#line:48
        return True #line:49
    if O0O0O00000O000OO0 [1 ]==OO00O0OOO0OOO0OOO [1 ]:#line:50
        return True #line:51
    return abs (O0O0O00000O000OO0 [0 ]-OO00O0OOO0OOO0OOO [0 ])==abs (O0O0O00000O000OO0 [1 ]-OO00O0OOO0OOO0OOO [1 ])#line:52
size ,colors =[int (OOO0O000000000000 )for OOO0O000000000000 in input ().split ()]#line:55
grid =[[]]#line:57
for _ in range (size ):#line:58
    grid .append ([0 ]+[int (O000O00OO0OO0000O )for O000O00OO0OO0000O in input ().split ()])#line:59
n_pairs =int (input ())#line:62
pairs =[]#line:63
for _ in range (n_pairs ):#line:64
    p =[int (O0OO00O0OOOO0O00O )for O0OO00O0OOOO0O00O in input ().split ()]#line:65
    pairs .append (((p [0 ],p [1 ]),(p [2 ],p [3 ])))#line:66
    if pairs [-1 ][0 ]==pairs [-1 ][1 ]:#line:67
        sys .exit (f"Invalid pair: identity ({pairs[-1][0]}, {pairs[-1][1]}) is not permitted.")#line:68
    if pairs [-1 ][0 ][0 ]not in range (1 ,len (grid ))or pairs [-1 ][0 ][1 ]not in range (1 ,len (grid )):#line:69
        sys .exit (f"Invalid pair: first element of ({pairs[-1][0]}, {pairs[-1][1]}) is out of range.")#line:70
    if pairs [-1 ][1 ][0 ]not in range (1 ,len (grid ))or pairs [-1 ][1 ][1 ]not in range (1 ,len (grid )):#line:71
        sys .exit (f"Invalid pair: second element of ({pairs[-1][0]}, {pairs[-1][1]}) is out of range.")#line:72
    if not inline (pairs [-1 ][0 ],pairs [-1 ][1 ]):#line:73
        sys .exit (f"Invalid pair: ({pairs[-1][0]}, {pairs[-1][1]}) is not an horizontal, vertical or diagonal line.")#line:74
pretty_print (0 ,grid )#line:76
for step in range (len (pairs )):#line:77
    f ,t =pairs [step ]#line:78
    if grid [f [0 ]][f [1 ]]==0 :#line:79
        sys .exit (f"Wrong pair: ({f}, {t}) but no button on {f}.")#line:80
    if grid [t [0 ]][t [1 ]]==0 :#line:81
        sys .exit (f"Wrong pair: ({f}, {t}) but no button on {t}.")#line:82
    if grid [f [0 ]][f [1 ]]!=grid [t [0 ]][t [1 ]]:#line:83
        sys .exit (f"Wrong pair: ({f}, {t}) but {f} and {t} have different colors.")#line:84
    cut =[f ,t ]#line:86
    if f [0 ]==t [0 ]:#line:87
        for x in range (min (f [1 ],t [1 ])+1 ,max (f [1 ],t [1 ])):#line:88
            if grid [f [0 ]][x ]not in (0 ,grid [f [0 ]][f [1 ]]):#line:89
                sys .exit (f"Wrong pair: ({f}, {t}) but ({f[0]}, {x}) has different color.")#line:90
            else :#line:91
                cut .append ((f [0 ],x ))#line:92
    elif f [1 ]==t [1 ]:#line:93
        for x in range (min (f [0 ],t [0 ])+1 ,max (f [0 ],t [0 ])):#line:94
            if grid [x ][f [1 ]]not in (0 ,grid [f [0 ]][f [1 ]]):#line:95
                sys .exit (f"Wrong pair: ({f}, {t}) but ({x}, {f[1]}) has different color.")#line:96
            else :#line:97
                cut .append ((x ,f [1 ]))#line:98
    else :#line:99
        x =f [0 ]#line:100
        y =f [1 ]#line:101
        dx =1 if f [0 ]<t [0 ]else -1 #line:102
        dy =1 if f [1 ]<t [1 ]else -1 #line:103
        for _ in range (min (f [0 ],t [0 ])+1 ,max (f [0 ],t [0 ])):#line:104
            x +=dx #line:105
            y +=dy #line:106
            if grid [x ][y ]not in (0 ,grid [f [0 ]][f [1 ]]):#line:107
                sys .exit (f"Wrong pair: ({f}, {t}) but ({x}, {y}) has different color.")#line:108
            else :#line:109
                cut .append ((x ,y ))#line:110
    pretty_print (step +1 ,grid ,cut )#line:112
    for (x ,y )in cut :#line:113
        grid [x ][y ]=0 #line:114
for i in range (1 ,len (grid )):#line:116
    for j in range (1 ,len (grid [i ])):#line:117
        if grid [i ][j ]!=0 :#line:118
            sys .exit (f"Wrong final state: button on ({i}, {j}).")#line:119
print ("CORRECT!")