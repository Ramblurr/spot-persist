from distutils.core import setup

setup(
    name='spot-persist',
    version='0.1.0',
    author='Casey Link',
    author_email='unnamedrambler@gmail.com',
    packages=['spotpersist'],
    scripts=['bin/spot-persist','bin/spot-fetch'],
    url='a url',
    license='LICENSE',
    description='Tools for fetching and working with data from SPOT GPS Messengers',
    long_description=open('README.md').read(),
    install_requires=[
        "SQLAlchemy >= 0.7.9",
    ],
)
