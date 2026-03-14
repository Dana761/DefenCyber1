# A26 – Research and Implement a System Bug (Race Condition in Python)

## Overview
A race condition is a concurrent programming bug that occurs when two or more threads
access shared data at the same time, leading to inconsistent or incorrect results.

## Vulnerable Program
The file `race_condition.py` demonstrates a race condition by incrementing a shared
counter variable from multiple threads without synchronization.

## Expected vs Actual Output
- Expected: 500,000  
- Actual: varies (incorrect), e.g., 183,203

This shows the race condition bug.

## Fixed Program
The file `race_condition_fixed.py` uses a threading.Lock() to ensure that increments
are performed safely, producing the correct value (500,000) every run.

## Evidence
Screenshots of the buggy and fixed runs are located in the `screenshots/` folder.
