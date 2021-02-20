from setuptools import setup

"""
TODO: add this later
with open("README", 'r') as f:
    long_description = f.read()
"""

setup(
   name='misty',
   version='0.1',
   description='mistypy',
   license="MIT",
   #long_description=long_description,
   author='ChrisScarred',
   author_email='scarred.chris@gmail.com',
   url="https://github.com/ChrisScarred",
   packages=['misty'],  #same as name
   install_requires=['requests'] #external packages as dependencies
)