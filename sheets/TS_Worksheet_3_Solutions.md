# TS_Worksheet_3 Solutions

### Q1

Daily consumption similar to previous day → depends on lagged values.
👉 **AR model**, because $X_t$ depends on $X_{t-1}$.

### Q2

Sudden power failures = short-term shocks/errors.
👉 **MA model**, because it models dependence on past errors.

### Q3

It refers to **lag difference**.

**Expression:**
$X_t - X_{t-1}$

### Q4
(a)
It represents **first differencing**.

(b)
It removes **trend** and makes the series **stationary**, which AR/MA models require.

### Q5
(a)
Dependence exists only up to 2 past lags.

(b)
Suggests **MA(2)** model (ACF cuts off at lag q).

### Q6
(a)
Differencing is needed to remove **non-stationarity/trend**.

(b)
ACF cuts off at 1 → **MA(1)**
First difference → **d = 1**
👉 **ARIMA(0, 1, 1)**

### Q7

Shuffling destroys **time order**, so past values no longer relate to future ones.
Therefore ACF and lag relationships become meaningless.

---

### 🎯 Quick Memory Cheat Sheet (super useful for exams)

| Pattern | Model |
| :--- | :--- |
| **PACF cutoff at p** | **AR(p)** |
| **ACF cutoff at q** | **MA(q)** |
| **Need differencing** | **ARIMA** |
| **Gradual decay both** | **Mixed ARMA** |
