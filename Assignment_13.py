def caesar_cipher(text, key, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key if mode == "encode" else -key
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print("=== Simple Caesar Cipher ===")

mode = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
message = input("Enter your message: ")
key = int(input("Enter your key (number): "))

output = caesar_cipher(message, key, mode)
print(f"\nYour {mode}d message is:\n{output}")
