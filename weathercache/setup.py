from setuptools import setup

setup(
    name='weathercache',
    packages=['weathercache'],
    include_package_data=True,
    install_requires=[
        'flask==2.0.1',
    ],
)