1️⃣ The First Mystery (Stationarity)

The average height (mean) slowly increases over time (upward drift/trend).
This makes forecasting tricky because the mean keeps changing, so the model can’t learn a stable pattern.

2️⃣ Differencing
        
The bottom plot calms down because differencing removes the trend.
The slow upward movement disappears, leaving only small fluctuations.

3️⃣ Log Transform

Logs reduce large values more than small ones, so variance becomes stable and big swings shrink.

4️⃣ ACF (Memory)

The first few lags are most important.
Memory fades slowly, meaning past values influence the present for several steps.

5️⃣ PACF (Direct Influence)

It means lag 2 has a direct effect, not just through lag 1.
So the process likely has AR structure of order ≥ 2.

6️⃣ Model Identification

ACF spikes at lags 1–3 then vanishes → MA(3)

PACF spikes only at lag 1 → AR(1)

7️⃣ Mini Puzzles
Puzzle A

Use differencing (removes climbing trend).

Puzzle B

Seasonality or MA effect at lag 3.

Puzzle C

AR(2)

8️⃣ Mini Case Study — Food Delivery Orders
Q1 — Stationarity

Problem: trend + seasonality (non-stationary)
Fix: differencing or seasonal differencing

Q2 — Memory

Gradual fading means long memory, so model should include multiple past days (higher AR order)

Q3 — Seasonality

Repeated peaks at lag 7, 14, 21…
Cause: weekly seasonality