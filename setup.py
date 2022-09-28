from setuptools import setup

setup(
    name='cleanup',
    version='0.1.0',
    py_modules=['cleanup'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'cleanup = cleanup:cli',
        ],
    },
)