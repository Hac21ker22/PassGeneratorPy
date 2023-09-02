import secrets
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + "[]{}#()*;._-"
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

length = 10
password = generate_password(length)
print("Passwort wird generiert... Das Passwort lautet:", password)
