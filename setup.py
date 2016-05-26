from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='python_mq5_gas_sensor',
    version='0.1',
    description='Library for reading mq5 gas sensor',
    long_description=readme(),
    url='https://github.com/modular-CAT/python_mq5_gas_sensor',
    author='Daniel Smith',
    author_email='',
    license='MIT',
    packages=['python_mq5_gas_sensor'],
    install_requires=[
        'Adafruit_BBIO',
    ],
    zip_safe=False)
