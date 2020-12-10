# Capture The Flag

## Metasploit CTF 2020
[https://metasploitctf.com/](https://metasploitctf.com/)

This was my first ever CTF challenge. I couldn't dedicate too much time over the specific weekend, but I was able to contribute in a very small way to two of the challenges. A big shout out to the rest of my team who dominated the challenges leaving us ranked 39th out of 413 teams.

### Challenge 1
This involved brute forcing a web login form, but with a slight twist. The challenge hinted towards a valid username and it became apparent that a valid username resulted in a delayed POST response. I decided to write a simple Python script that would iterate over a wordlist of common usernames and record the response times. Any username that resulted in longer than usual response time was likely to be valid. Bingo, "demo".
Script: [response-timer.py](https://github.com/parity0x1/ctf/blob/main/response-timer.py) 
