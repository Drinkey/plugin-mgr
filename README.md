# plugin-mgr

Just a simple demo of a plugin management framework.

The plugin can be added without modifying other modules. We can develop the features easily in parallel.

## environment

Python 3.6.3 (install by brew)
Mac OSX 10.13.4

## log sample

```
$ python run.py
['lastline.py', 'cyren.py', 'bitdefender.py', '__init__.py', 'badplugin.py', 'webblocker.py']
2020-11-18 15:10:06,886 ERROR  launch:34: Detected plugin: [lastline]
2020-11-18 15:10:06,886 INFO   _load:45: Loading plugin [lastline]
2020-11-18 15:10:06,892 DEBUG  _load:47: Author:Jason B
2020-11-18 15:10:06,892 DEBUG  _load:48: Type:services
2020-11-18 15:10:06,892 DEBUG  _load:50: plugin: <module 'plugins.lastline' from '/Users/user/github.com/plugin-mgr/plugins/lastline.py'>
2020-11-18 15:10:06,892 DEBUG  _load:53: instance: <class 'plugins.lastline.Lastline'>
2020-11-18 15:10:06,892 DEBUG  __init__:6: [init] launching monitor
2020-11-18 15:10:06,892 DEBUG  _load:56: invoking execution function
2020-11-18 15:10:06,892 ERROR  run:9: this is lastline run
2020-11-18 15:10:06,892 ERROR  _load:58: Plugin [lastline] execution completed.
2020-11-18 15:10:06,892 INFO   __del__:12: exit plugin
2020-11-18 15:10:06,892 ERROR  launch:40: ----------
2020-11-18 15:10:06,892 ERROR  launch:34: Detected plugin: [cyren]
2020-11-18 15:10:06,892 INFO   _load:45: Loading plugin [cyren]
2020-11-18 15:10:06,894 DEBUG  _load:47: Author:Winter
2020-11-18 15:10:06,895 DEBUG  _load:48: Type:feeds
2020-11-18 15:10:06,895 DEBUG  _load:50: plugin: <module 'plugins.cyren' from '/Users/juser/github.complugin-mgr/plugins/cyren.py'>
2020-11-18 15:10:06,895 DEBUG  _load:53: instance: <class 'plugins.cyren.Cyren'>
2020-11-18 15:10:06,895 DEBUG  __init__:6: [init] launching monitor
2020-11-18 15:10:06,895 DEBUG  _load:56: invoking execution function
2020-11-18 15:10:06,895 ERROR  run:10: this is Cyren run
2020-11-18 15:10:06,895 ERROR  _load:58: Plugin [cyren] execution completed.
2020-11-18 15:10:06,895 ERROR  launch:40: ----------
2020-11-18 15:10:06,895 ERROR  launch:34: Detected plugin: [bitdefender]
2020-11-18 15:10:06,895 INFO   _load:45: Loading plugin [bitdefender]
2020-11-18 15:10:06,896 DEBUG  _load:47: Author:Steven Rogers
2020-11-18 15:10:06,897 DEBUG  _load:48: Type:feeds
2020-11-18 15:10:06,897 DEBUG  _load:50: plugin: <module 'plugins.bitdefender' from '/Users/user/github.com/plugin-mgr/plugins/bitdefender.py'>
2020-11-18 15:10:06,897 DEBUG  _load:53: instance: <class 'plugins.bitdefender.Bitdefender'>
2020-11-18 15:10:06,897 DEBUG  __init__:6: [init] launching monitor
2020-11-18 15:10:06,897 DEBUG  _load:56: invoking execution function
2020-11-18 15:10:06,897 ERROR  run:9: this is Bitdefender run
2020-11-18 15:10:06,897 ERROR  _load:58: Plugin [bitdefender] execution completed.
2020-11-18 15:10:06,897 ERROR  launch:40: ----------
2020-11-18 15:10:06,897 ERROR  launch:34: Detected plugin: [badplugin]
2020-11-18 15:10:06,897 INFO   _load:45: Loading plugin [badplugin]
2020-11-18 15:10:06,898 DEBUG  launch:38: Encountered exception, but continue execution.
2020-11-18 15:10:06,898 ERROR  launch:39: module 'plugins.badplugin' has no attribute '__author__'
2020-11-18 15:10:06,939 ERROR  launch:40: ----------
2020-11-18 15:10:06,939 ERROR  launch:34: Detected plugin: [webblocker]
2020-11-18 15:10:06,939 INFO   _load:45: Loading plugin [webblocker]
2020-11-18 15:10:06,941 DEBUG  _load:47: Author:Jay Chou
2020-11-18 15:10:06,942 DEBUG  _load:48: Type:services
2020-11-18 15:10:06,942 DEBUG  _load:50: plugin: <module 'plugins.webblocker' from '/Users/user/github.com/plugin-mgr/plugins/webblocker.py'>
2020-11-18 15:10:06,942 DEBUG  _load:53: instance: <class 'plugins.webblocker.Webblocker'>
2020-11-18 15:10:06,942 DEBUG  __init__:6: [init] launching monitor
2020-11-18 15:10:06,942 DEBUG  _load:56: invoking execution function
2020-11-18 15:10:06,942 ERROR  run:9: this is Webblocker run
2020-11-18 15:10:06,942 ERROR  _load:58: Plugin [webblocker] execution completed.
2020-11-18 15:10:06,942 INFO   __del__:12: exit plugin
2020-11-18 15:10:06,942 ERROR  launch:40: ----------
```

