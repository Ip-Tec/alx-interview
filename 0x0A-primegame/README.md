# Prime Game

## Overview
The Prime Game is a competitive game between two players, Maria and Ben. Given a set of consecutive integers from 1 up to a number `n`, they take turns selecting a prime number from the set, removing that prime and its multiples from the set. The player who cannot make a move loses the game. Maria always plays first, and both players play optimally.

This project implements the game logic to determine the winner of multiple rounds of the game based on a given set of numbers for each round.

## Problem Description
In each round, the players will:
1. Choose a prime number from the set of integers.
2. Remove that prime number and its multiples.
3. The player who cannot make a valid move loses.

The task is to determine who wins the most rounds after `x` rounds.

### Function
`def isWinner(x, nums):`
- **x (int)**: The number of rounds.
- **nums (list)**: A list of integers, where each integer is the upper bound for each round.

### Return Value
- Returns the name of the player with the most wins: either `"Maria"` or `"Ben"`.
- If the winner cannot be determined, return `None`.

## How It Works
1. The Sieve of Eratosthenes algorithm is used to efficiently find all prime numbers up to the largest number in `nums`.
2. The prime count for each number is calculated.
3. For each round, the number of primes up to `n` is checked:
   - If the count of primes is odd, Maria wins.
   - If the count is even, Ben wins.
4. After all rounds, the player with the most wins is returned.

## Example

### Input:
```python
x = 3
nums = [4, 5, 1]
```

```bash
Winner: Ben
```

## Explanation:
    - In the first round (n = 4):
	- Maria picks 2, leaving 1, 3.
	- Ben picks 3, leaving 1.
	- Ben wins as no prime numbers remain for Maria to pick.
    - In the second round (n = 5):
	- Maria picks 2, leaving 1, 3, 5.
 	- Ben picks 3, leaving 1, 5.
	- Maria picks 5, leaving 1.
	- Maria wins as no prime numbers remain for Ben.
    - In the third round (n = 1):
	- Ben wins since there are no primes for Maria to pick.

## Requirements
    - Python 3.4.3 or higher.
    - Ubuntu 20.04 LTS for execution.

## File Structure
    - 0-prime_game.py: Contains the implementation of the game logic.
    - main_0.py: Runs the game and determines the winner based on multiple rounds.
    - README.md: This file, which explains the project and provides examples.

## Installation
To run the project, simply clone this repository and execute the Python script:

```bash
git clone <repository-url>
cd 0x0A-primegame
python3 main_0.py
```


