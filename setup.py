from setuptools import setup

setup(name='I2CSensor',
      version='0.0.1',
      description='CraftBeerPi Plugin',
      author='',
      author_email='',
      url='',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'I2CSensor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['I2CSensor'],
     )