#!/bin/bash

bitcoin-cli -regtest createrawtransaction \
	'[ \
	]' \
	'{"recipient"}'
