from cryptography.fernet import Fernet

def encrypt_and_decrypt(message):
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    decrypted = f.decrypt(encrypted).decode()
    return decrypted

# This program depends on a library that is known to have different pre-built wheels for x86_64 and
# aarch64 Linux, and is meant to demonstrate that the universal requirements lock file that uv
# generates enables building and running applications successfully on different platform
# architectures.
# 
# To run on x86_64 Linux:
#   bazel run -c opt --platforms=//plaforms:linux_x86_64 //src:multi_platform_support_test
# 
# To run on aarch64 Linux:
#   bazel run -c opt --platforms=//plaforms:linux_aarch64 //src:multi_platform_support_test
if __name__ == "__main__":
    original_message = "Hello, Bazel!"
    result = encrypt_and_decrypt(original_message)
    assert result == original_message, "Encryption and decryption failed"
    print("Success: ", result)
