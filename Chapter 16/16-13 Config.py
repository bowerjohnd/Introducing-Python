import configparser
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')

cfg
cfg['french']
cfg['french']['greeting']
cfg['files']['bin']

#works when typed line by line in interpretor