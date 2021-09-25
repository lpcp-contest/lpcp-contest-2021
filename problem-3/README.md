# Problem 3

_The problem is [Pipes Puzzle](https://www.puzzle-pipes.com/) and instances are taken/adapted from the game._

I don't know if your name is Mario, Luigi or something else, but it's time to dress your plumber suit!

Look at that mess of pipes!
Put them in a proper order so to a single, closed circuit.

Specifically, the following types of pipes are possibly present, represented by a two-digits number:

```
10 ─  LONG PIPE
11 │  LONG PIPE
20 ╮  CORNER TUBE
21 ╯  CORNER TUBE
22 ╰  CORNER TUBE
23 ╭  CORNER TUBE
30 ╶  CLOSED PIPE
31 ╷  CLOSED PIPE
32 ╴  CLOSED PIPE
33 ╵  CLOSED PIPE
50 ┬  T PIPE
51 ┤  T PIPE
52 ┴  T PIPE
53 ├  T PIPE
```

Note that the first digit is the actual type of pipe, and the second digit represents the orientation of the pipe.
For example, `10` is a long pipe with horizontal orientation, and `11` is a long pipe with vertical orientation.
The only action you can do on a pipe is *clockwise rotation*, possibly multiple times.
For example, rotating `30` two times, a pipe closed on the left and open on the right, turns it to `32`, a pipe closed on the right and open on the left. 

Your task is to form a unique closed circuit.


## Input format

The first line contains an integer, the size `S` of the grid.
The following `S` lines contain `S` integers each, denoting the type and orientation of a pipe.


## Output format

A line with an integer `N` followed by `N` lines made of two integers `I J`, representing a pipe to rotate clockwise.
`I` and `J` range from `1` to `N`.


## Constraints

Instances are guaranteed to satisfy the following constraints:

* `S` between 4 and 40


## Example

Instance:

```
4
31 22 31 31 
33 52 50 11 
21 52 52 53 
32 33 31 23 
```

Possible output:

```
19
1 1
1 1
1 1
1 2
1 2
2 1
2 3
3 1
3 1
3 2
3 2
3 4
3 4
4 1
4 3
4 3
4 3
4 4
4 4
```

Checker output:

```text
#### STEP 0 ####
╷╰╷╷
╵┴┬│
╯┴┴├
╴╵╷╭

#### STEP 1 ####
╴╰╷╷
╵┴┬│
╯┴┴├
╴╵╷╭

#### STEP 2 ####
╵╰╷╷
╵┴┬│
╯┴┴├
╴╵╷╭

#### STEP 3 ####
╶╰╷╷
╵┴┬│
╯┴┴├
╴╵╷╭

#### STEP 4 ####
╶╭╷╷
╵┴┬│
╯┴┴├
╴╵╷╭

#### STEP 5 ####
╶╮╷╷
╵┴┬│
╯┴┴├
╴╵╷╭

#### STEP 6 ####
╶╮╷╷
╶┴┬│
╯┴┴├
╴╵╷╭

#### STEP 7 ####
╶╮╷╷
╶┴┤│
╯┴┴├
╴╵╷╭

#### STEP 8 ####
╶╮╷╷
╶┴┤│
╰┴┴├
╴╵╷╭

#### STEP 9 ####
╶╮╷╷
╶┴┤│
╭┴┴├
╴╵╷╭

#### STEP 10 ####
╶╮╷╷
╶┴┤│
╭├┴├
╴╵╷╭

#### STEP 11 ####
╶╮╷╷
╶┴┤│
╭┬┴├
╴╵╷╭

#### STEP 12 ####
╶╮╷╷
╶┴┤│
╭┬┴┬
╴╵╷╭

#### STEP 13 ####
╶╮╷╷
╶┴┤│
╭┬┴┤
╴╵╷╭

#### STEP 14 ####
╶╮╷╷
╶┴┤│
╭┬┴┤
╵╵╷╭

#### STEP 15 ####
╶╮╷╷
╶┴┤│
╭┬┴┤
╵╵╴╭

#### STEP 16 ####
╶╮╷╷
╶┴┤│
╭┬┴┤
╵╵╵╭

#### STEP 17 ####
╶╮╷╷
╶┴┤│
╭┬┴┤
╵╵╶╭

#### STEP 18 ####
╶╮╷╷
╶┴┤│
╭┬┴┤
╵╵╶╮

#### STEP 19 ####
╶╮╷╷
╶┴┤│
╭┬┴┤
╵╵╶╯

CORRECT!
```
