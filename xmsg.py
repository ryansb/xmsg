import subprocess
from os.path import expanduser

import fedmsg.config
import fedmsg.meta

config_path = expanduser('~/.fedmsg.d/config.py')
config = fedmsg.config.load_config(filenames=[config_path])
fedmsg.meta.make_processors(**config)


def notification(title, message, icon_url, link):
    subprocess.Popen(['terminal-notifier',
                      '-message', message,
                      '-title', title,
                      '-appIcon', icon_url,
                      '-open', link])

# Yield messages as they're available from a generator
for name, endpoint, topic, msg in fedmsg.tail_messages():
    notification(fedmsg.meta.msg2title(msg, **config),
                 fedmsg.meta.msg2subtitle(msg, **config),
                 fedmsg.meta.msg2secondary_icon(msg, **config),
                 fedmsg.meta.msg2link(msg, **config))
