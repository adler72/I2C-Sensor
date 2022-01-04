from setuptools import setup

setup(name='I2CSensor',
      version='0.0.1',
      description='CraftBeerPi Plugin',
      author='Marc Adler',
      author_email='aeda@gmx.de',
      url='https://github.com/adler72/I2C-Sensor',
      license='GPLv3',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'I2CSensor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['I2CSensor'],
     )
