# dfk-meditation-circle
Sticky9000's fork of 0rtis / dfktools to automatically level up your heroes

### Instructions

1. Install Python on your local machine
2. Copy this repo and replace the following:

`private` // for your private key, in the config.py file
`account_address` // for your 0x address
`level` // for level of the hero you want leveled up
`hero_id` // id of the hero you want leveled up
`meditation.stat2id('luck'), meditation.stat2id('dexterity'), meditation.stat2id('intelligence')` // replace these with the stats you want to pick

You can create copies of the script so that it's templated. 
You can see what values to use in `meditation/meditation.py`

3. Once it is configured to your liking, run it with `python meditate_LCK_AGI_VIT.py`