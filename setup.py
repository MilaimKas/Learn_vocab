from setuptools import setup

setup(
    name='Deutsche_WS',
    version='0.1.0',
    description='Simple application to learn new fr/ge vocabulary',
    url='https://github.com/MilaimKas/Learn_vocab',
    author='Milaim Kas',
    author_email='milaim.kas@gmail.com',
    license='MIT License',
    packages=['pyexample'],
    install_requires=['PySimpleGUI',
                      'tabulate',
                      'googletrans',
                      'mlconjug3',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: All',
        'License :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.9'
    ],
)
