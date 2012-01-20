from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-forms',
	version=version,
	description="This plugin customizes the form to update a package",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Luis Felipe \xc3\x81lvarez Burgos',
	author_email='falvarez@ciudadanointeligente.cl',
	url='http://www.ciudadanointeligente.cl',
	license='AGPL',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.forms'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	forms=ckanext.forms.plugin:CustomForm
	""",
)
