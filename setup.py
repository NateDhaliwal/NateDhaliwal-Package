from setuptools import setup

setup(
    name='natedhaliwal',
    version='1.2.2',
    description='A simple package to help code Python easier. Long functions with difficult parameters? Shortened!',
    author='Nate Dhaliwal',
    author_email='nathaniel.shaan@gmail.com',
    url='https://github.com/NateDhaliwal/NateDhaliwal-Package',
    packages=["natedhaliwal"],
    install_requires=[
      "python>=3.8,<4.0",
      "requests>2.31.0,<3.0.0"
    ],

    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ]
)
