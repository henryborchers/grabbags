from setuptools import setup

setup(
    name='grabbags',
    version='0.0.1',
    packages=['grabbags'],
    url='https://github.com/amiaopensource/grabbags',
    license='',
    author='AMIA',
    author_email='',
    description='',
    test_suite='tests',
    install_requires=[
        "bagit"
    ],
    tests_require=[
        'pytest',
    ],
    setup_requires=[
        'pytest'
    ],


)
