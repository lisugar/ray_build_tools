import os
import shutil
from build_tools.plugin.jinja2_executor import Jinja2Plugin

def test():
    return "test"

class FirePlugin(Jinja2Plugin):

    def execute(self, yaml_json):
        print('exeute {} on {}'.format(self.__class__.__name__, self.metadata.get('target_dir')))
        self.gen_input = yaml_json

        #needs to loop gen dir, and create similar structure in target dir
        self.target_dir = self.metadata.get('target_dir')
        self.target_gen_dir = self.target_dir + '/gen'

        path = os.path.realpath(__file__)
        self.base_dir = os.path.dirname(path)
        self.gen_dir = self.base_dir + '/gen'
        self.generate_files(self.gen_dir, self.target_gen_dir)
        pass


