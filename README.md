# Simple Ransomware

This program is a ransomware which encode files located a $HOME/infection and decoded them as well.

### Context

This ransomware follow severals rules:

- The program will only act on ﬁles whose extensions have been aﬀected by Wannacry.
- The program have to encrypt the contents of the ﬁles in this folder using a key (20 char)
- The program must rename all the ﬁles in the mentioned folder adding the ".ft" extension.

### Usage

```bash
usage: stockholm.py [-h] [-v] [-r] [-s]

This randsomware will encode file at ~/infection/ whose extensions have been affected by Wannacry

options:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  -r, --reverse  Decode encoded files
  -s, --silent   Execute in silent mode
```

### Encode

Files has been encoded with openssl:

- Algorithm `aes-256-cbc` : AES (Advanced Encryption Standard) with a 256-bit key length in Cipher Block Chaining (CBC)  
- Key derivation function: `pbkdf2` :  (Password-Based Key Derivation Function 2) is a method for securely deriving cryptographic keys from a password or passphrase.

#### What is pbkdf2

PBKDF2, which stands for Password-Based Key Derivation Function 2, is a key derivation function used to derive cryptographic keys from a password or passphrase. It plays a crucial role in enhancing the security of the encryption process.

Here's a simplified sequence of the process:

- The passphrase or key material is provided (in your command, it's specified using the -k option).
- PBKDF2 processes this input and derives a secure cryptographic key from it.
- The derived key is then used as the encryption key for the AES-256-CBC algorithm.
- The actual data encryption takes place using AES-256-CBC, with the derived key.
- The encrypted data is written to the output file.

#### Purpose of pbkdf2

- **Protection Against Brute Force Attacks**: By making key derivation slow, it becomes more time-consuming and computationally expensive for an attacker to try a large number of possible keys in a brute force attack.