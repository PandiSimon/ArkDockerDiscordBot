# Discord bot for controlling an ASA Docker Server
Only works with [ARK Ascended Docker image by azixus](https://github.com/azixus/ARK_Ascended_Docker)!

 1. Go to the folder where you want to install the bot, e.g. `cd /etc`
 2. Use `sudo git clone https://github.com/PandiSimon/ArkDockerDiscordBot`
 3. Install the dependencies of Python3 with `sudo pip3 install -r requirements.txt`. Make sure Python3 and Pip3 are installed.
 4. Edit `bot.py` with your own token, id's and container names. `sudo nano bot.py`
 5. Save the file with Ctrl+O and exit with Ctrl+X
 6. Setup the Linux Service according to the following description:

## Setup Linux Service for systemctl
**Servicefile:**
Path: /etc/systemd/system/_name_.service

    [Unit]
    Description=*Discord Bot fuer den ARK Server*
    After=multi-user.target
    [Service]
    Type=simple
    Restart=always
    ExecStart=/usr/bin/python3 */etc/ArkDockerDiscordBot/bot.py*
    [Install]
    WantedBy=multi-user.target

 1. Put the file there for the service to work properly
 2. Remember to change the path, the name and the description
 3. Use  `sudo systemctl daemon-reload`  to reload the services
 4. Start and enable with  `sudo systemctl start *name*.service`  and  `sudo systemctl enable *name*.service`
 5. Check status with  `sudo systemctl status *name*.service`