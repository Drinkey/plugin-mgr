# plugin-mgr

Just a simple demo of a plugin management framework

## environment

Python 3.6.3 (install by brew)
Mac OSX 10.13.4

## log

```
$ python run.py
['lastline.py', 'cyren.py', 'bitdefender.py', 'cyren.pyc', '__init__.py', '__pycache__', 'webblocker.pyc', 'badplugin.py', '__init__.pyc', 'bitdefender.pyc', 'webblocker.py']
2018-06-04 23:16:48,733 ERROR  __init__:28: Detected plugin: [lastline]
2018-06-04 23:16:48,733 INFO   load:39: Loading plugin [lastline]
2018-06-04 23:16:48,735 DEBUG  load:41: Author:Junkai Zhang
2018-06-04 23:16:48,735 DEBUG  load:42: Type:services
2018-06-04 23:16:48,735 DEBUG  load:44: plugin: <module 'plugins.lastline' from '/Users/jkzhang/Code/gitlab/plugin-mgr/plugins/lastline.py'>
2018-06-04 23:16:48,735 DEBUG  load:47: instance: <class 'plugins.lastline.Lastline'>
2018-06-04 23:16:48,735 DEBUG  __init__:5: [init] service monitor
2018-06-04 23:16:48,735 DEBUG  load:50: invoking execution function
2018-06-04 23:16:48,735 ERROR  run:9: this is lastline run
2018-06-04 23:16:48,736 ERROR  load:52: Plugin [lastline] execution completed.
2018-06-04 23:16:48,736 INFO   __del__:12: exit plugin
2018-06-04 23:16:48,736 ERROR  __init__:34: ----------
2018-06-04 23:16:48,736 ERROR  __init__:28: Detected plugin: [cyren]
2018-06-04 23:16:48,736 INFO   load:39: Loading plugin [cyren]
2018-06-04 23:16:48,736 DEBUG  load:41: Author:Junkai Zhang
2018-06-04 23:16:48,737 DEBUG  load:42: Type:in-feed
2018-06-04 23:16:48,737 DEBUG  load:44: plugin: <module 'plugins.cyren' from '/Users/jkzhang/Code/gitlab/plugin-mgr/plugins/cyren.py'>
2018-06-04 23:16:48,737 DEBUG  load:47: instance: <class 'plugins.cyren.Cyren'>
2018-06-04 23:16:48,737 DEBUG  __init__:5: [init] service monitor
2018-06-04 23:16:48,737 DEBUG  load:50: invoking execution function
2018-06-04 23:16:48,737 ERROR  run:10: this is Cyren run
2018-06-04 23:16:48,737 ERROR  load:52: Plugin [cyren] execution completed.
2018-06-04 23:16:48,737 ERROR  __init__:34: ----------
2018-06-04 23:16:48,737 ERROR  __init__:28: Detected plugin: [bitdefender]
2018-06-04 23:16:48,737 INFO   load:39: Loading plugin [bitdefender]
2018-06-04 23:16:48,738 DEBUG  load:41: Author:Junkai Zhang
2018-06-04 23:16:48,738 DEBUG  load:42: Type:in-feed
2018-06-04 23:16:48,738 DEBUG  load:44: plugin: <module 'plugins.bitdefender' from '/Users/jkzhang/Code/gitlab/plugin-mgr/plugins/bitdefender.py'>
2018-06-04 23:16:48,738 DEBUG  load:47: instance: <class 'plugins.bitdefender.Bitdefender'>
2018-06-04 23:16:48,738 DEBUG  __init__:5: [init] service monitor
2018-06-04 23:16:48,739 DEBUG  load:50: invoking execution function
2018-06-04 23:16:48,739 ERROR  run:9: this is Bitdefender run
2018-06-04 23:16:48,739 ERROR  load:52: Plugin [bitdefender] execution completed.
2018-06-04 23:16:48,740 ERROR  __init__:34: ----------
2018-06-04 23:16:48,740 ERROR  __init__:28: Detected plugin: [badplugin]
2018-06-04 23:16:48,740 INFO   load:39: Loading plugin [badplugin]
2018-06-04 23:16:48,741 DEBUG  __init__:32: Encountered exception, but continue execution.
2018-06-04 23:16:48,741 ERROR  __init__:33: module 'plugins.badplugin' has no attribute '__author__'
2018-06-04 23:16:48,741 ERROR  __init__:34: ----------
2018-06-04 23:16:48,741 ERROR  __init__:28: Detected plugin: [webblocker]
2018-06-04 23:16:48,741 INFO   load:39: Loading plugin [webblocker]
2018-06-04 23:16:48,742 DEBUG  load:41: Author:Junkai Zhang
2018-06-04 23:16:48,742 DEBUG  load:42: Type:services
2018-06-04 23:16:48,742 DEBUG  load:44: plugin: <module 'plugins.webblocker' from '/Users/jkzhang/Code/gitlab/plugin-mgr/plugins/webblocker.py'>
2018-06-04 23:16:48,742 DEBUG  load:47: instance: <class 'plugins.webblocker.Webblocker'>
2018-06-04 23:16:48,742 DEBUG  __init__:5: [init] service monitor
2018-06-04 23:16:48,742 DEBUG  load:50: invoking execution function
2018-06-04 23:16:48,742 ERROR  run:9: this is Webblocker run
2018-06-04 23:16:48,743 ERROR  load:52: Plugin [webblocker] execution completed.
2018-06-04 23:16:48,743 INFO   __del__:12: exit plugin
2018-06-04 23:16:48,743 ERROR  __init__:34: ----------
```

