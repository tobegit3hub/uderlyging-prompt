from setuptools import setup, find_packages

setup(
    name='underlying-prompts',
    version='0.1.0',
    author="tobe",
    author_email="tobeg3oogle@gmail.com",
    url="https://github.com/tobegit3hub/underlying-prompts",
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
