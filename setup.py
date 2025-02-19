from setuptools import find_packages,setup


AUTHOR_USER_NAME='DhanushKumarb'
REPO_NAME='Application'

def get_requirements(file_path:str='requirements.txt'):
    try:
        with open(file_path,'r') as f:
            return [line.strip() for line in f.readlines() if line.strip() and line.strip()!='-e .']
    except FileNotFoundError:
        return [] 
print(get_requirements())
setup(
    name='Machine learning project',
    version='0.0.0',
    author=AUTHOR_USER_NAME,
    author_email='dk071849@gmail.com',
    description='creating end to end project',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug  Report":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements()
)