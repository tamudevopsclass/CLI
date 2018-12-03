from setuptools import setup

setup(
    name='groone',
    version='0.1',
    py_modules=['groupcli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        groone=groupcli:cli
    ''',
)
