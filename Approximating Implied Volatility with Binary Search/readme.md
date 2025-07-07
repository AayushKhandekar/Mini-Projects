# Approximating Implied Volatility with Binary Search

This Python script estimates the implied volatility (IV) of a European call option using the Black-Scholes pricing model and binary search on a continuous 1D space.

## Overview

Knowns: 
- Market price of a European call option
- Strike price, spot price, risk-free rate, and time to maturity

The script uses binary search to find the value of volatility `σ` 

## Model Used

### Black-Scholes-Merton Model (European Call Option)

The Implied Volatility is a value of sigma that, when substituted into the BSM equation, provides the call price. Since it is not possible to convert the BSM equation so that it is a function of sigma, we need to approximate the value of sigma for which the function provides the call price. The value which satisfies this condition is the Implied Volatility.

## Example Parameters

```python
S0 = 21      # Spot price
K = 20       # Strike price
r = 0.10     # Risk-free rate
T = 0.25     # Time to maturity (in years)
c = 1.875    # Market price of the European call
