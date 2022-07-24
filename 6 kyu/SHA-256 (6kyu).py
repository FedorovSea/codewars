import hashlib
def to_sha256(s):
    hasked_string = s.encode()
    return hashlib.sha256(hasked_string).hexdigest()