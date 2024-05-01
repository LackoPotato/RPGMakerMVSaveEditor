# RPGMakerMVSaveEditor

I noticed how the website SaveEditOnline (https://www.saveeditonline.com/) does not have the ability to edit switches in .rpgmaker files.
So I decided to make my own editor.

This editor uses the LZstring library (https://pypi.org/project/lzstring/) in order to decode and encode .rpgmaker files.
In order to use this program, install the LZstring library using PIP and run the following command:

python3 path/to/saveedit.py -input path/to/save/file -output output/path/directory (uses ./ as default)

This program does not include the ability to decode variables and item names like SaveEditOnline sadly.

This is mainly done as a programming challenge and there should may be better websites in order to accomplish this same task.

# Dependents
Depends on LZstring - https://pypi.org/project/lzstring/

