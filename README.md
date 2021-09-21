# File-SHare-Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
  </a>
  <a href="https://telegram.me/COLD_ONEZ">
    <img src="https://telegram.me/COLD_ONEZ/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg" width="250">
  </a><br>
  <a href="https://telegram.me/Mo_Tech_YT">
    &nbsp;<img src="https://img.shields.io/badge/MoTech-Channel-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <a href="https://telegram.me/Mo_Tech_Group">
    &nbsp;<img src="https://img.shields.io/badge/MoTech-Group-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <br>
  <a href="https://github.com/COLD-ONEZ/File-SHare-Bot/stargazers">
    <img src="https://img.shields.io/github/stars/COLD-ONEZ/File-SHare-Bot?style=social">
  </a>
  <a href="https://github.com/COLD-ONEZ/File-SHare-Bot/fork">
    <img src="https://img.shields.io/github/forks/COLD-ONEZ/File-SHare-Bot?label=Fork&style=social">
  </a>  
</p>


Telegram Bot To Store Posts And Documents And it Can Access By Special Links.
I Guess This Will Be Usefull For Many People.....😇. 

##

**If you need any more modes in repo or If you find out any bugs, mention in [@Mo_Tech_Group](https://telegram.me/Mo_Tech_Group)**

### Features
- Fully customisable.
- Customisable welcome & Forcesub messages.
- More than one Posts in One Link.
- Can be deployed on heroku directly.

### Setup

- Add the bot to Database Channel with all permission
- Add bot to ForceSub channel as Admin with Invite Users via Link Permission if you enabled ForceSub 

##
### Installation
#### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/COLD-ONEZ/File-SHare-Bot)</br>
<a href="https://youtu.be/ep3u-n_DI_Q">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>

#### Deploy in your VPS
````bash
git clone https://github.com/COLD-ONEZ/File-SHare-Bot
cd File-SHare-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

### Admin Commands

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

/users - view bot statistics

/broadcast - broadcast any messages to bot users
```

### Variables

* `API_HASH` Your API Hash from [@MT_MyTelegramOrg_Bot](https://telegram.me/MT_MyTelegramOrg_Bot)
* `API_ID` Your API ID from [@MT_MyTelegramOrg_Bot](https://telegram.me/MT_MyTelegramOrg_Bot)
* `TG_BOT_TOKEN` Your bot token from [@BotFather](https://telegram.me/BotFather)
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/COLD-ONEZ/File-SHare-Bot/blob/main/README.md#start_message'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub


### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption


## Support   
Join Our [Telegram Group](https://telegram.me/Mo_Tech_Group) For Support/Assistance.     

### Credits

- Thanks To [CodeXBotz](https://t.me/CodeXBotz) & [MoTech](https://t.me/Mo_Tech_YT)

##

   **Star this Repo if you Liked it ⭐⭐⭐**

