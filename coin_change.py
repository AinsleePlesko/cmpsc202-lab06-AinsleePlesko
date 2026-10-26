"""Code for the three minimum-coin change programs."""

# imports needed for this program:
import time
import matplotlib.pyplot as plt


def _validate_inputs(coins, amount):
    """Require integer inputs so all implementations share the same domain."""
    if not isinstance(amount, int) or isinstance(amount, bool):
        raise TypeError("amount must be an integer")
    coins = list(coins)
    if any(not isinstance(coin, int) or isinstance(coin, bool) for coin in coins):
        raise TypeError("coin denominations must be integers")
    return coins


# phase #1
def coin_change_recursive(coins, amount):
    """Return the minimum number of coins needed, or -1 if impossible."""
    coins = _validate_inputs(coins, amount)
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    minimum = float("inf")
    for coin in coins:
        if coin > 0:
            result = coin_change_recursive(coins, amount - coin)
            if result != -1:
                minimum = min(minimum, 1 + result)
    return -1 if minimum == float("inf") else minimum


# phase #2
def coin_change_memoized(coins, amount, memo):
    """Return the minimum coin count using memoized recursive computation."""
    coins = _validate_inputs(coins, amount)
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if amount in memo:
        return memo[amount]
    minimum = float("inf")
    for coin in coins:
        if coin > 0:
            result = coin_change_memoized(coins, amount - coin, memo)
            if result != -1:
                minimum = min(minimum, 1 + result)
    memo[amount] = -1 if minimum == float("inf") else minimum
    return memo[amount]


# phase #3
def coin_change_dp(coins, amount):
    """Return the minimum coin count using bottom-up dynamic programming."""
    coins = _validate_inputs(coins, amount)
    if amount < 0:
        return -1
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if 0 < coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return -1 if dp[amount] == amount + 1 else dp[amount]


# create a visual comparison of the three algorithms
def compare_algorithms():
    """Plot the execution times of all three implementations."""
    # Keep the range small enough for the intentionally slow recursive version.
    coins = [1, 2, 5]
    amounts = list(range(1, 21))
    algorithms = (
        ("Recursive", lambda amount: coin_change_recursive(coins, amount)),
        ("Memoized", lambda amount: coin_change_memoized(coins, amount, {})),
        ("Dynamic programming", lambda amount: coin_change_dp(coins, amount)),
    )

    for label, algorithm in algorithms:
        elapsed = []
        for amount in amounts:
            start = time.perf_counter()
            algorithm(amount)
            elapsed.append(time.perf_counter() - start)
        plt.plot(amounts, elapsed, marker="o", label=label)

    plt.xlabel("Amount")
    plt.ylabel("Execution time (seconds)")
    plt.title("Coin Change Runtime Comparison: Coins [1,2,5]")
    # The memoized and DP runtimes are much smaller than the recursive runtime.
    plt.yscale("log")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


# put it all together
if __name__ == "__main__":
    """Run the comparison of the three algorithms."""
    compare_algorithms()

    # to run in your terminal, run:
    # python3 coin_change.py