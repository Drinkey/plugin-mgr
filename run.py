import os
import importlib
import logging

PLUGIN_FOLDER = 'plugins'
LOG_LEVEL = logging.DEBUG

logging.basicConfig(level=LOG_LEVEL,
                    format='%(asctime)s %(levelname)-6s %(funcName)s:%(lineno)d: %(message)s'
                    )


def plugin_loader(plugin_module_name):
    return importlib.import_module(plugin_module_name)

def get_plugins(plugin_path):
    files = os.listdir(plugin_path)
    print(files)
    return [x.split('.')[0] for x in files if not x.startswith('__') and not x.endswith('pyc')]

def get_plugin_name(plugin_name):
    return '{0}.{1}'.format(PLUGIN_FOLDER, plugin_name)

class PluginMgr(object):
    
    def __init__(self):
        for plugin in get_plugins(PLUGIN_FOLDER):
            logging.error("Detected plugin: [{0}]".format(plugin))
            plugin_name = get_plugin_name(plugin)
        
            logging.info("Loading plugin [{0}]".format(plugin))
            plugin_module_obj = plugin_loader(plugin_name)
            logging.debug("Author:{0}".format(plugin_module_obj.__author__))
            logging.debug("Type:{0}".format(plugin_module_obj.__plugin_type__))
        
            logging.debug("plugin: {0}".format(plugin_module_obj))
            class_obj = getattr(plugin_module_obj, plugin.capitalize())
        
            logging.debug("instance: {0}".format(class_obj))
            obj = class_obj()
            # logging.debug(dir(obj))
            logging.debug("invoking execution function")
            obj.run()
            logging.error("Plugin [{0}] execution completed.".format(plugin))
            logging.error("----------")
    
x = PluginMgr()