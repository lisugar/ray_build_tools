import os
import six
import abc
import json
import shutil
from jinja2 import Environment

from build_tools.plugin.base_exectuor import PluginBase

@six.add_metaclass(abc.ABCMeta)
class Jinja2Plugin(PluginBase):

    def render_template_str(self, tmpl_str, input):
        env = Environment(
            extensions=['jinja2.ext.do', 'jinja2.ext.loopcontrols'],
            cache_size=400
        )

        def json_dumps(value):
            return json.dumps(value)

        env.filters['json_dumps'] = json_dumps

        template = env.from_string(tmpl_str)
        return template.render(input)

    def render_template(self, base_file, input):

        tmpl_str = open(base_file).read()
        return self.render_template_str(tmpl_str, input)

    def generate_files(self, base_dir, target_dir):
        if base_dir and os.path.exists(base_dir) and target_dir:
            #ensure target dir always there
            self.mkdirs(target_dir)

            file_list = os.listdir(base_dir)
            if file_list:
                for f in file_list:
                    file_path = base_dir + '/' + f
                    file_name, file_ext = os.path.splitext(f)
                    if file_ext == '.del':
                        #this case is used to delete the original file, which may be not needed in next version
                        if os.path.exists(target_dir + '/' + file_name):
                            if os.path.isdir(target_dir + '/' + file_name):
                                shutil.rmtree(target_dir + '/' + file_name)
                            else:
                                os.remove(target_dir + '/' + file_name)
                    elif file_ext == '.skip':
                        #this would be temp file in generate dir, do nothing
                        pass
                    elif os.path.isdir(file_path):
                        self.generate_files(file_path, target_dir + '/' + f)
                    else:
                        #this is file, just copy to dist
                        if file_ext == '.jinja2':
                            #if file is a jinja2 file, we need to run Jinja2 to render it firstly and write to target dir
                            if '{{' in f:
                                #file name include jinja2
                                for obj in self.gen_input.get('objects'):
                                    self.gen_input['obj'] = obj

                                    file_rendered_name = self.render_template_str(file_name, self.gen_input)

                                    rendered_str = self.render_template(file_path, self.gen_input)
                                    #write to target
                                    with open(target_dir + '/' + file_rendered_name, 'w+') as out_file:
                                        out_file.write(rendered_str)
                                    pass
                            else:
                                rendered_str = self.render_template(file_path, self.gen_input)
                                #write to target
                                with open(target_dir + '/' + file_name, 'w+') as out_file:
                                    out_file.write(rendered_str)
                                pass
                        else:
                            shutil.copy2(file_path, target_dir)