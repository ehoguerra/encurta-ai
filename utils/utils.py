from models.link import Link

import secrets
import string

def generateCode():
    size = 6
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(secrets.choice(chars) for i in range(size))

        existing_code = Link.query.filter_by(short_code=code).first()

        if not existing_code:
            return code
