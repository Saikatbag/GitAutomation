########################## project Github automation##########################################
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# Github repository which automatically sends an event (webhook) on the following
# Github actions ("Push", "Pull Request", "Merge") to a registered endpoint, and store it to
# MongoDB.The UI will keep pulling data from MongoDB every 15 seconds and display the latest
# changes to the repo.
# ---------------------------------------------------------------------------------------------
# first you chack, your python version using this command
# ~python3 --version (linux, Mac)
# ~python --version (windows)
# when not install python then go to "https://www.python.org/downloads/" and downlod and install.
 
# second point, creat a vartual enverment. (this is optional )
# ~pip install virtualenv (install vartualenv )
# ~vartualenv venv (creat a vartual enverment "venv" name)
# ~source venv/bin/activate (activate the vartual env)
# then this type of screen you can see- (venv) vaio@vaio-S:~/Desktop/Project$ 

# 3rd point, install Flack and py mongo 
# ~pip install Flack
# ~pip install pymongo

# 4th point you also install mongo db database ,
# if not install your pc then goto 'https://www.mongodb.com/try/download/community' and downlod then install .

# 5th point, you also install ngrok,
# if not install in your pc goto "https://ngrok.com/download" folw this instraction,

# then Run This
# ~python3 run.py ( For run this app)
# folowing ip adress open your web page,
# ~ngrok http 5000 ( my program run 5000 port )
# --------------------------------------------------------------------------------------------------------
# but not work this time , you can not set webhook in your git account. you set your ngrok web address in your git account.
# go to Github diractory >setting tab> webhook> then creat new webhook > and past this ngrock address. 
# also selict "application/jason" and "Send me everything".

# then creat pull Request , marge, and push
# ======================================================================================================

















