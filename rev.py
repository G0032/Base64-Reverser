import base64

data = "YVZnemJFbHplR0ZQUW5JcllWUTBWRkIzZFhsSGNXaHZSVGhtVVc4ME1qTk9helIxVWpGWUwwc3JZejA9"

for i in range(3):
    try:
        data = base64.b64decode(data)
        print(f"[{i+1}] {data}")
    except Exception as e:
        print(f"Decoding failed at iteration {i+1}: {e}")
        break
