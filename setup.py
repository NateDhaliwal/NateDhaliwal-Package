from setuptools import setup

setup(
    name='natedhaliwal',
    version='1.0.1',
    description='A package that makes Python easier.',
    author='Nate Dhaliwal',
    author_email='nathaniel.shaan@gmail.com',
    url='https://github.com/NateDhaliwal/NateDhaliwal-Package',
    packages=["natedhaliwal"],
    install_requires=[
      "python>=3.7,<4.0",
      "flask>=3.0.0",
      "requests>2.31.0,<3.0.0"
    ],
)
