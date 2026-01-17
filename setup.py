from setuptools import find_packages,setup
from typing import List,Any

hyphen_e = '-e .'

def find_reqrmnts(file_path:str)->List[str]:
    with open(file_path) as rqrs:
        rqrmnts = rqrs.readlines()
        frqs = [r.replace('\n','') for r in rqrmnts]
        if hyphen_e in frqs:
            frqs.remove(hyphen_e)
        return frqs

setup(
    name = 'drugs_data',
    version = '0.0.1',
    author='adiyann13',
    packages = find_packages(),
    install_requires = find_reqrmnts('requirements.txt')
)


 
