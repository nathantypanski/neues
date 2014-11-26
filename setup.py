from setuptools import setup, find_packages

setup(
    name = "neuepy",
    version = "0.1",
    packages = ['neuepy'],
    package_dir = {'': 'src'},
    scripts = ['src/bin/neues',],
    include_package_data = True,
    install_requires = [
        'feedparser>=5.1.0',
        'pyyaml>=3.10',
        'blessings>=1.6',
    ],

    package_data = {
        'config': ['*.yml'],
    },

    author = "Nathan Typanski",
    author_email = "ndt@nathantypanski.com",
    description = "Read RSS in your terminal, yesterday.",
    license='LICENSE.txt',
    keywords = "",
    url='https://github.com/nathantypanski/neuepy',
)
