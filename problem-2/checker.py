#!/usr/bin/env python3
"""
Example input:

5 6
1 1 1 2 3
4 3 1 3 3
5 4 5 2 5
1 6 6 2 6
5 5 5 4 2
11
4 4 5 5
4 2 4 5
2 1 5 4
1 5 2 4
3 1 3 3
1 1 1 3
2 3 4 1
2 2 2 5
3 5 5 3
1 4 3 4
5 1 5 2
"""
import fileinput #line:26
import re #line:27
import sys #line:28
def pretty_print (OOO00OO000OO0O00O ,OOOOO000OO00OO0OO ,cut =None ):#line:31
    if len(sys.argv) >= 2 and sys.argv[1] == '--quiet': return
    if cut is None :#line:32
        cut =[]#line:33
    print (f'#### STEP {OOO00OO000OO0O00O} ####')#line:34
    for OO0OO0O00OOO0OO00 in range (1 ,len (OOOOO000OO00OO0OO )):#line:35
        OO0OO0O000O00O00O =[]#line:36
        for O0OO0OOOOO0000000 in range (1 ,len (OOOOO000OO00OO0OO [OO0OO0O00OOO0OO00 ])):#line:37
            O0000O00O000OO0O0 =OOOOO000OO00OO0OO [OO0OO0O00OOO0OO00 ][O0OO0OOOOO0000000 ]if OOOOO000OO00OO0OO [OO0OO0O00OOO0OO00 ][O0OO0OOOOO0000000 ]!=0 else '.'#line:38
            if (OO0OO0O00OOO0OO00 ,O0OO0OOOOO0000000 )in cut :#line:39
                OO0OO0O000O00O00O .append (f"[{O0000O00O000OO0O0}]")#line:40
            else :#line:41
                OO0OO0O000O00O00O .append (f" {O0000O00O000OO0O0} ")#line:42
        print (''.join (OO0OO0O000O00O00O ))#line:43
    print ()#line:44
def inline (O0O0000O0O0OO00OO ,OO0000O00O0OO0OOO ):#line:47
    if O0O0000O0O0OO00OO [0 ]==OO0000O00O0OO0OOO [0 ]:#line:48
        return True #line:49
    if O0O0000O0O0OO00OO [1 ]==OO0000O00O0OO0OOO [1 ]:#line:50
        return True #line:51
    return abs (O0O0000O0O0OO00OO [0 ]-OO0000O00O0OO0OOO [0 ])==abs (O0O0000O0O0OO00OO [1 ]-OO0000O00O0OO0OOO [1 ])#line:52
size ,colors =[int (OOOO0OOO00OO0000O )for OOOO0OOO00OO0000O in input ().split ()]#line:55
grid =[[]]#line:57
for _ in range (size ):#line:58
    grid .append ([0 ]+[int (OOO00OO000OO0O000 )for OOO00OO000OO0O000 in input ().split ()])#line:59
n_pairs =int (input ())#line:62
pairs =[]#line:63
for _ in range (n_pairs ):#line:64
    p =[int (OOOOOOO00O000O0O0 )for OOOOOOO00O000O0O0 in input ().split ()]#line:65
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
        y =f [1 ]#line:100
        dy =1 if f [1 ]<t [1 ]else -1 #line:101
        for x in range (min (f [0 ],t [0 ])+1 ,max (f [0 ],t [0 ])):#line:102
            y +=dy #line:103
            if grid [x ][y ]not in (0 ,grid [f [0 ]][f [1 ]]):#line:104
                sys .exit (f"Wrong pair: ({f}, {t}) but ({x}, {y}) has different color.")#line:105
            else :#line:106
                cut .append ((x ,y ))#line:107
    pretty_print (step +1 ,grid ,cut )#line:109
    for (x ,y )in cut :#line:110
        grid [x ][y ]=0 #line:111
for i in range (1 ,len (grid )):#line:113
    for j in range (1 ,len (grid [i ])):#line:114
        if grid [i ][j ]!=0 :#line:115
            sys .exit (f"Wrong final state: button on ({i}, {j}).")#line:116
print ("CORRECT!")
