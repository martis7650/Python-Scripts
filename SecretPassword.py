import secrets
import string


def generate_password(length=16):
  alphabet = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(secrets.choice(alphabet) for _ in range(length))
  return password


print("This script using secrets so they are safe.")
print("Password:", generate_password(20))
