# RPGMakerMVSaveEditor - Edits .rpgsave files

I noticed how the website SaveEditOnline (https://www.saveeditonline.com/) does not have the ability to edit switches in .rpgsave files.
So I decided to make my own editor.

This editor uses the LZstring library (https://pypi.org/project/lzstring/) in order to decode and encode .rpgmaker files.
In order to use this program, install the LZstring library using PIP and run the following command:

python3 (or python on windows) path/to/saveedit.py -input path/to/save/file -output output/path/directory (uses ./ as default)

This program does not include the ability to decode variables and item names like SaveEditOnline sadly.

This is mainly done as a programming challenge and there should may be better websites in order to accomplish this same task.

Like actually, this editor is clunky. But hey, it just works :tm:.

# Dependents
Depends on LZstring - https://pypi.org/project/lzstring/

Also needs Python - https://www.python.org/
