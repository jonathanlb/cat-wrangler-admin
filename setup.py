from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='cat-wrangler-admin',
    version='0.1.0',
    description='Server admin tools for cat-wrangler rsvp system',
    long_description=readme,
    author='Jonathan Bredin',
    author_email='bredin@acm.org',
    url='https://github.com/jonathanlb/cat-wrangler-admin',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
