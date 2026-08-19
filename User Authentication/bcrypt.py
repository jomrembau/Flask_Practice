from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

login_password = "Bobo"

pw_hash = bcrypt.generate_password_hash(login_password)

check_password = bcrypt.check_password_hash(pw_hash, 'hunter2')

print(check_password)