import os
import importlib
import logging

PLUGIN_FOLDER = 'plugins'
LOG_LEVEL = logging.DEBUG

logging.basicConfig(level=LOG_LEVEL,
                    format='%(asctime)s %(levelname)-6s %(funcName)s:%(lineno)d: %(message)s'
                    )


def import_plugin(plugin_module_name):
    return importlib.import_module(plugin_module_name)


def is_legal_plugin(plugin):
    return not plugin.startswith('__') and not plugin.endswith('pyc')


def get_plugins(plugin_path):
    files = os.listdir(plugin_path)
    print(files)
    return [x.split('.')[0] for x in files if is_legal_plugin(x)]


def get_plugin_name(plugin_name):
    return '{0}.{1}'.format(PLUGIN_FOLDER, plugin_name)


class PluginMgr(object):
    def launch(self):
        for plugin in get_plugins(PLUGIN_FOLDER):
            logging.error("Detected plugin: [{0}]".format(plugin))
            try:
                self._load(plugin)
            except Exception as e:
                logging.debug("Encountered exception, run next plugin.")
                logging.error(e)
            logging.error("----------")

    def _load(self, plugin):
        plugin_name = get_plugin_name(plugin)
        
        logging.info("Loading plugin [{0}]".format(plugin))
        plugin_module_obj = import_plugin(plugin_name)
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
    
x = PluginMgr().launch()