#!/usr/bin/python2.7

from setuptools import setup

setup(
    name='Crypto-Notifier',
    version='1.0.3',
    description='Get the latest rates of popular Cryptocurrencies',
    long_description='This python package notifies the user of the current market rates of popular Cryptocurrencies',
    author='Dushyant Rathore',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stablegit
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords="Cryptocurrency notifier",
    author_email='dushyant.bgs@gmail.com',
    url='https://github.com/dushyantRathore/Crypto-Notifier',
    packages=["cryptonotifier"],
    install_requires=[
        "requests<=2.11.1",
        "beautifulsoup4",
        "notify2"
    ],
entry_points={
        'console_scripts':
            ['cryptonotifier = cryptonotifier.Main:notify']
    }
)