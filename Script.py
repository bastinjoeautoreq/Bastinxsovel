class script(object):
    START_TXT = """ð·ð´ð»ð¾ {},
ð¼ð ð½ð°ð¼ð´ ð¸ð <a href=https://t.me/{}>{}</a>, ð¸ ð²ð°ð½ ð¿ðð¾ðð¸ð³ð´ ð¼ð¾ðð¸ð´ð, ð¹ððð ð°ð³ð³ ð¼ð´ ðð¾ ðð¾ðð ð¶ðð¾ðð¿ ð°ð½ð³ ð´ð½ð¹ð¾ð ð"""
    HELP_TXT = """ð·ð´ð {}
ð·ð´ðð´ ð¸ð ðð·ð´ ð·ð´ð»ð¿ ðµð¾ð ð¼ð ð²ð¾ð¼ð¼ð°ð½ð³ð."""
    ABOUT_TXT = """â¯ ð¼ð ð½ð°ð¼ð´: {}
â¯ ð²ðð´ð°ðð¾ð: <a href=https://t.me/sovel_jaison>sá´á´ á´Ê á´á´Éªsá´É´ {ð®ð³}</a>
â¯ ð»ð¸ð±ðð°ðð: ð¿ððð¾ð¶ðð°ð¼
â¯ ð»ð°ð½ð¶ðð°ð¶ð´: ð¿ððð·ð¾ð½ ð¹
â¯ ð³ð°ðð° ð±ð°ðð´: ð¼ð¾ð½ð¶ð¾ ð³ð±
â¯ ð±ð¾ð ðð´ððð´ð: ðð¿ð
â¯ ð±ðð¸ð»ð³ ððð°ððð: v1.0.1 [ ð±ð´ðð° ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- This is a private project. 
- Source - https://t.me/sovel_jaison  

<b>DEVS:</b>
- <a href=https://t.me/sovel_jaison>sá´á´ á´Ê á´á´Éªsá´É´ {ð®ð³} </a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
â¢ /filter - <code>add a filter in chat</code>
â¢ /filters - <code>list all the filters of a chat</code>
â¢ /del - <code>delete a specific filter in chat</code>
â¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
â¢ /connect  - <code>connect a particular chat to your PM</code>
â¢ /disconnect  - <code>disconnect from a chat</code>
â¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
â¢ /id - <code>get id of a specified user.</code>
â¢ /info  - <code>get information about a user.</code>
â¢ /imdb  - <code>get the film information from IMDb source.</code>
â¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
â¢ /logs - <code>to get the rescent errors</code>
â¢ /stats - <code>to get status of files in db.</code>
â¢ /delete - <code>to delete a specific file from db.</code>
â¢ /users - <code>to get list of my users and ids.</code>
â¢ /chats - <code>to get list of the my chats and ids </code>
â¢ /leave  - <code>to leave from a chat.</code>
â¢ /disable  -  <code>do disable a chat.</code>
â¢ /ban  - <code>to ban a user.</code>
â¢ /unban  - <code>to unban a user.</code>
â¢ /channel - <code>to get list of total connected channels</code>
â¢ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """â ðð¾ðð°ð» ðµð¸ð»ð´ð: <code>{}</code>
â ðð¾ðð°ð» ððð´ðð: <code>{}</code>
â ðð¾ðð°ð» ð²ð·ð°ðð: <code>{}</code>
â ððð´ð³ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±
â ðµðð´ð´ ððð¾ðð°ð¶ð´: <code>{}</code> ð¼ðð±"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
