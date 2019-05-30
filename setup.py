from setuptools import setup, find_packages

requires = [
    'pdfminer.six',
    'numpy',
    'python-dateutil',
    'chardet == 3.0.4'
]

setup(
    name='imrt-qa-data-miner',
    include_package_data=True,
    packages=find_packages(),
    version='0.2',
    description='Scans a directory for IMRT QA results',
    author='Dan Cutright',
    author_email='dan.cutright@gmail.com',
    url='https://github.com/cutright/IMRT-QA-Data-Miner/',
    download_url='https://github.com/cutright/IMRT-QA-Data-Miner/archive/master.zip',
    license="MIT License",
    keywords=['radiation therapy', 'qa', 'research'],
    classifiers=[],
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'imrt-qa-data-miner=imrt-qa-data-miner.main:main',
        ],
    },
    long_description="""IMRT QA Data Miner
    
    This software will iteratively scan all files with in a directory to extract data from IMRT QA reports 
    and generate a csv file.
    """
)