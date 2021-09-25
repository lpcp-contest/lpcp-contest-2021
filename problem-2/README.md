# Problem 2

_The problem is [Buttons and Scissors](https://play.google.com/store/apps/details?id=com.kyworks.buttonsandscissors.inapp&hl=en&gl=US) and instances are taken/adapted from the game._

Your friend Giorgio Arcani is asking for your help, again!

He received a supply of buttons attached to patches, and now someone has to cut them out in order to complete some very expensive suits.
If that weren't enough, buttons in the same patch are also of mixed color, and therefore they must be properly separated after detaching.

Giorgio has no time to waste!
Find a way to detach buttons of the same color with a cut on cardinal directions or along diagonals.
A cut must involve at least two buttons, and all buttons along the cut are detached, so they must have the same color.

Given a patch with buttons, can you find a sequence of cuts that detaches all buttons?


## Input format

The first line contains two integers, the size `S` of the patch, and the number `C` of colors.
The following `S` lines contain `S` integers each, denoting the color of the button (from `1` to `C`).


## Output format

A line with an integer `N` followed by `N` lines made of four integers `I1 J1 I2 J2`, representing a cut from `(I1,J1)` to `(I2,J2)`.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `S` between 5 and 7
* `C` between 5 and 6


## Example

Instance:

```
5 6
1 1 1 2 3
4 3 1 3 3
5 4 5 2 5
1 6 6 2 6
5 5 5 4 2
```

Possible output:

```
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
```

Checker output:

```
#### STEP 0 ####
 1  1  1  2  3 
 4  3  1  3  3 
 5  4  5  2  5 
 1  6  6  2  6 
 5  5  5  4  2 

#### STEP 1 ####
 1  1  1  2  3 
 4  3  1  3  3 
 5  4  5  2  5 
 1  6  6 [2] 6 
 5  5  5  4 [2]

#### STEP 2 ####
 1  1  1  2  3 
 4  3  1  3  3 
 5  4  5  2  5 
 1 [6][6][.][6]
 5  5  5  4  . 

#### STEP 3 ####
 1  1  1  2  3 
[4] 3  1  3  3 
 5 [4] 5  2  5 
 1  . [.] .  . 
 5  5  5 [4] . 

#### STEP 4 ####
 1  1  1  2 [3]
 .  3  1 [3] 3 
 5  .  5  2  5 
 1  .  .  .  . 
 5  5  5  .  . 

#### STEP 5 ####
 1  1  1  2  . 
 .  3  1  .  3 
[5][.][5] 2  5 
 1  .  .  .  . 
 5  5  5  .  . 

#### STEP 6 ####
[1][1][1] 2  . 
 .  3  1  .  3 
 .  .  .  2  5 
 1  .  .  .  . 
 5  5  5  .  . 

#### STEP 7 ####
 .  .  .  2  . 
 .  3 [1] .  3 
 . [.] .  2  5 
[1] .  .  .  . 
 5  5  5  .  . 

#### STEP 8 ####
 .  .  .  2  . 
 . [3][.][.][3]
 .  .  .  2  5 
 .  .  .  .  . 
 5  5  5  .  . 

#### STEP 9 ####
 .  .  .  2  . 
 .  .  .  .  . 
 .  .  .  2 [5]
 .  .  . [.] . 
 5  5 [5] .  . 

#### STEP 10 ####
 .  .  . [2] . 
 .  .  . [.] . 
 .  .  . [2] . 
 .  .  .  .  . 
 5  5  .  .  . 

#### STEP 11 ####
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  . 
 .  .  .  .  . 
[5][5] .  .  . 

CORRECT!
```
