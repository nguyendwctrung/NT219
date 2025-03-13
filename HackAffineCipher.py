import string

def gcd(a, b):
    """Compute the Greatest Common Divisor (Euclid's Algorithm)."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """
    Computes the modular inverse of a modulo m using a simple brute-force approach.
    Returns the inverse if it exists, else None.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(ciphertext, a, b):
    """
    Decrypts the input text using the Affine cipher with keys a and b.
    Computes the modular inverse of a and applies the decryption formula:
      D(y) = a_inv * (y - b) mod 26.
    """
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return None

    alphabets = string.ascii_uppercase
    plaintext_chars = []
    for ch in ciphertext:
        if ch.isalpha():
            offset_char = ch.upper()
            y = ord(offset_char) - ord('A')
            x = (a_inv * (y - b)) % 26
            decrypted_char = alphabets[x]
            if ch.islower():
                decrypted_char = decrypted_char.lower()
            plaintext_chars.append(decrypted_char)
        else:
            plaintext_chars.append(ch)
    return "".join(plaintext_chars)

def brute_force_affine(ciphertext):
    """
    For each pair (a, b), with a coprime 26 and b from 0..25
    Return list(a, b, decrypted)
    """
    results = []
    for a_val in range(1, 26):
        if gcd(a_val, 26) == 1:  # a_val and 26 must coprime
            for b_val in range(26):
                decrypted = affine_decrypt(ciphertext, a_val, b_val)
                if decrypted is not None:
                    results.append((a_val, b_val, decrypted))
    return results

def main():
    cipher_text = input("\nEnter the text to decrypt: ")

    all_decryptions = brute_force_affine(cipher_text)

    for index, (a_val, b_val, decrypted) in enumerate(all_decryptions, start=1):
        print(f"\n-- {index}/{len(all_decryptions)} --")
        print(f"(a = {a_val}, b = {b_val}):\n{decrypted}")
        user_input = input(f"\n--Press Enter to continue. "
                           "Press 'q' to exit: ")
        if user_input.lower() == 'q':
            break

if __name__ == "__main__":
    main()
