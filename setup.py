from setuptools import setup


setup(
    name='report',
    version='0.1',
    py_modules=['report'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        report=report:generate_report
    '''
)