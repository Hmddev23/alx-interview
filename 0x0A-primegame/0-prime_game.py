#!/usr/bin/python3
"""
Prime Game: Determines the winner between Maria and Ben
in multiple rounds of a prime number removal game.
"""


def generate_prime_numbers(limit):
    """
    Generate a list of prime numbers up to the given
    limit using the Sieve of Eratosthenes algorithm.
    Args:
    - limit (int): Upper limit to generate prime numbers up to (inclusive).
    Returns:
    - list: List of prime numbers up to the limit.
    """
    prime_numbers = []
    sieve_list = [True] * (limit + 1)
    for potential_prime in range(2, limit + 1):
        if sieve_list[potential_prime]:
            prime_numbers.append(potential_prime)
            for multiple in range(potential_prime, limit + 1, potential_prime):
                sieve_list[multiple] = False

    return prime_numbers


def isWinner(num_rounds, round_values):
    """
    Determine the winner of the prime game after playing multiple rounds.
    Args:
    - num_rounds (int): Number of rounds/games to play.
    - round_values (list of int): integers for 'n' values for each round.
    Returns:
    - str or None: Name of the player who won
    the most rounds (either "Maria" or "Ben").
    """
    if not num_rounds or not round_values:
        return None

    maria_score = 0
    ben_score = 0

    for i in range(num_rounds):
        primes = generate_prime_numbers(round_values[i])
        if len(primes) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"

    return None
