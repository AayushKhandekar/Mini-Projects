import numpy as np
from scipy.stats import norm

S0 = 21
K = 20
r = 0.1
T = 0.25
c = 1.875

iv_bounds = [0, 3]

class BlackScholesModel:

    def __init__(self):
        pass

    def d1(self, S0, K, T, r, sigma):
        return (np.log(S0 / K) + (r + 0.5 * (sigma ** 2)) * T) / (sigma * np.sqrt(T))
    
    def d2(self, S0, K, T, r, sigma):
        return self.d1(S0, K, T, r, sigma) - (sigma * np.sqrt(T))
    
    def call_price(self, S0, K, T, r, sigma):
        d1 = self.d1(S0, K, T, r, sigma)
        d2 = self.d2(S0, K, T, r, sigma)
        return (S0 * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2))
    
    def put_price(self, S0, K, T, r, sigma):
        d1 = self.d1(S0, K, T, r, sigma)
        d2 = self.d2(S0, K, T, r, sigma)
        return (-S0 * norm.cdf(-d1)) + (K * np.exp(-r * T) * norm.cdf(-d2))

bsm = BlackScholesModel()

def binary_search_iv(target_price, S0, K, T, r, low, high, epsilon=1e-4):
    while high - low > epsilon:
        mid = (low + high) / 2
        price = bsm.call_price(S0, K, T, r, mid)
        if price < target_price:
            low = mid
        else:
            high = mid
    return (low + high) / 2

iv = binary_search_iv(c, S0, K, T, r, iv_bounds[0], iv_bounds[1])
print(f"Implied Volatility ≈ {iv:.4f}")