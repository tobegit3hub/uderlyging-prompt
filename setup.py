from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='underlying-prompts',
    version='0.1.1',
    author="tobe",
    author_email="tobeg3oogle@gmail.com",
    url="https://github.com/tobegit3hub/underlying-prompts",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'requests',
        'flask'
    ],
    entry_points={
        'console_scripts': [
            'underlying-prompts=underlying_prompts.server:main'
        ]
    }
)
