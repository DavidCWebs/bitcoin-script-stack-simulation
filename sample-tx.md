Sample Transaction
==================

Commands
--------

```bash
# Generate address suitable for P2PKH
ADD=$(bitcoin-cli -regtest getnewaddress "" "legacy")

echo $ADD
mwBMQqRc2EKfhrCKYF8r5C1YY5qFHJqVUL

# Send funds (3.14) to the new address
bitcoin-cli -regtest sendtoaddress $ADD 3.14

# This function returns the txid of the relevant transaction:
8f2ac0537dc1c106aaeb3f6b23f27290d4762366963d28c0e42ca76a57cf9a12

# Get raw transaction data
TX=8f2ac0537dc1c106aaeb3f6b23f27290d4762366963d28c0e42ca76a57cf9a12
RAW=$(bitcoin-cli -regtest getrawtransaction "$TX")

# Display with the aid of jq
bitcoin-cli -regtest decoderawtransaction $RAW | jq

```
The decoded transaction looks like this:

```json
{
  "txid": "8f2ac0537dc1c106aaeb3f6b23f27290d4762366963d28c0e42ca76a57cf9a12",
  "hash": "c1fd636d7c691b94956795cf0973ed12efb6479f72af4f872b11cf7085cedced",
  "version": 2,
  "size": 249,
  "vsize": 168,
  "weight": 669,
  "locktime": 0,
  "vin": [
    {
      "txid": "9b23fc8231445d6a40f585a2f022b5e6ed65f8e4ce6bb3971b7bdd2b499eae37",
      "vout": 0,
      "scriptSig": {
        "asm": "00140756ef70f4284e3b3330c502b3d655696e7bae03",
        "hex": "1600140756ef70f4284e3b3330c502b3d655696e7bae03"
      },
      "txinwitness": [
        "30440220422579366145e0c7b352ab948db586781d61122849ebae77fd45ad1f4d752e5c0220766f469a1d4fdf63b236641d43706569dd3abbe83ec7bfc4f0c60e07c68e9a5901",
        "02ab8c032485266c3647153d6b4f19f723453711f45666d1afad31df690d7a30b6"
      ],
      "sequence": 4294967294
    }
  ],
  "vout": [
    {
      "value": 3.14,
      "n": 0,
      "scriptPubKey": {
        "asm": "OP_DUP OP_HASH160 abccfd87163dbcfba881aae7020cdcb6dcc10c2d OP_EQUALVERIFY OP_CHECKSIG",
        "hex": "76a914abccfd87163dbcfba881aae7020cdcb6dcc10c2d88ac",
        "reqSigs": 1,
        "type": "pubkeyhash",
        "addresses": [
          "mwBMQqRc2EKfhrCKYF8r5C1YY5qFHJqVUL"
        ]
      }
    },
    {
      "value": 6.8599664,
      "n": 1,
      "scriptPubKey": {
        "asm": "OP_HASH160 94fe16c053c225b46f0f0fbe60a5b05b415021e2 OP_EQUAL",
        "hex": "a91494fe16c053c225b46f0f0fbe60a5b05b415021e287",
        "reqSigs": 1,
        "type": "scripthash",
        "addresses": [
          "2N6q2P5Yfk6URn5yjgBeTCSQkVFCyUznssM"
        ]
      }
    }
  ]
}

```

Get pubKey of `mwBMQqRc2EKfhrCKYF8r5C1YY5qFHJqVUL`:

```bash
bitcoin-cli -regtest getaddressinfo "mwBMQqRc2EKfhrCKYF8r5C1YY5qFHJqVUL"

# Returns:
{
  "address": "mwBMQqRc2EKfhrCKYF8r5C1YY5qFHJqVUL",
  "scriptPubKey": "76a914abccfd87163dbcfba881aae7020cdcb6dcc10c2d88ac",
  "ismine": true,
  "solvable": true,
  "desc": "pkh([90ba3d87/0'/0'/34']022b93e1e1a361a33efb455448d468a8addb9382e6acd7ed0dffa3b41d526b04aa)#xvx3mnjm",
  "iswatchonly": false,
  "isscript": false,
  "iswitness": false,
  "pubkey": "022b93e1e1a361a33efb455448d468a8addb9382e6acd7ed0dffa3b41d526b04aa",
  "iscompressed": true,
  "label": "",
  "ischange": false,
  "timestamp": 1556042466,
  "hdkeypath": "m/0'/0'/34'",
  "hdseedid": "bec78067267534898a9ae20ebfbe3786cbc99bb3",
  "hdmasterfingerprint": "90ba3d87",
  "labels": [
    {
      "name": "",
      "purpose": "receive"
    }
  ]
}

```

More concisely, set the variable `$PubKey` as so:

```bash
PubKey=$(bitcoin-cli -regtest getaddressinfo "mwBMQqRc2EKfhrCKYF8r5C1YY5qFHJqVUL" | jq -r .pubkey)
```


