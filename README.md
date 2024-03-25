# RPGMakerMVSaveEditor

I noticed how the website SaveEditOnline (https://www.saveeditonline.com/) does not have the ability to edit switches in .rpgmaker files.
So I decided to make my own editor.

This editor uses the LZstring library (https://pypi.org/project/lzstring/) in order to decode and encode .rpgmaker files.
In order to use this program, install the LZstring library using PIP and run the following command:

python3 path/to/saveedit.py -input path/to/save/file -output output/path/directory (uses ./ as default)

This program does not include the ability to decode variable and item names like SaveEditOnline sadly.


# I am unsure if this program works for other RPGMaker versions as I only have OMORI to test this program on.
If you want to edit OMORI save file switches use this website (https://goats.dev/omori/) in order to find the variable/switch ID.
