import requests
import pandas as pd
from datetime import datetime, timezone, timedelta
import time
import os

# ========== Configuration ==========
SYMBOL = "ETHUSDT"
PRODUCT_TYPE = "USDT-FUTURES"
INTERVAL = "1H"

# Specify your date range here in UTC (ISO8601 format for convenience)
START_DATE = "2025-07-16T00:00:00Z"
END_DATE = "2025-10-16T23:59:00Z"
OUTPUT_FILENAME = f"historical_{SYMBOL}_{INTERVAL}_{START_DATE[:10]}_{END_DATE[:10]}.csv"

def fetch_candles(symbol, interval, start_time, end_time):
    """Fetch historical candles between start_time and end_time from Bitget API"""
    all_candles = []
    limit = 200  # max candles per request
    current_end_time = end_time
    request_count = 0  # Add a counter

    while True:
        try:
            params = {
                "symbol": symbol,
                "productType": PRODUCT_TYPE,
                "granularity": interval,
                "endTime": int(current_end_time.timestamp() * 1000),
                "limit": limit
            }
            print(f"Request #{request_count + 1}: Fetching candles ending at {current_end_time.isoformat()} ...")
            response = requests.get("https://api.bitget.com/api/v2/mix/market/history-candles", params=params)
            data = response.json().get("data", [])

            if not data:
                print("No more data to fetch.")
                break

            batch = [{
                "timestamp": datetime.fromtimestamp(int(entry[0]) / 1000, tz=timezone.utc),
                "open": float(entry[1]),
                "high": float(entry[2]),
                "low": float(entry[3]),
                "close": float(entry[4]),
                "volume": float(entry[5]),
                "quote_volume": float(entry[6])
            } for entry in data]

            batch = [c for c in batch if c["timestamp"] >= start_time]

            if not batch:
                break

            all_candles.extend(batch)
            print(f"  Retrieved: {len(batch)} candles; Total so far: {len(all_candles)}")

            oldest = min(c["timestamp"] for c in batch)
            if oldest <= start_time:
                break

            current_end_time = oldest - timedelta(hours=1)
            request_count += 1
            
            time.sleep(0.2)

        except Exception as e:
            print(f"Error fetching data: {e}")
            break

    df = pd.DataFrame(all_candles)
    if not df.empty:
        df = df.sort_values("timestamp").drop_duplicates()
    return df


def save_to_csv(df, filename):
    """Save DataFrame to CSV with proper formatting"""
    df = df.copy()
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%SZ')

    if os.path.exists(filename):
        existing = pd.read_csv(filename)
        combined = pd.concat([existing, df]).drop_duplicates('timestamp')
        combined = combined.sort_values('timestamp')
        combined.to_csv(filename, index=False)
        print(f"Appended {len(combined) - len(existing)} new records to {filename}")
    else:
        df.to_csv(filename, index=False)
        print(f"Created new data file: {filename} with {len(df)} records")


def main():
    start_time = datetime.fromisoformat(START_DATE.replace("Z", "+00:00"))
    end_time = datetime.fromisoformat(END_DATE.replace("Z", "+00:00"))

    print(f"Fetching candles from {start_time} to {end_time} for {SYMBOL}...")
    df = fetch_candles(SYMBOL, INTERVAL, start_time, end_time)

    if not df.empty:
        print(f"Retrieved {len(df)} candles ({df['timestamp'].min()} to {df['timestamp'].max()})")
        save_to_csv(df, OUTPUT_FILENAME)
    else:
        print("No data retrieved. Check API connection and parameters")


if __name__ == "__main__":
    main()
