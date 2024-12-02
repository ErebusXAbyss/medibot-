from setuptools import find_packages, setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Medical Chatbot',
    version='0.0.0',
    author='nishita',
    author_email='nishirai04@gamil.com',
    packages=find_packages(),
    install_requires=requirements
)
