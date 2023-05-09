#automatically install the packages 
from setuptools import find_packages,setup
#for converting to list
from typing import List

hypen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the requiremnts as list
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  #read each line in requirements file
        # while reading, each line create a \n so replacing \n with blank
        requirements = [req.replace("\n","") for req in requirements] 

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)


#metadata of ml application
setup(
            name = 'mlproject',
            version = '0.0.1',
            author = 'Madhan',
            author_email = 'madhanbalasukumar@gmail.com',
            packages = find_packages(),   #will the packages on folder scr and file __init__.py
            install_requires=get_requirements('requirements.txt')  # to install the packages from requiremnts file
)
