from distutils.core import setup

setup(
    name='dPy',
    version='0.1dev',
    packages=['dpy',],
    long_description=open('README.md').read(),
    
     entry_points = {
        'console_scripts': ['testCmd=dpy.bin:testCmd'],
    }
)