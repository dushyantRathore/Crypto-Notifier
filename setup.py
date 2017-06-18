#!/usr/bin/python2.7

from setuptools import setup

setup(
    name='Crypto-Notfier',
    version='1.0.1',
    description='Get the latest conversion rates of Cryptocurrencies to INR',
    long_description='This python package notifies the user of the conversion rates of popular Cryptocurrencies',
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
        'Programming Language :: Python :: 2'
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
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