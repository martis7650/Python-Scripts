import os


def xor_cipher(file_path, key_string):
  file_path = file_path.strip("'\"")

  if not os.path.exists(file_path):
    print(f"\nError: File '{file_path}' not found!")
    return

  if not key_string:
    print("\nError: Please enter password!")
    return

  with open(file_path, "rb") as f:
    data = f.read()

  key_bytes = key_string.encode("utf-8")

  processed_data = bytearray(
      b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data)
  )

  if file_path.endswith(".enc"):
    output_path = file_path[:-4] + ".decrypted"
    action = "Dešifrováno"
  else:
    output_path = file_path + ".enc"
    action = "Zašifrováno"

  with open(output_path, "wb") as f:
    f.write(processed_data)

  print(f"\n{action}! New file is saved as:\n{output_path}")


if __name__ == "__main__":
  print("--- XOR Decoder / Encoder ---")
  path = input("Zadej cestu k souboru (např. /home/user/Desktop/test.txt): ")
  password = input("Enter password (key): ")

  xor_cipher(path, password)
