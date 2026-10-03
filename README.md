# SSH Brute-Force Log Analyzer

A Python script that detects password-guessing (brute-force) attacks in real SSH server logs.

## What it does

- Reads a real OpenSSH server log (2,000 entries)
- Finds every failed login and extracts the attacker's IP address
- Counts failed attempts per IP and ranks them, worst first
- Flags any IP with 5 or more failed attempts as suspicious
- Checks whether any flagged IP later logged in successfully (a likely break-in)

## Results

- One IP made **286 failed login attempts**, a clear automated brute-force attack
- No flagged IP achieved a successful login in this sample
- The break-in alert was validated by injecting a simulated successful login from the top attacker, confirming the detection works

## How to run

1. Install Python 3
2. Download this repository
3. Run: `python log_analyzer.py`

## Limitations and next steps

- Only counts "Failed password" lines; could also track "Invalid user" attempts
- Does not check time order, so a success before the failures would still trigger an alert
- Threshold is fixed at 5; could be made configurable

## Data source

Log data from [Loghub](https://github.com/logpai/loghub), a collection of system logs for research by the LogPAI team.
Zhu, J., He, S., He, P., Liu, J., Lyu, M. R. *Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics.* IEEE ISSRE, 2023.
