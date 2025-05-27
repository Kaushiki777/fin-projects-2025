"""
Market Simulator v1
Author: Kaushiki Shukla
Date: May 2025

Simulates a basic market with random buyers and sellers.
Trades are executed when buyer price ≥ seller price.
Generates price and volume plots over time.
"""


import random
import matplotlib as plt

# --- CONFIGURATION ---
NUM_TRADES = 100          # Number of simulated trades
BUYER_PRICE_RANGE = (95, 105)
SELLER_PRICE_RANGE = (95, 105)

# --- DATA STORAGE ---
trade_prices = []
trade_volume = []

# --- FUNCTION: Simulate a Single Trade ---
def simulate_trade(trade_number):
    buyer_price = random.randint(*BUYER_PRICE_RANGE)
    seller_price = random.randint(*SELLER_PRICE_RANGE)
    
    if buyer_price >= seller_price:
        # Match happens
        price = (buyer_price + seller_price) // 2
        volume = random.randint(1, 10)
        trade_prices.append(price)
        trade_volume.append(volume)
        print(f"Trade {trade_number}: Executed at {price}, volume {volume}")
    else:
        # No match
        print(f"Trade {trade_number}: No match (Buyer {buyer_price}, Seller {seller_price})")

# --- MAIN LOOP ---
for i in range(NUM_TRADES):
    simulate_trade(i + 1)

# --- VISUALIZE ---
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(trade_prices, label='Price')
plt.title("Price over Time")
plt.xlabel("Trade Number")
plt.ylabel("Price")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(trade_volume, label='Volume', color='orange')
plt.title("Trade Volume over Time")
plt.xlabel("Trade Number")
plt.ylabel("Volume")
plt.legend()

plt.tight_layout()
plt.show()
