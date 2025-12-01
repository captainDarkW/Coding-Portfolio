#!/usr/bin/env python3
import re
import time
import sys

def parse_seconds(s: str) -> int:
    s = s.strip()
    if not s:
        raise ValueError("empty input")
    mmss = re.match(r'^(\d+):(\d{1,2})$', s)
    if mmss:
        m = int(mmss.group(1))
        sec = int(mmss.group(2))
        if sec >= 60:
            raise ValueError("seconds part must be < 60")
        total = m * 60 + sec
    else:
        try:
            total = int(s)
        except ValueError:
            raise ValueError("invalid format; use seconds or MM:SS")
    if total <= 0:
        raise ValueError("time must be positive")
    return total

def run_countdown(seconds: int):
    try:
        for remaining in range(seconds, 0, -1):
            print(f"Time remaining: {remaining} seconds", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nCountdown interrupted.")
        return False
    print("Time's up!")
    return True

def main():
    while True:
        try:
            user = input("Enter countdown time (seconds or MM:SS): ")
        except EOFError:
            print("\nNo input — exiting.")
            break

        try:
            secs = parse_seconds(user)
        except ValueError as e:
            print("Error:", e)
            continue

        completed = run_countdown(secs)
        if not completed:
            # interrupted by Ctrl+C
            break

        again = input("Restart timer with a new time? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()