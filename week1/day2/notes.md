# Day 2: Files, Permissions & Users

## Permissions & chmod
- r (read = 4), w (write = 2), x (execute = 1)
- chmod 600: rw------- (owner read/write only)
- chmod 644: rw-r--r-- (owner read/write, group/others read-only)

## Ownership & sudo
- chown user:group filename changes file ownership
- sudo grants administrative privileges to perform restricted tasks

## Users & Groups
- adduser / deluser: create and remove system users
- addgroup: create new user groups
