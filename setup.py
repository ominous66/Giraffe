from setuptools import find_packages, setup
from typing import List
HYPHEN_E_DOT = "-e ."
# This is the setup script for the Chitti package.
# It defines the package metadata and dependencies.
def get_requirements(file_path:str)->list[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
    requirements = [req.replace("\n", "") for req in requirements] # Remove newline characters
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)  # Remove editable install if present

    return requirements

setup(
    name="Chitti",
    version="0.1.0",
    author="giraffe",
    author_email="giraffe@zoo.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    description="A Python package for zookeeping and animal management"
)