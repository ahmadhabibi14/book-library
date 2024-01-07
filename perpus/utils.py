import bcrypt

def hashPassword(password):
  bytePassword = password.encode('utf-8')
  salt = bcrypt.gensalt()

  hash = bcrypt.hashpw(bytePassword, salt)
  return hash

def verifyPassword(input_password, hashed_password):
  # Check if the input password matches the hashed password
  return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password.encode('utf-8'))