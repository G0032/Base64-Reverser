# Base64-Reverser
CTF Script
Here’s a concise and clear markdown description for the provided code:

---

## Base64 Multi-layer Decoder (`decoder.py`)

This script attempts to decode a string that has been encoded multiple times using Base64 encoding. It is useful in CTF challenges or situations where data has been repeatedly Base64-encoded.

### How It Works

- The script starts with a long Base64-encoded string stored in the variable `data`.
- It tries to decode `data` up to 25 times in a loop.
- After each decoding step, it prints the decoded result and the iteration number.
- If decoding fails at any point (e.g., the data is no longer valid Base64), the script prints an error message and stops.

### Example

```
[1] b'Some intermediate result...'
[2] b'Another layer...'
...
[25] b'Final decoded data or error'
```

### Use Case

- **CTF Challenges**: Unwrapping data that has been encoded multiple times.
- **Forensics**: Analyzing suspicious payloads that use encoding as obfuscation.

---

**Note:**  
The script prints the decoded output at each step for inspection. If the data cannot be decoded further, it will stop and print an error message.
