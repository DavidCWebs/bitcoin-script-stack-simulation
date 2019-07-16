Validation Scripts in Bitcoin
=============================
This is an educational project that I'm using to learn about how Bitcoin transactions are validated.

Usage
-----
1. Clone this repo
2. `cd` into the project directory
3. Make a virtual environment: `virtualenv -p python3 venv`
4. `source` the virtual environment activation script - e.g. `source venv/bin/activate`
5. Run `pip install -r requirements.txt`

Pay to Public Key Hash(P2PKH)
-----------------------------
The locking script contains a hashed public key, surrounded by op codes. The fact that the public key is hashed enhances privacy - the locking script is on the blockchain incorporated into an UTXO, but the public key is not exposed in the locking script, only the hashed value.

Locking script:
```
OP_DUP OP_HASH_160 317a5cd184cf5aa6ec86f8e0f510c4bb3cca8658 OP_EQUALVERIFY OP_CHECKSIG
```

To solve this, the spender (i.e. the owner of the hashed public key) needs to provide the original public key 
(i.e. the public  key corresponding to the hash in the locking script) and a valild signature for the key.

The data is provided to the verification script in this order:
```
<signature> <PubK> OP_DUP OP_HASH_I60 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
```
### Stack Contents Step 1
<signature> is pushed onto the stack:

- <signature>

### Stack Contents Step 2
The unhashed (spending) public key is pushed to the stack:

- <PubK>
- <signature>

### Stack Contents Step 3
The OP_DUP opcode is applied, duplicating the top element on the stack and pushing this value onto the top:

- <PubKey>
- <PubKey>
- <signature>

### Stack Contents Step 4
The HASH_160 opcode is applied. This pops and hashes the top stack item: `RIPEMD160(SHA256(PubKey))`, and pushes the result back onto the stack:

- <PubKeyHash>
- <PubKey>
- <signature>

### Stack Contents Step 5
The `<PubKeyHash>` from the locking script is pushed onto the stack:

- <PubKeyHash>
- <PubKeyHash>
- <PubKey>
- <signature>

### Stack Contents Step 6
The OP_EQUALVERIFY opcode is applied. The top two elements are popped and checked for equality. If they are not equal, processing stops here. If they are equal, the process continues:

- <PubKey>
- <signature>

### Stack Contents Step 7
The OP_CHECKSIG opcode is applied. The top two elements in the stack are popped and the signature is checked against the public key. If the signature is valid, `TRUE` is pushed onto the stack.

If the process finishes and the stack has the single element `TRUE`, the transaction is valid.

