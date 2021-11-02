import six
import abc
import os

@six.add_metaclass(abc.ABCMeta)
class PluginBase(object):

    def __init__(self, plugin_name, metadata):
        self.metadata = metadata
        self.plugin_name = plugin_name

    @abc.abstractmethod
    def execute(self, yaml_json):
        raise NotImplementedError('Plugin should implement the method to execute')  # pragma: no cover

    def mkdirs(self, path):
        if os.path.exists(path):
            pass
        else:
            last_part = os.path.basename(path)
            parent_part = os.path.dirname(path)

            self.mkdirs(parent_part)
            os.mkdir(path)