import os
import yaml
import argparse
import importlib
import traceback

def build_with_yaml(opt):
    #1.read yaml file
    data = open(opt.yaml_file).read()
    yaml_json = yaml.load(data)

    #2.get project parent dir, the dir would use yaml dir's parent dir
    path = os.path.realpath(opt.yaml_file)
    yaml_dir_path = os.path.dirname(path)
    yaml_file_name = os.path.basename(path)
    proj_dir_path = os.path.dirname(yaml_dir_path)
    file_name, file_ext = os.path.splitext(yaml_file_name)
    pkg_dir = proj_dir_path + '/ray_' + file_name

    #3 detect all plugin
    generater_path = os.path.realpath(__file__)
    generater_dir_path = os.path.dirname(generater_path)
    plugin_dir_path = generater_dir_path + '/plugin'

    for plugin_name in os.listdir(plugin_dir_path):
        if os.path.isdir(plugin_dir_path + '/' + plugin_name) and plugin_name != '__pycache__':
            try:
                plugin_module = importlib.import_module("build_tools.plugin." + plugin_name)
                plugin_executor = plugin_module.get_plugin_class()
                plugin_instance = plugin_executor(plugin_name, {
                    "target_dir": pkg_dir
                })
                plugin_instance.execute(yaml_json)
                print('found plugin {}'.format(plugin_name))
            except:
                traceback.print_exc()
                pass


    print(yaml_json)





parser = argparse.ArgumentParser(description='Run script to generate/update project')

def parse_options():

    #yaml location
    parser.add_argument('-y', '--yaml', dest='yaml_file', help='yaml location')

    opt = parser.parse_args()
    return opt

if __name__ == '__main__':
    opt = parse_options()
    if opt is None or opt.yaml_file is None:
        parser.print_help()
        exit(-1)

    build_with_yaml(opt)