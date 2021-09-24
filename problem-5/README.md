# Problem 5

Water... water everywhere!
Does it remind you of something?

You are given some bottles filled with four shots of *colored water* (pretend it to be water if you are under 21 years old), and some empty bottles.
I don't know if it's the strange smell of this water, or we drunk too much of it, but shots of water of different colors do not mix.
We would like to rearrange those shots so that filled bottles will contain water of the same color.
Can you do it for us?

You can pour water from a bottle `A` to a bottle `B` only if either `B` is empty or the top shot in `B` has the same color of `A`.
Moreover, if the top `k` shots of `A` have the same color, all of them are poured on `B` up to the capacity of `B`.
For example, if `A` contains `RED GREEN GREEN GREEN` and `B` contains `YELLOW GREEN`, then after pouring they will respectively contain `RED GREEN` and `YELLOW GREEN GREEN GREEN`, that is, two shots of `GREEN` are poured from `A` to `B`.


## Input format

The first line contains two integers, the number `F` of full bottles and the number `E` of empty bottles.
The following `F` lines contain `4` integers `W1 W2 W3 W4` each, representing the color of the water in each bottle, where `W1` is the color of the water in the bottom slot.


## Output format

A line with an integer `N` followed by `N` lines made of two integers `FROM TO`, representing the movement of the top ball in bottle `FROM` to the bottle `TO`.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `F` between 2 and 5
* `E` between 1 and 3


## Example

Instance:

```
2 1
1 2 1 2
2 1 2 1
```

Possible output:

```
8
1 3
2 1
3 2
1 3
2 1
2 3
1 2
1 3
```

Checker output:

```
#### STEP 0 ####
1: 1 2 1 2
2: 2 1 2 1
3: 

#### STEP 1 ####
1: 1 2 1 >>> 2
2: 2 1 2 1
3: 2 <<<

#### STEP 2 ####
1: 1 2 1 1 <<<
2: 2 1 2 >>> 1
3: 2

#### STEP 3 ####
1: 1 2 1 1
2: 2 1 2 2 <<<
3: >>> 2

#### STEP 4 ####
1: 1 2 >>> 1 1
2: 2 1 2 2
3: 1 1 <<<

#### STEP 5 ####
1: 1 2 2 2 <<<
2: 2 1 >>> 2 2
3: 1 1

#### STEP 6 ####
1: 1 2 2 2
2: 2 >>> 1
3: 1 1 1 <<<

#### STEP 7 ####
1: 1 >>> 2 2 2
2: 2 2 2 2 <<<
3: 1 1 1

#### STEP 8 ####
1: >>> 1
2: 2 2 2 2
3: 1 1 1 1 <<<

CORRECT!
```
