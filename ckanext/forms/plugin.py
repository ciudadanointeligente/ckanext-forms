import os
from ckan.plugins.core import SingletonPlugin, implements
from ckan.plugins.interfaces import IRoutes, IConfigurer

import ckanext.forms


def configure_template_directory(config, relative_path):
    configure_served_directory(config, relative_path, 'extra_template_paths')
    
def configure_public_directory(config, relative_path):
    configure_served_directory(config, relative_path, 'extra_public_paths')

def configure_served_directory(config, relative_path, config_var):
    'Configure serving of public/template directories.'
    assert config_var in ('extra_template_paths', 'extra_public_paths')
    this_dir = os.path.dirname(ckanext.forms.__file__)
    absolute_path = os.path.join(this_dir, relative_path)
    if absolute_path not in config.get(config_var, ''):
        if config.get(config_var):
            config[config_var] += ',' + absolute_path
        else:
            config[config_var] = absolute_path
            
            
class CustomForm(SingletonPlugin):


    implements(IRoutes)
    implements(IConfigurer)
    
    
    def before_map(self, map):
        map.connect('/dataset/new', controller='ckanext.forms.controller:FormsController', action='new')
        map.connect('/dataset/edit/{id}', controller='ckanext.forms.controller:FormsController', action='edit')
        return map
        
        
    def after_map(self, map):
        return map
        
        
    def update_config(self, config):
        configure_template_directory(config, 'templates')
