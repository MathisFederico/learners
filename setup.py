from setuptools import setup
import os

import versioneer
VERSION = '1.0.4'

with open("readme.md", "r") as readme_file:
    README = readme_file.read()

print(README)

setup(
    name         = "sensorymotor-learners",
    version      = VERSION,
    cmdclass     = versioneer.get_cmdclass(),
    author       = "Fabien Benureau",
    author_email = "fabien.benureau@gmail.com",
    url          = 'github.com/humm/learners.git',
    long_description = README,
    download_url = 'https://github.com/humm/learners/tarball/{}'.format(VERSION),
    maintainer   = 'Fabien Benureau',
    description  = "A collection of simple incremental forward and inverse model learning algorithms",
    license      = "Open Science License (see fabien.benureau.com/openscience.html)",
    keywords     = "learning algorithm",
    packages     = ['learners', 'learners.algorithms', 'learners.operators'],
    install_requires=['scicfg','numpy', 'scipy', 'scikit-learn'],
    # in order to avoid 'zipimport.ZipImportError: bad local file header'
    zip_safe=False,
)
