from setuptools import find_packages,setup

REPO_NAME='Application'
AUTHOR_USER_NAME='DhanushKumarb'

def get_requirements(file_path:str='requirements.txt'):
    try:
        with open(file_path,'r') as f:
            return[line.strip() for line in f.readlines() if line.strip() and line.strip()!='-e .']
    except FileNotFoundError:
        return []
    
setup(
    name='Machine_learning_end-to-end',
    version='0.0.0',
    author='DhanushKumarb',
    author_email='dk071849@gmail.com',
    description='a small project to implement end to end',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug_Tracker"=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements()
)
