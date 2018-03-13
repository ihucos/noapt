from setuptools import setup

setup(
    name='noapt',
    version='0.6.0',
    description='Install ubuntu packages in other distributions',
    url='https://github.com/ihucos/noapt',
    scripts=['noapt'],
    install_requires=['plash'],
    python_requires='>=3', # plash requires this
)
