from distutils.core import setup

setup(
    name='UnitConverter',
    version='0.1.0',
    author='evilrix',
    author_email='code@evilrix.com',
    packages=['unitconverter', 'unitconverter.test'],
    scripts=['bin/main.py'],
    url='http://pypi.python.org/pypi/UnitConverter/',
    license='LICENSE.txt',
    description='Convert units between different units of imperial and metric.',
    long_description=open('README.txt').read(),
    install_requires=[],
)