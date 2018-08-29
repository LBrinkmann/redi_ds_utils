from setuptools import find_packages, setup

# configure these
PACKAGE_NAME = 'redi-datascience-utils'
MODULE_NAME = 'redi'
VERSION = '0.0.4'

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    packages=find_packages(),
    install_requires=[
            'matplotlib',
            'seaborn',
            'numpy',
            'pandas',
            'ipdb'
        ],

    extras_require={
        'dev': []
    },

    cmdclass={
    },

    scripts=[
    ],

    # run `python3 setup.py prepare_build`
    # followed by `python3 setup.py bdist`
    # then you can check the `build` folder to see if your package data is included in
    # the binary distribution
    package_data={
        '': [
            'resources/*',
            'config/*'
        ]
    }
)
