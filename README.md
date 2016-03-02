# Wunderlist 2 Todoist
Tool in Python 3 to export Wunderlist data into Todoist.

Bases upon the library *pytodoist* by [Gary](https://github.com/Garee/pytodoist).

If you have any sugestion, please contact me to my [diogojapinto@gmail.com](mailto:diogojapinto@gmail.com?Subject=Contribute%20to%20Wunderlist2Todoist) or submit a pull request.

## Usage

1. Go into your Wunderlist account:
  1. Click on your user icon
  2. Account Settings
  3. Account -> Account Backupt -> Create Backup
2. Make shure you have set a Todoist password (in the case you created the account with Google's login)
3. In a terminal in the destination folder (make sure you have *pip* installed):
  1. $ pip install pytodoist
  2. $ python wunderlist2todoist.py [email] [wunderlist_dump_path]
  3. Input the password when requested
4. Enjoy a service that is being actively developed :wink:

## Tips

* Be careful about leading and trailing white-spaces in your JSON.
