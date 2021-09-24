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
import fileinput #line:28
import re #line:29
import sys #line:30
sym ={10 :'\u2500',11 :'\u2502',20 :'\u256E',21 :'\u256F',22 :'\u2570',23 :'\u256D',30 :'\u2576',31 :'\u2577',32 :'\u2574',33 :'\u2575',50 :'\u252C',51 :'\u2524',52 :'\u2534',53 :'\u251C',}#line:48
def pretty_print (OO0OOO00O00O00OOO ,OO0O0O00OO00O0O00 ,cut =None ):#line:51
    if len(sys.argv) >= 2 and sys.argv[1] == '--quiet': return
    if cut is None :#line:52
        cut =[]#line:53
    print (f'#### STEP {OO0OOO00O00O00OOO} ####')#line:54
    for OO000O00O00O00OO0 in range (len (OO0O0O00OO00O0O00 )):#line:55
        OOO00O000000OO0O0 =[]#line:56
        for O00O0OOOO000O0O0O in range (len (OO0O0O00OO00O0O00 [OO000O00O00O00OO0 ])):#line:57
            OOO00O000000OO0O0 .append (sym [OO0O0O00OO00O0O00 [OO000O00O00O00OO0 ][O00O0OOOO000O0O0O ]])#line:58
        print (''.join (OOO00O000000OO0O0 ))#line:59
    print ()#line:60
def inline (OOO0O00O0O0OO000O ,OO0O0OO0OOO0O0OO0 ):#line:63
    if OOO0O00O0O0OO000O [0 ]==OO0O0OO0OOO0O0OO0 [0 ]:#line:64
        return True #line:65
    if OOO0O00O0O0OO000O [1 ]==OO0O0OO0OOO0O0OO0 [1 ]:#line:66
        return True #line:67
    return abs (OOO0O00O0O0OO000O [0 ]-OO0O0OO0OOO0O0OO0 [0 ])==abs (OOO0O00O0O0OO000O [1 ]-OO0O0OO0OOO0O0OO0 [1 ])#line:68
size =int (input ())#line:72
grid =[]#line:74
for _ in range (size ):#line:75
    grid .append ([int (OOOO0000OOO0O0O00 )for OOOO0000OOO0O0O00 in input ().split ()])#line:76
n_rotations =int (input ())#line:79
rotations =[]#line:80
for _ in range (n_rotations ):#line:81
    rotations .append ([int (O0O00000O00OOOO0O )for O0O00000O00OOOO0O in input ().split ()])#line:82
    if rotations [-1 ][0 ]-1 not in range (len (grid ))or rotations [-1 ][1 ]-1 not in range (len (grid )):#line:83
        sys .exit (f"Invalid rotation: {rotations[-1]} is out of range.")#line:84
pretty_print (0 ,grid )#line:86
for step in range (len (rotations )):#line:87
    i ,j =rotations [step ]#line:88
    grid [i -1 ][j -1 ]+=1 #line:89
    if grid [i -1 ][j -1 ]==12 :#line:90
        grid [i -1 ][j -1 ]=10 #line:91
    elif grid [i -1 ][j -1 ]%10 ==4 :#line:92
        grid [i -1 ][j -1 ]-=4 #line:93
    pretty_print (step +1 ,grid )#line:94
connections ={'left':[10 ,20 ,21 ,32 ,50 ,51 ,52 ],'right':[10 ,22 ,23 ,30 ,50 ,52 ,53 ],'up':[11 ,21 ,22 ,33 ,51 ,52 ,53 ],'down':[11 ,20 ,23 ,31 ,50 ,51 ,53 ],}#line:102
seen =set ()#line:104
stack =[(0 ,0 ,'nil')]#line:105
while stack :#line:106
    i ,j ,d =stack .pop ()#line:107
    if i not in range (size )or j not in range (size ):#line:109
        sys .exit (f"Water on ({i+1}, {j+1}), out of grid!")#line:110
    if d !='nil'and grid [i ][j ]not in connections [d ]:#line:112
        sys .exit (f"Wrong connection on ({i+1}, {j+1})")#line:113
    if (i ,j )in seen :#line:115
        continue #line:116
    seen .add ((i ,j ))#line:117
    if grid [i ][j ]in connections ['left']:#line:119
        stack .append ((i ,j -1 ,'right'))#line:120
    if grid [i ][j ]in connections ['right']:#line:121
        stack .append ((i ,j +1 ,'left'))#line:122
    if grid [i ][j ]in connections ['up']:#line:123
        stack .append ((i -1 ,j ,'down'))#line:124
    if grid [i ][j ]in connections ['down']:#line:125
        stack .append ((i +1 ,j ,'up'))#line:126
print ("CORRECT!")