# Pure TEA (Tiny Encryption Algorithm) Implementation in Python

This repository contains a clean, educational implementation of the **TEA (Tiny Encryption Algorithm)** in Python, written entirely **without using structured data libraries** (such as Python's built-in `struct` module). All byte manipulation, padding, and conversion into 32-bit registers are performed manually using low-level bitwise operations.

## 📌 Features

* **No Structural Dependencies:** Designed completely from scratch using fundamental data types, bitwise shifts, and masks.
* **32-bit Integer Simulation:** Python handles arbitrarily large integers automatically. To perfectly match C's `uint32_t` modulo overflow behavior required by TEA, an `& 0xFFFFFFFF` mask is applied to every mathematical operation.
* **Manual Byte Parsing:** Blocks of data and keys are parsed from `bytes` into arithmetic variables (`left`, `right`, `k0`–`k3`) using explicit bit shifts (`<< 24`, `<< 16`, etc.).
* **Feistel Cipher Structure:** Implements standard 32 cycles (64 rounds) of the Feistel network.
* **Zero Padding:** Automatically pads input text with null bytes (`\x00`) to guarantee compatibility with 8-byte block sizes.

## 🚀 Getting Started

No third-party libraries are required. The script runs natively on any modern Python 3 installation.

**Test** Enter your message and encryption key when prompted:

```text
Enter text for TEA encryption: Hello World!
Enter TEA encryption key: my_secret_key

Encrypted bytes: b'\x84\xec\xa9...\x1f'
Decrypted text: Hello World!
```

## ⚠️ Security Disclaimer

The original Tiny Encryption Algorithm (TEA) is vulnerable to **related-key attacks**, where each 128-bit key corresponds to three other equivalent keys. This effectively reduces its keyspace to 126 bits. It is also susceptible to differential cryptanalysis. 

This repository is intended **strictly for educational and academic purposes** to demonstrate the mechanics of symmetric block ciphers. It should not be deployed in production environments handling sensitive data.
