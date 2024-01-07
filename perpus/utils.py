import bcrypt

def hashPassword(password):
  bytePassword = password.encode('utf-8')
  salt = bcrypt.gensalt()

  hash = bcrypt.hashpw(bytePassword, salt)
  return hash