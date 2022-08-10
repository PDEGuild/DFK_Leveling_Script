# dfk-meditation-circle
Sticky9000's fork of 0rtis / dfktools to automatically level up your heroes

### Instructions

0. Consider testing this first on a non-primary wallet so you dont mishandle your private key while learninng. 
1. Install Python on your local machine
2. Copy these files into a folder and make the following customizations:

`private` for your private key, in the config.py file

`account_address` for your 0x address

`level` for level of the hero you want leveled up

`hero_id` id of the hero you want leveled up

`meditation.stat2id('luck'), meditation.stat2id('dexterity'), meditation.stat2id('intelligence')` replace these with the stats you want to pick

> You can create copies of the script so that it's templated, like how I did for LCK DEX INT or VIT DEX INT
> You can see what stat "strings" are available to use in `meditation/meditation.py`

3. Once it is configured to your liking, run it with `python meditate_LCK_AGI_VIT.py`

### Helpful resources

0rtis dfktools: https://github.com/0rtis/dfktools

DirtyCajunRice web3 tool for nft batch transfer: [Web3helper.dfk.af/#/](https://web3helper.dfk.af/#/) (If you want to be extra cautious, use this to transfer your NFTs in bulk to a "sanitized wallet")
