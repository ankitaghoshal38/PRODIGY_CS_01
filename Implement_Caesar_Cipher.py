def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(ch) - base + shift) % 26 + base)
            else:  # decrypt
                result += chr((ord(ch) - base - shift) % 26 + base)
        else:
            result += ch
    return result


def start_cipher():
    print("🔑 Caesar Cipher Tool 🔑")
    while True:
        action = input("\nDo you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

        if action in ["e", "encrypt"]:
            msg = input("Enter your message: ")
            key = int(input("Shift value: "))
            print("👉 Encrypted text:", caesar_cipher(msg, key, "encrypt"))

        elif action in ["d", "decrypt"]:
            msg = input("Enter the encrypted message: ")
            key = int(input("Shift value: "))
            print("👉 Decrypted text:", caesar_cipher(msg, key, "decrypt"))

        else:
            print("⚠️ Invalid option! Choose E or D.")

        again = input("Do you want to try again? (y/n): ").strip().lower()
        if again != "y":
            print("Exiting... Stay secure! 👋")
            break


if __name__ == "__main__":
    start_cipher()
