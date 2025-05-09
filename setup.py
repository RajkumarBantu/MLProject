from setuptools import find_packages,setup
from typing import List

Hype = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if Hype in requirements:
            requirements.remove(Hype)
    return requirements

        



setup(
    name='ML Project',
    version='0.0.1',
    Author = 'Rajkumar Bantu',
    Email = 'rajbantu801@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)