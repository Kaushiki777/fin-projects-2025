# 📈 Market Simulator – v1

This project simulates a simple financial market where random buyer and seller agents place limit or market orders. It visualizes how trades are executed based on price overlap, and how price and volume evolve over time.

---

## 💡 Project Goals

- Understand the basics of order flow and price discovery
- Simulate a simplified quote-driven market
- Visualize price and trade volume changes with each executed trade
- Lay the foundation for more advanced simulations (multi-agent, inventory limits, LOBs)

---

## 🧠 What It Does

- Generates random buyer and seller order prices
- Executes trades when buyer price ≥ seller price
- Calculates transaction price as midpoint of bid/ask
- Randomizes trade volume
- Tracks:
  - Executed trade prices
  - Volumes per trade
- Plots both over time using `matplotlib`

---

## 📊 Example Output

![Trade Chart]
![market_simulator](https://github.com/user-attachments/assets/fa551a10-e275-46ba-b6ad-060825772f04)


> Price and volume movements over 100 trades

---

## 🛠 Technologies Used

- Python 3
- Matplotlib
- Random (for agent simulation)

---
