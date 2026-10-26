# Ainslee Plesko

## Summary of Set-Up:
The implementations in `coin_change.py` compare naive recursive, memoized, and bottom-up methods for the configured coin denominations and amounts; the runtime for each method is measured across those inputs.

## Findings:
The major finding is that naive recursion becomes much slower as the amount increases because it repeatedly solves the same subproblems. Memoization and bottom-up dynamic programming avoid that repeated work and perform substantially better, with their relative runtimes shown in the plot.

## Comparison Plot of Results:
[comparison plot](comparison_plot.png)