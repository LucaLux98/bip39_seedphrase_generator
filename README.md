# BIP-39 SEED PHRASE GENERATOR (Python)
Offline Python tool that generates BIP39-compliant 24-word mnemonic seed phrases using 256-bit entropy and SHA-256 checksum.

## Features
- Fully offline generation
- 256-bit entropy (32 Bytes)
- SHA-256 checksum (BIP39 standard)
- Compatible with official BIP39 wordlist (2048 words)
- Deterministic and reproducible

## How it works
1. Generates secure entropy
2. Computes SHA-256 checksum
3. Combines entropy + checksum
4. Splits into 11-bit chunks
5. Maps chunks to BIP39 wordlist

## DISCLAIMER: 
This project is for educational purposes only. Do NOT use this tool to generate wallets for real funds.
