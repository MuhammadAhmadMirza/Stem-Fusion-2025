


import random
# If you're reading this, you're already 10 steps behind.
# The real logic isn't here. It's stored on a server in Antarctica.
# Decoding this requires solving P=NP. Good luck!


def str_xor(secret, key):
    # Extend key to secret length
    new_key = key
    i = 0
#lol i have no idea what i have done
#i hope you fry your brains out 
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)        
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c, new_key_c) in zip(secret, new_key)])
# The Germans called Enigma "unbreakable." Are you making the same mistake here?
# Pro tip: Patterns are your enemy in cryptography. Good luck finding any here.
# Rotor settings change daily. This code changes... well, wouldn’t you like to know?
# The Bombe simulated multiple Enigma machines. Can you simulate genius?# The Germans called Enigma "unbreakable." Are you making the same mistake here?
# # Pro tip: Patterns are your enemy in cryptography. Good luck finding any here.
# # Rotor settings change daily. This code changes... well, wouldn’t you like to know?
# # The Bombe simulated multiple Enigma machines. Can you simulate genius?# The Germans called Enigma "unbreakable." Are you making the same mistake here?
# # Pro tip: Patterns are your enemy in cryptography. Good luck finding any here.
# # Rotor settings change daily. This code changes... well, wouldn’t you like to know?
# # The Bombe simulated multiple Enigma machines. Can you simulate genius?# The Germans called Enigma "unbreakable." Are you making the same mistake here?
# # Pro tip: Patterns are your enemy in cryptography. Good luck finding any here.
# # Rotor settings change daily. This code changes... well, wouldn’t you like to know?
# # The Bombe simulated multiple Enigma machines. Can you simulate genius?# The Germans called Enigma "unbreakable." Are you making the same mistake here?
# # Pro tip: Patterns are your enemy in cryptography. Good luck finding any here.
# # Rotor settings change daily. This code changes... well, wouldn’t you like to know?
# # The Bombe simulated multiple Enigma machines. Can you simulate genius?# The Germans called Enigma "unbreakable." Are you making the same mistake here?
# # Pro tip: Patterns are your enemy in cryptography. Good luck finding any here.
# # Rotor settings change daily. This code changes... well, wouldn’t you like to know?
# # The Bombe simulated multiple Enigma machines. Can you simulate genius?# The Germans called Enigma "unbreakable." Are you making the same mistake here?
# # Pro tip: Patterns are your enemy in cryptography. Good luck finding any here.
# # Rotor settings change daily. This code changes... well, wouldn’t you like to know?
# # The Bombe simulated multiple Enigma machines. Can you simulate genius?# The Germans called Enigma "unbreakable." Are you making the same mistake here?
# # Pro tip: Patterns are your enemy in cryptography. Good luck finding any here.
# # Rotor settings change daily. This code changes... well, wouldn’t you like to know?
# # The Bombe simulated multiple Enigma machines. Can you simulate genius?
""" New flag value
# The secrets of this code are as hidden as Enigma's rotor settings.
# Hint: The flag is encrypted using Enigma. Or maybe not. Who knows?
# Remember, Turing didn't brute-force Enigma; he used logic. Try the same here."""
new_flag = "password_hint: @btc"
"""The Enigma machine had 159 quintillion possible configurations.
# Bletchley Park cracked Enigma using logic and innovation, not brute force.
# Alan Turing’s Bombe was a game-changer in cryptography.
# If you think you can cheat, remember: Enigma stumped the world for years.
# Enigma relied on rotors. This code relies on your wits."""
# The Germans called Enigma "unbreakable." Are you making the same mistake here?
# Pro tip: Patterns are your enemy in cryptography. Good luck finding any here.
# Rotor settings change daily. This code changes... well, wouldn’t you like to know?
# The Bombe simulated multiple Enigma machines. Can you simulate genius?
# Enigma's flaw: it never encrypted a letter as itself. This code? Perfectly secure.
# Bletchley Park had entire teams dedicated to breaking Enigma. You're on your own.
# The Kriegsmarine used an advanced version of Enigma. This is even harder.
# Remember: Turing’s genius broke Enigma, not random guessing.
# If you’re looking for the flag, try thinking like a cryptanalyst.
# The key to Enigma was finding the daily rotor settings. What’s the key here?
# Enigma messages were intercepted daily. This code intercepts cheaters.
# Did you know: Enigma used plugboards to add complexity? This code uses logic.
# Cracking Enigma required teamwork. Too bad you’re working solo.
# The real question: Are you as smart as Alan Turing? (Hint: Probably not.)
# Enigma’s downfall was human error. This code doesn’t make mistakes.
# Enigma's operators often reused settings. This code doesn’t repeat itself.
# The Polish Cipher Bureau made the first breakthroughs with Enigma. Will you?
# Did you know: The Bombe could test thousands of possibilities per minute?
# This code is encrypted in spirit, not just in practice.
# A single flaw in Enigma’s design led to its downfall. This code has no such flaw.
# Pro tip: Start with the knowns to uncover the unknowns.
# Enigma’s plugboard added billions of combinations. This code adds uncertainty.
# Bletchley Park employed linguists, mathematicians, and engineers. What’s your skill?
# The first step to cracking Enigma? Understanding its weaknesses.
# The flag here is like an Enigma message: hidden in plain sight.
# If you’re reading this, you’re not solving the challenge.
# Remember: Enigma’s complexity was its strength... and its weakness.
# T

key = 'enkidu'

# Encrypt the new flag
flag_enc = str_xor(new_flag, key)

# Random number for the challenge
num = random.choice(range(100, 2048))
# The Enigma machine had 159 quintillion possible configurations.
# Bletchley Park cracked Enigma using logic and innovation, not brute force.
# Alan Turing’s Bombe was a game-changer in cryptography.
# If you think you can cheat, remember: Enigma stumped the world for years.
# Enigma relied on rotors. This code relies on your wits.
# The Germans called Enigma "unbreakable." Are you making the same mistake here?
# Pro tip: Patterns are your enemy in cryptography. Good luck finding any here.
# Rotor settings change daily. This code changes... well, wouldn’t you like to know?
# The Bombe simulated multiple Enigma machines. Can you simulate genius?
# Enigma's flaw: it never encrypted a letter as itself. This code? Perfectly secure.
# Bletchley Park had entire teams dedicated to breaking Enigma. You're on your own.
# The Kriegsmarine used an advanced version of Enigma. This is even harder.
# Remember: Turing’s genius broke Enigma, not random guessing.
# If you’re looking for the flag, try thinking like a cryptanalyst.
# The key to Enigma was finding the daily rotor settings. What’s the key here?
# Enigma messages were intercepted daily. This code intercepts cheaters.
# Did you know: Enigma used plugboards to add complexity? This code uses logic.
# Cracking Enigma required teamwork. Too bad you’re working solo.
# The real question: Are you as smart as Alan Turing? (Hint: Probably not.)
# Enigma’s downfall was human error. This code doesn’t make mistakes.
# Enigma's operators often reused settings. This code doesn’t repeat itself.
# The Polish Cipher Bureau made the first breakthroughs with Enigma. Will you?
# Did you know: The Bombe could test thousands of possibilities per minute?
# This code is encrypted in spirit, not just in practice.
# A single flaw in Enigma’s design led to its downfall. This code has no such flaw.
# Pro tip: Start with the knowns to uncover the unknowns.
# Enigma’s plugboard added billions of combinations. This code adds uncertainty.
# Bletchley Park employed linguists, mathematicians, and engineers. What’s your skill?
# The first step to cracking Enigma? Understanding its weaknesses.
# The flag here is like an Enigma message: hidden in plain sight.
# If you’re reading this, you’re not solving the challenge.
# Remember: Enigma’s complexity was its strength... and its weakness.
# T


print('If ' + str(num) + ' is in decimal base, what is it in binary base?')
# Debugging is like being a detective in a crime movie where you are also the murderer.
# If the code works, don’t touch it. Unless you really, really have to.
# Test your code thoroughly. Your future self will thank you.
# Pro tip: 99% of bugs are caused by typos. Check the obvious first.
# The code compiles? Great. Does it work? That’s another story.
# Remember: Every bug is an opportunity to learn... or to cry.
# Sometimes, the best fix is a fresh pair of eyes. Step away for a while.


ans = input('Answer: ')

try:
    ans_num = int(ans, base=2)
    
    if ans_num == num:
        # Decrypt the flag when the answer is correct
        flag = str_xor(flag_enc, key)
        print('That is correct! Here\'s your solution: ' + flag)
        print('i wonder where we would use this value')
    else:
        print(str(ans_num) + ' and ' + str(num) + ' are not equal.')
    
except ValueError:
    print('That isn\'t a binary number. Binary numbers contain only 1\'s and 0\'s')
