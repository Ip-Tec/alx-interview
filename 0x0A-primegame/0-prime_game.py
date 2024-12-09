#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Returns a list of prime numbers up to n using the Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

def isWinner(x, nums):
    """
    Determine the winner of each game round.

    Args:
        x (int): Number of rounds.
        nums (list): Array containing the upper bounds for each round.

    Returns:
        str: Name of the player with the most wins ("Maria" or "Ben").
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # Precompute the number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if i in primes else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
