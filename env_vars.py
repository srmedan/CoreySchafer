import os

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')

print(db_user)
print(db_password)


# How to set  Environment Variables

#1. Go to "Advanced system settings"
#2. "Environment Variables"
#. Add the variable (idealy CAPS LOCK for ) under USER variable