#!/usr/bin/env python

from setuptools import setup, find_packages
from admin_tools import VERSION

repo_url = 'https://github.com/django-admin-tools/django-admin-tools'
long_desc = '''
%s

%s
''' % (open('README.rst').read(), open('CHANGELOG').read())

setup(
    name='django-admin-tools',
    version='0.2',
    description='A collection of tools for the django administration interface',
    long_description=long_desc,
    long_description_content_type='text/x-rst',
    author='David Jean Louis',
    author_email='izimobil@gmail.com',
    url=repo_url,
    download_url='https://pypi.python.org/packages/source/d/django-admin-tools/django-admin-tools-%s.tar.gz' % VERSION,
    packages=find_packages(exclude=['test_proj*']),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False,
    install_requires=[
        "django>=2.2",
        'django-libsass',
        'bootstrap-scss @ git+https://github.com/useHTML5/bootstrap-scss.git@0.2#egg=bootstrap-scss',
        'django-compressor',
    ],
)
