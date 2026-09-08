# Day 05 — Logs + SSH

## System Logs (journalctl)
* Purpose: Query central system logs managed by systemd.
* Key Command:`sudo journalctl -u nginx --since today` (filter Nginx service logs for today).

## Nginx Logs
* Location: `/var/log/nginx/`
* access.log: Record of real-time HTTP requests (includes --- Client IP, Timestamp, Method, Status Code).
* error.log: Records Nginx server errors and diagnostic information.

##  SSH (Secure Shell)
use:Provides encrypted remote shell access over port 22.
Client/Server: An SSH client connects to an active SSH server process (`sshd`)daemon.

## Authentication & Security
Key Pairs:
  Public Key: Shared with the server (acts as the lock)
  Private Key: Kept secret on the client (acts as the key).
Keep port 22 protected behind firewalls and routers, avoid exposing unencrypted or password only SSH to the public internet.
