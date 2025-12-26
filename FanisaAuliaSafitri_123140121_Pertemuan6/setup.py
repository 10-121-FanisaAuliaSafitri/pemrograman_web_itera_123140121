from setuptools import setup, find_packages

requires = [
    'pyramid',
    'pyramid_sqlalchemy',
    'sqlalchemy',
    'waitress',
    'zope.sqlalchemy',
]

setup(
    name='manajemen_mk',
    version='0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = manajemen_mk:main',
        ],
    },
)