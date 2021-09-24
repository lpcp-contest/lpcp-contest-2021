#!/usr/bin/env python3
"""
Example input:

4 3 3
0 1 0 0
0 0 0 1
1 0 0 0
0 1 0 0
11
4 3
4 4
4 1
2 1
1 1
1 3
1 4
3 4
3 2
2 2
2 3
"""
import fileinput #line:25
import re #line:26
import sys #line:27
def pretty_print (O00OOOO00OOOO00O0 ,OOO0OOOOO000O0O00 ,OOO00O0OO0OO0OO00 ,OOO0000OOOO00O0OO ):#line:30
    if len(sys.argv) >= 2 and sys.argv[1] == '--quiet': return
    print (f'#### STEP {O00OOOO00OOOO00O0} ####')#line:31
    for OOO0O0OO000OO00OO in range (len (OOO0OOOOO000O0O00 )):#line:32
        OOOOOO0O0OO0O0OO0 =[]#line:33
        for OO00OO0000OOOO00O in range (len (OOO0OOOOO000O0O00 [OOO0O0OO000OO00OO ])):#line:34
            O00OOOOO0OOOO0000 =OOO0OOOOO000O0O00 [OOO0O0OO000OO00OO ][OO00OO0000OOOO00O ]#line:35
            if O00OOOOO0OOOO0000 ==1 :#line:36
                OOOOOO0O0OO0O0OO0 .append ('\U0001F9F1')#line:37
            elif OOO00O0OO0OO0OO00 ==OOO0O0OO000OO00OO and OOO0000OOOO00O0OO ==OO00OO0000OOOO00O :#line:38
                OOOOOO0O0OO0O0OO0 .append (f'\U0001F438')#line:39
            elif O00OOOOO0OOOO0000 ==0 :#line:40
                OOOOOO0O0OO0O0OO0 .append ('\U0001F99F')#line:41
            else :#line:42
                assert O00OOOOO0OOOO0000 ==-1 #line:43
                OOOOOO0O0OO0O0OO0 .append ('\U0001F4A9')#line:44
        print (''.join (OOOOOO0O0OO0O0OO0 ))#line:45
    if O00OOOO00OOOO00O0 ==0 :#line:46
        print (f'=> start  at ({OOO00O0OO0OO0OO00+1}, {OOO0000OOOO00O0OO+1})')#line:47
    else :#line:48
        print (f'=> jumped to ({OOO00O0OO0OO0OO00+1}, {OOO0000OOOO00O0OO+1})')#line:49
    print ()#line:50
size ,fi ,fj =[int (OO00O0OO0OOOOO0OO )for OO00O0OO0OOOOO0OO in input ().split ()]#line:53
grid =[]#line:55
for _ in range (size ):#line:56
    grid .append ([int (OO0O0O0O0000OO000 )for OO0O0O0O0000OO000 in input ().split ()])#line:57
n_arcs =int (input ())#line:59
arcs =[]#line:60
for _ in range (n_arcs ):#line:61
    arcs .append ([int (O00OO00O0O000OO0O )-1 for O00OO00O0O000OO0O in input ().split ()])#line:62
    if arcs [-1 ][0 ]not in range (size )or arcs [-1 ][1 ]not in range (size ):#line:63
        sys .exit (f"Wrong step: ({arcs[-1][0]+1}, {arcs[-1][1]+1}) is out of range.")#line:64
    if grid [arcs [-1 ][0 ]][arcs [-1 ][1 ]]==1 :#line:65
        sys .exit (f"Wrong step: ({arcs[-1][0]+1}, {arcs[-1][1]+1}) is a wall.")#line:66
    if arcs [-1 ]in arcs [:-1 ]:#line:67
        sys .exit (f"Wrong step: ({arcs[-1][0]+1}, {arcs[-1][1]+1}) was already visited.")#line:68
fi -=1 #line:70
fj -=1 #line:71
pretty_print (0 ,grid ,fi ,fj )#line:72
for step in range (n_arcs ):#line:73
    grid [fi ][fj ]=-1 #line:74
    fi ,fj =arcs [step ]#line:75
    if grid [fi ][fj ]==1 :#line:76
        sys .exit (f"Wrong step: ({fi+1}, {fj+1}) is a wall.")#line:77
    if grid [fi ][fj ]==-1 :#line:78
        sys .exit (f"Wrong step: ({fi+1}, {fj+1}) was already visited.")#line:79
    pretty_print (step +1 ,grid ,fi ,fj )#line:80
grid [fi ][fj ]=-1 #line:81
for i in range (len (grid )):#line:83
    for j in range (len (grid )):#line:84
        if grid [i ][j ]==0 :#line:85
            sys .exit (f"Cell ({i+1}, {j+1}) was not visited.")#line:86
print ("CORRECT!")
