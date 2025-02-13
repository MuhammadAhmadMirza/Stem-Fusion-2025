import sys
import io
import os
import tempfile
import builtins
from ciphers import *

# Helper: Override input to always return "c"
original_input = builtins.input
builtins.input = lambda prompt="": "c"

def run_test(func, input_value, key, expected, test_name, use_key=True):
    old_stdout = sys.stdout
    captured = io.StringIO()
    sys.stdout = captured
    try:
        if use_key:
            func(input_value, key)
        else:
            func(input_value)
    except Exception as e:
        sys.stdout = old_stdout
        print(f"FAIL: {test_name}: Exception occurred: {e}")
        return
    sys.stdout = old_stdout
    output = captured.getvalue()
    lines = output.splitlines()
    result_line = None
    for line in lines:
        if "Print result to console" in line or "Result saved to" in line:
            continue
        result_line = line.strip()
        break
    if result_line == expected:
        print(f"PASS: {test_name}")
    else:
        print(f"FAIL: {test_name}: expected '{expected}', got '{result_line}'")

def test_reverse_cipher():
    run_test(reverse_cipher, "hello", None, "olleh", "reverse_cipher with direct text", use_key=False)
    with tempfile.NamedTemporaryFile("w+", delete=False) as tmp:
        tmp.write("Python")
        tmp_path = tmp.name
    run_test(reverse_cipher, tmp_path, None, "nohtyP", "reverse_cipher with file input", use_key=False)
    os.remove(tmp_path)

def test_substitution_cipher():
    key = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    run_test(substitution_cipher, "ABC", key, "ZYX", "substitution_cipher with 'ABC'")
    run_test(substitution_cipher, "abc", key, "zyx", "substitution_cipher with 'abc'")
    run_test(substitution_cipher, "Hello, World!", key, "Svool, Dliow!", "substitution_cipher with punctuation")

def test_vigenere_cipher():
    run_test(vigenere_cipher, "DB", "BC", "CZ", "vigenere_cipher with 'DB' and key 'BC'")
    run_test(vigenere_cipher, "LIPPS", "KEY", "BERFO", "vigenere_cipher with 'LIPPS' and key 'KEY'")
    run_test(vigenere_cipher, "Hello, World!", "KEY", "Xanbk, Yennt!", "vigenere_cipher with punctuation")

def test_caesar_cipher():
    run_test(caesar_cipher, "ABC", "2", "YZA", "caesar_cipher with 'ABC' and key '2'")
    run_test(caesar_cipher, "hello", "3", "ebiil", "caesar_cipher with 'hello' and key '3'")
    run_test(caesar_cipher, "Hello, World!", "5", "Czggj, Rjmgy!", "caesar_cipher with punctuation")

def test_modulo_cipher():
    run_test(modulo_cipher, "AB", "3", "AJ", "modulo_cipher with 'AB' and key '3'")
    run_test(modulo_cipher, "Modulo", "5", "Silexi", "modulo_cipher with 'Modulo' and key '5'")
    run_test(modulo_cipher, "A1B2", "3", "A1J2", "modulo_cipher with numbers")

def test_base64_decode():
    run_test(base64_decode, "SGVsbG8=", "unused", "Hello", "base64_decode with 'SGVsbG8='")
    run_test(base64_decode, "V29ybGQ=", "unused", "World", "base64_decode with 'V29ybGQ='")
    run_test(base64_decode, "U29tZSB0ZXh0", "unused", "Some text", "base64_decode with 'U29tZSB0ZXh0'")

def test_rot_cipher():
    # Test ROT13 decryption (default key)
    run_test(rot_cipher, "uryyb", None, "hello", "rot_cipher with default key (ROT13)")
    # Test ROT cipher with custom key (e.g., key = 5)
    run_test(rot_cipher, "hello", "5", "czggj", "rot_cipher with key '5'")

def main():
    print("Running cipher tests...\n")
    test_reverse_cipher()
    test_substitution_cipher()
    test_vigenere_cipher()
    test_caesar_cipher()
    test_modulo_cipher()
    test_base64_decode()
    test_rot_cipher()
    print("\nAll tests completed.")

if __name__ == '__main__':
    main()
    builtins.input = original_input
