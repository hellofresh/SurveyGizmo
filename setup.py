from setuptools import setup, find_packages

setup(
    name='surveygizmoHF',
    version="1.0.0",
    description='A Python Wrapper for SurveyGizmo\'s restful API service.',
    author='Ryan P Kilby',
    author_email='rpkilby@ncsu.edu',
    keywords="Survey Gizmo SurveyGizmo surveygizmo",
    packages=find_packages(),
    install_requires=['requests==2.11.1', 'rauth==0.7.2'],
    license='BSD License',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
