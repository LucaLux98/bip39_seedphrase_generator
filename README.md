# BIP39 SEED PHRASE GENERATOR (Python)

Educational Python implementation of a fully offline BIP39 mnemonic (seed phrase) generator.

---

## Overview

This project generates valid BIP39 24-word mnemonic seed phrases starting from cryptographically secure entropy.  
It follows the official BIP39 standard, including checksum calculation and wordlist mapping.

The implementation is fully offline and does not rely on external libraries.

---

## What this project does

The generator implements the complete BIP39 pipeline:

- Generates 256-bit cryptographically secure entropy
- Computes SHA-256 hash for checksum
- Appends checksum bits to entropy
- Splits the result into 11-bit segments
- Maps each segment to the official BIP39 English wordlist (2048 words)
- Produces a 24-word mnemonic phrase

---

## Pipeline

Entropy (256-bit) ➡️ SHA-256 Hash ➡️ Checksum (8-bit) ➡️ Entropy + Checksum (264-bit) ➡️ Split into 11-bit chunks ➡️ Index mapping (0–2047) ➡️ BIP39 Mnemonic (24 words)

---

## Features

- Fully offline execution
- No external dependencies
- BIP39-compliant implementation
- Deterministic and reproducible output
- Manual implementation of bit-level operations
- Compatible with official BIP39 wordlist

---

## Requirements

- Python 3.x
- Official BIP39 English wordlist (2048 words) provided as a .txt file inside a wordlist folder

---

## Project Structure

```bash
bip39_seedphrase_generator/
    ├── BIP39_seedphrase.py
    └── wordlist
           └── english.txt
