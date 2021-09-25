# Problem 1

_The problem is based on the [Crazy Frog Puzzle](https://www.nearly42.org/vdisk/cstheory/crazyfrog.pdf) and instances are randomly generated._

You have the control of a little frog, capable of very long jumps, and today is your lucky day!

The little frog just woke up in an SxS land, with few obstacles and a lot of insects.
Time to eat them all!
The frog can jump as long as you want, but only in the four cardinal directions (don't ask why) and you cannot land on any obstacle or already visited places (you will see why).
Don't leave any insect alive!


## Input format

The first line contains three integers, the size `S` of the land, and the coordinates `I`,`J` of the place where you woken up.
The following `S` lines contain `S` integers each, denoting the absense (`0`) or presence (`1`) of an obstacle.


## Output format

A line with an integer `N` followed by `N` lines made of two integers `I`,`J`, each pair representing the landing place of your jumps.
`I` and `J` range from `1` to `N`.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `S` between 4 and 60


## Example

Instance:

```
4 3 3
0 1 0 0
0 0 0 1
1 0 0 0
0 1 0 0
```

Possible output:

```
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
```

Checker output:

```
#### STEP 0 ####
🦟🧱🦟🦟
🦟🦟🦟🧱
🧱🦟🐸🦟
🦟🧱🦟🦟
=> start  at (3, 3)

#### STEP 1 ####
🦟🧱🦟🦟
🦟🦟🦟🧱
🧱🦟💩🦟
🦟🧱🐸🦟
=> jumped to (4, 3)

#### STEP 2 ####
🦟🧱🦟🦟
🦟🦟🦟🧱
🧱🦟💩🦟
🦟🧱💩🐸
=> jumped to (4, 4)

#### STEP 3 ####
🦟🧱🦟🦟
🦟🦟🦟🧱
🧱🦟💩🦟
🐸🧱💩💩
=> jumped to (4, 1)

#### STEP 4 ####
🦟🧱🦟🦟
🐸🦟🦟🧱
🧱🦟💩🦟
💩🧱💩💩
=> jumped to (2, 1)

#### STEP 5 ####
🐸🧱🦟🦟
💩🦟🦟🧱
🧱🦟💩🦟
💩🧱💩💩
=> jumped to (1, 1)

#### STEP 6 ####
💩🧱🐸🦟
💩🦟🦟🧱
🧱🦟💩🦟
💩🧱💩💩
=> jumped to (1, 3)

#### STEP 7 ####
💩🧱💩🐸
💩🦟🦟🧱
🧱🦟💩🦟
💩🧱💩💩
=> jumped to (1, 4)

#### STEP 8 ####
💩🧱💩💩
💩🦟🦟🧱
🧱🦟💩🐸
💩🧱💩💩
=> jumped to (3, 4)

#### STEP 9 ####
💩🧱💩💩
💩🦟🦟🧱
🧱🐸💩💩
💩🧱💩💩
=> jumped to (3, 2)

#### STEP 10 ####
💩🧱💩💩
💩🐸🦟🧱
🧱💩💩💩
💩🧱💩💩
=> jumped to (2, 2)

#### STEP 11 ####
💩🧱💩💩
💩💩🐸🧱
🧱💩💩💩
💩🧱💩💩
=> jumped to (2, 3)

CORRECT!
```
