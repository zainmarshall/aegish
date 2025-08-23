from setuptools import setup, find_packages

setup(
    name='aegish',
    version='0.1.0',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'openai',
        'google-genai',
        'anthropic',
        'ollama',
    ],
    entry_points={
        'console_scripts': [
            'ag = aegish.main:main',
        ],
    },
    author='Zain Marshall',
    description='Natural language to Linux command converter',
    include_package_data=True,
    zip_safe=False,
)
