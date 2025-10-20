# 📈 Bitget Free Historical Candle Data Downloader (Python)

Easily **fetch historical candlestick (OHLCV) data** from the **Bitget Futures API** for any trading pair and interval — completely **free and without API keys**.  
This Python script automatically retrieves full historical ranges (e.g., months or years) and saves clean, ready-to-use **CSV files** for research, backtesting, or data analysis.

---

## 🚀 Features

✅ **Free data — no API key required**  
✅ **Fetch from Bitget Futures API**  
✅ **Custom date range support** (e.g., 2021–2025)  
✅ **Works with all timeframes** (1m, 5m, 1H, 4H, 1D, etc.)  
✅ **Automatically continues across multiple requests**  
✅ **Appends new data to existing CSV files**  
✅ **Rate-limit safe** with 0.2s delay between calls  
✅ **Clean output** — ISO timestamps and OHLCV structure  

---

## 🧩 Example Use Cases

- Quantitative trading research and strategy development  
- Backtesting bots with real Bitget data  
- Market structure or volatility analysis  
- Machine learning model training (price prediction, volatility forecasting)  

---

## 📦 Installation

Make sure you have **Python 3.8+** installed.

Clone the repository and install dependencies:

```bash
git clone https://github.com/frostyalce000/bitget-free-historical-candlestick-data-fetcher.git
cd bitget-free-historical-candlestick-data-fetcher
pip install -r requirements.txt
````

If you don’t have a `requirements.txt`, just install manually:

```bash
pip install requests pandas
```

---

## ⚙️ Configuration

Edit these lines at the top of the script:

```python
SYMBOL = "ETHUSDT"                # Trading pair, e.g., BTCUSDT, ETHUSDT
PRODUCT_TYPE = "USDT-FUTURES"     # Bitget product type (USDT-FUTURES / COIN-FUTURES / MIX)
INTERVAL = "1H"                   # Supported: 1m, 5m, 15m, 1H, 4H, 1D

START_DATE = "2025-07-16T00:00:00Z"  # Start time (UTC)
END_DATE = "2025-10-16T23:59:00Z"    # End time (UTC)
```

You can set any date range and timeframe Bitget supports.
The output will automatically save as:

```
historical_ETHUSDT_1H_2025-07-16_2025-10-16.csv
```

---

## ▶️ Usage

Run the script directly:

```bash
python fetch_bitget_candles.py
```

Example output:

```
Fetching candles from 2025-07-16 00:00:00+00:00 to 2025-10-16 23:59:00+00:00 for ETHUSDT...
Request #1: Fetching candles ending at 2025-10-16T23:59:00+00:00 ...
  Retrieved: 200 candles; Total so far: 200
Request #2: Fetching candles ending at 2025-10-08T00:00:00+00:00 ...
  Retrieved: 200 candles; Total so far: 400
...
Created new data file: historical_ETHUSDT_1H_2025-07-16_2025-10-16.csv with 2184 records
```

If the file already exists, it automatically **appends new data**.

---

## 📂 Output Example

| timestamp            | open    | high    | low     | close   | volume  | quote_volume |
| -------------------- | ------- | ------- | ------- | ------- | ------- | ------------ |
| 2025-07-16T00:00:00Z | 3200.12 | 3215.45 | 3190.33 | 3205.77 | 1234.12 | 3958223.50   |
| 2025-07-16T01:00:00Z | 3205.77 | 3220.50 | 3198.21 | 3218.00 | 1320.33 | 4255521.92   |
| ...                  | ...     | ...     | ...     | ...     | ...     | ...          |

---

## 🧠 Notes

* Uses the **Bitget API v2** endpoint:
  `https://api.bitget.com/api/v2/mix/market/history-candles`
* The script fetches in reverse (from end date backwards) due to Bitget’s API limitations.
* Default rate limit is safe at **0.2 seconds** per request — adjust if needed.
* Data includes **open, high, low, close, volume, quote_volume**, and **timestamp (UTC)**.

---

## 💡 Example: Fetch BTCUSDT Daily Candles

```python
SYMBOL = "BTCUSDT"
PRODUCT_TYPE = "USDT-FUTURES"
INTERVAL = "1D"
START_DATE = "2023-01-01T00:00:00Z"
END_DATE = "2023-12-31T23:59:00Z"
```

---

## 🧰 Tech Stack

* **Language:** Python 3
* **Libraries:** requests, pandas
* **Exchange:** Bitget (Futures)
* **Output:** CSV (timestamp, OHLCV)

---

## 🌟 Contribute

Pull requests, issues, and feature suggestions are welcome!
If you find this project helpful, please ⭐ **star the repo** to support future updates.
