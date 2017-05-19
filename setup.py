from setuptools import setup

dependencies = ['ipython']
extra_packages = {'test': ['pytest', 'pytest-watch', 'pytest-cov']}

setup(
    name="mailroom-madness",
    description="Makes mailroom mad",
    version="0.1",
    author="Erik Enderlein, James Salamonsen",
    author_email="erik.end@gmail.com, jamessalamonsen@gmail.com",
    py_modules=['mailroom'],
    package_dir={'': 'src'},
    install_requires=dependencies,
    extras_require=extra_packages,
    entry_points={
        'console_scripts': [
            'mailroom = mailroom:main']
    }
)
