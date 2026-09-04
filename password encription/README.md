# Password Encryption

Local password manager that encrypts saved passwords with Fernet.

## Requirements
```bash
pip install cryptography
```

## Files
- `password_manager.py` — main app
- `key.key` — encryption key (auto-created; do not commit)
- `passwords.txt` — encrypted passwords (do not commit)

## Run
```bash
cd "password encription"
python password_manager.py
```

Commands: `view` / `v`, `add` / `a`, `q` to quit.
