# Problem 4

Balls... balls everywhere!
Someone messed up with your precious golf balls, and now they are all mixed in colors.
This doesn't satisfy your sense of order, so you have to rearrange them in your containers, ie. bottles with space for four balls.
You will be satisfied when balls of the same color will be in the same bottle.

Don't be hasty!
Your balls are so precious that you are going to move one ball at time.
Luckily, you have some extra bottles to help you in the process, but you must avoid to move a ball on top of a ball of different color.
Remember that each bottle has space for no more than four balls!


## Input format

The first line contains two integers, the number `F` of full bottles and the number `E` of empty bottles.
The following `F` lines contain `4` integers `B1 B2 B3 B4` each, representing the color of the balls in each bottle, where `B1` is the color of the bottom ball.


## Output format

A line with an integer `N` followed by `N` lines made of two integers `FROM TO`, representing the movement of the top ball in bottle `FROM` to the bottle `TO`.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `F` between 4 and 7
* `E` fixed to 2


## Example

Instance:

```
4 2
1 1 2 2
3 3 3 2
4 4 4 1
2 4 1 3
```

Possible output:

```
11
1 6
2 6
4 5
2 5
2 5
1 6
4 1
3 1
4 3
2 5
4 6
```

Checker output:

```
#### STEP 0 ####
1: 1 1 2 2
2: 3 3 3 2
3: 4 4 4 1
4: 2 4 1 3
5: 
6: 

#### STEP 1 ####
1: 1 1 2 >>> 2
2: 3 3 3 2
3: 4 4 4 1
4: 2 4 1 3
5: 
6: 2 <<<

#### STEP 2 ####
1: 1 1 2
2: 3 3 3 >>> 2
3: 4 4 4 1
4: 2 4 1 3
5: 
6: 2 2 <<<

#### STEP 3 ####
1: 1 1 2
2: 3 3 3
3: 4 4 4 1
4: 2 4 1 >>> 3
5: 3 <<<
6: 2 2

#### STEP 4 ####
1: 1 1 2
2: 3 3 >>> 3
3: 4 4 4 1
4: 2 4 1
5: 3 3 <<<
6: 2 2

#### STEP 5 ####
1: 1 1 2
2: 3 >>> 3
3: 4 4 4 1
4: 2 4 1
5: 3 3 3 <<<
6: 2 2

#### STEP 6 ####
1: 1 1 >>> 2
2: 3
3: 4 4 4 1
4: 2 4 1
5: 3 3 3
6: 2 2 2 <<<

#### STEP 7 ####
1: 1 1 1 <<<
2: 3
3: 4 4 4 1
4: 2 4 >>> 1
5: 3 3 3
6: 2 2 2

#### STEP 8 ####
1: 1 1 1 1 <<<
2: 3
3: 4 4 4 >>> 1
4: 2 4
5: 3 3 3
6: 2 2 2

#### STEP 9 ####
1: 1 1 1 1
2: 3
3: 4 4 4 4 <<<
4: 2 >>> 4
5: 3 3 3
6: 2 2 2

#### STEP 10 ####
1: 1 1 1 1
2: >>> 3
3: 4 4 4 4
4: 2
5: 3 3 3 3 <<<
6: 2 2 2

#### STEP 11 ####
1: 1 1 1 1
2: 
3: 4 4 4 4
4: >>> 2
5: 3 3 3 3
6: 2 2 2 2 <<<

CORRECT!
```
