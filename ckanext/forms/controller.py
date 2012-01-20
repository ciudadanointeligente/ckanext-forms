from ckan.controllers.package import PackageController
from ckan.logic import get_action, check_access
from ckan.lib.base import c, model
from ckan.authz import Authorizer
from ckan.logic import NotAuthorized




class FormsController(PackageController):
    package_form = 'custom_package_form.html'
    
    def _setup_template_variables(self, context, data_dict):
        c.groups_authz = get_action('group_list_authz')(context, data_dict)
        data_dict.update({'available_only':True})
        c.groups_available = get_action('group_list_authz')(context, data_dict)
        c.licences = [('', '')] + model.Package.get_license_options()
        c.is_sysadmin = Authorizer().is_sysadmin(c.user)

        ## This is messy as auths take domain object not data_dict
        context_pkg = context.get('package',None)
        pkg = context_pkg or c.pkg
        if pkg:
            try:
                if not context_pkg:
                    context['package'] = pkg
                check_access('package_change_state',context)
                c.auth_for_change_state = True
            except NotAuthorized:
                c.auth_for_change_state = False
