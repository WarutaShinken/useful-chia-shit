# useful-chia-shit
shit for chia and it's forks that you may find useful.

## derive_all_addresses.py

Derives the first 500 of each type of address (classic/non-observer and modern/observer/unhardened) from your mnemonics. You will need to install Chia from source to use it.

Simply edit the parameters inside the file (mnemonics prefix if you're deriving fork addresses and maybe the number of addresses to derive), place it under `chia-blockchain/chia`, activate the virtual environment and run `python derive_all_addresses.py`.

## kill.bat

Forcefully kills every process of a Chia/fork client on Windows. This includes:

- Daemon
- GUI
- Crawler
- Farmer
- Full Node
- Harvester
- Introducer
- Seeder
- Timelord (not that there's one for Windows anyway)
- Wallet

Just edit the first 2 line of the script to target the fork and version. Note that you will have to uncomment the 2nd `binpath` definition for forks based on Chia 1.5.1 or higher.

wen linugs version? idk

## hodl_archive

Archive of the list of past HDDcoin HODL programs.

## multi_wallet_sync.sh

If you wanted to sync multiple wallets, you have to switch between them every now and then. This script does this, changing the focus every 10 minutes.

Edit the values at the top of the script, place it under `chia-blockchain`, activate the virtual environment and run the script with `bash multi_wallet_sync.sh`.

wen wandows version? idk