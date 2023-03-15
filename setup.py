from setuptools import setup
import py2exe

setup(
    name='datenbanken.py',
    version='1.0.0',
    packages=[''],
    url='github.com/mattipunkt/datenbanken.py',
    license='GPL-2.0',
    author='matti',
    author_email='',
    description='Movie-Datenbank für den Informatik-Unterricht',
    console=['projekt.py'],
    install_requires=[
        'prettytable']
)
