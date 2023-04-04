import base64
import hashlib


try:
    from secrets import token_urlsafe
except ImportError:
    # token_urlsafe polyfill for Python < 3.6
    import os

    def token_urlsafe(nbytes=None):
        if nbytes is None:
            nbytes = 32
        tok = os.urandom(nbytes)
        return base64.urlsafe_b64encode(tok).rstrip(b"=").decode("ascii")


def generate_code_challenge():
    # Create a code verifier with a length of 128 characters
    code_verifier = token_urlsafe(96)
    hashed_verifier = hashlib.sha256(code_verifier.encode("ascii"))
    code_challenge = base64.urlsafe_b64encode(hashed_verifier.digest())
    code_challenge_without_padding = code_challenge.rstrip(b"=")
    return {
        "code_verifier": code_verifier,
        "code_challenge_method": "S256",
        "code_challenge": code_challenge_without_padding,
    }
