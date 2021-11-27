# Chatbot-szy
It is a fantastic project for me 
First install the VirtualBox.The development of RASA system requires virtual machines. Linux environment is more suitable for the development of rasa. Windows system will cause many inexplicable errors
Open the virtual machine, download a compiler and import my project
Then use the command line to create a folder on the desktop as the virtual environment, and then activate it to install the rasa environment. The command line goes to the rasa official website to find something similar to this
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -U --user pip && pip3 install rasa
The update will change over time, so everything is based on the latest release on the official website
Then the command line should start action first(IN the compiler)
 rasa run action
Open another command line rasa train to build the model
Then rasa shell is used in the compiler.
If you want to have a page, Download rasa-x from the external command line
It is also based on the official website
rasa run --cors "*" --enable-api --port 5005
