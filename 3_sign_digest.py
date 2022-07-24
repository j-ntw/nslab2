# Signed Message Digest
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64
import traceback
from termcolor import colored

# Generate 1024 bit asymmetric keys
# TODO: Task 3-1
private_key = None

# Extract the RSAPublicKey instance
# TODO: Task 3-2
public_key = None


def enc_digest(filename):
    # Open and read the file to encrypt as bytes
    with open(filename, "rb") as fp:
        file_data = fp.read()

    # Create a Hash instance
    # TODO: Task 3-3

    # Hash the file data to produce the message digest
    # TODO: Task 3-4
    message_digest_bytes = None

    print("hash_bytes", message_digest_bytes)

    # Encrypt the message digest
    # TODO: Task 3-5
    encrypted_message_digest_bytes = None

    # Decrypt the message digest back
    # TODO: Task 3-6
    decrypted_message_digest_bytes = None

    try:
        print(
            "Original hash bytes: "
            + base64.b64encode(message_digest_bytes).decode("utf8")
        )
        print(
            "Encrypted hash bytes: "
            + base64.b64encode(encrypted_message_digest_bytes).decode("utf8")
        )
        print(
            "Decrypted hash bytes: "
            + base64.b64encode(decrypted_message_digest_bytes).decode("utf8")
        )
    except:
        print("Task 3-1 to 3-6 not implemented")


def sign_digest(filename):
    # Open and read the file to sign as bytes
    with open(filename, "rb") as fp:
        file_data = fp.read()

    # Sign the message digest to produce a signature
    # TODO: Task 3-7
    signature = None

    try:
        print(f"Original data bytes length: {len(file_data)} bytes")
        print(f"Signed message digest length: {len(signature)} bytes")
    except:
        print("Task 3-7 not implemented")

    try:
        # Verify the authenticity of the signed digest using the public_key
        # TODO: Task 3-8
        raise Exception("Task 3-8 not implemented")
        print(colored("======= SIGNATURE VERIFIED =======", "yellow"))
    except Exception as e:
        traceback.print_exc()
        print(colored("======= INVALID SIGNATURE =======", "red"))


if __name__ == "__main__":
    enc_digest("original_files/shorttext.txt")
    enc_digest("original_files/longtext.txt")
    sign_digest("original_files/shorttext.txt")
    sign_digest("original_files/longtext.txt")
