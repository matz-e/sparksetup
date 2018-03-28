"""Installation setup for bbp.spark
"""

from setuptools import setup

SPARKMANAGER_NAME = 'sparkmanager'
SPARKMANAGER_VERSION = '0.2'


setup(
    name=SPARKMANAGER_NAME,
    version=SPARKMANAGER_VERSION,
    description='A pyspark management framework',
    author='Matthias Wolf',
    author_email='matthias.wolf@epfl.ch',
    license='MIT',
    keywords=['apache-spark'],
    url='https://github.com/matz-e/sparkmanager',
    download_url='https://github.com/matz-e/sparkmanager/archive/{}.tar.gz'.format(SPARKMANAGER_VERSION),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
    packages=[
        'sparkmanager',
    ],
    install_requires=[
        'pyspark',
        'six'
    ],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
        'pytest-cov'
    ],
    scripts=[
        'scripts/sm_cluster'
    ]
)
