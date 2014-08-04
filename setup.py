from distutils.core import setup

setup(
    name='spotpersist',
    version='0.1.1',
    author='Casey Link',
    author_email='unnamedrambler@gmail.com',
    packages=['spotpersist'],
    scripts=['bin/spot-persist','bin/spot-fetch', 'bin/spot-cartodb-sync'],
    url='a url',
    license='LICENSE',
    description='Tools for fetching and working with data from SPOT GPS Messengers',
    long_description=open('README.md').read(),
    install_requires=[
        "SQLAlchemy >= 0.7.9",
    ],
)
