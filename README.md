# CrackHex

CrackHex is a Python-based hash cracking tool designed for CTFs, security labs, and educational purposes.

Unlike traditional wordlist-only tools, CrackHex can generate password combinations directly from user-provided inputs without creating a separate wordlist file. This helps when attacking lab hashes that are based on known information such as names, usernames, dates, phone numbers, or custom keywords.

## Features

* Crack hashes using the RockYou wordlist
* Generate password combinations from user input
* No need to create a separate custom wordlist file
* Multiple cracking modes
* Word filtering options to reduce unnecessary attempts
* Suitable for CTF challenges and security labs

---

## Modes

### 1. Filtered Wordlist Mode

Uses the RockYou wordlist but allows filtering before cracking.

Available filters:

* Password length
* Starting characters
* Combination of both

This helps reduce the search space and speeds up cracking when partial information is known.

---

### 2. Self Generated Wordlist Mode

Generate password combinations directly from user input.

Example inputs:

* Name
* Username
* Phone number
* Birth year
* Custom keywords

CrackHex creates combinations automatically and attempts to crack the target hash.

Available filters:

* Password length
* Starting characters
* Combination of both

No external wordlist file is required.

---

### 3. Default Mode

Uses the complete RockYou wordlist without any filtering.

Recommended when no information about the password is available.

---

## Installation

```bash
git clone https://github.com/deependu5960/CrackHex.git
cd CrackHex
python install.py
```

## Usage

```bash
python start.py
```

---

## Workflow

1. Start CrackHex
2. Select the hash type
3. Choose a cracking mode
4. Enter the target hash
5. Configure filters (optional)
6. Start cracking

---

## Use Cases

* Capture The Flag (CTF) challenges
* Cybersecurity labs
* Password auditing in authorized environments
* Learning password cracking techniques
* Educational demonstrations

---

## Disclaimer

This tool is intended for educational purposes, CTF challenges, authorized security testing, and laboratory environments only.

Users are responsible for ensuring they have permission to test any system, account, or hash. Unauthorized access to systems or accounts may violate laws and regulations.
