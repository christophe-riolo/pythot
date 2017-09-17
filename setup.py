from setuptools import setup, find_packages

# Checking install of PyQt5
pyqt5_failed = False
try:
    import PyQt5
except ModuleNotFoundError:
    import pip
    pyqt5_failed = pip.main(['install', 'PyQt5'])

# Fiw for bdist_wininst codec fail
import codecs
try:
    codecs.lookup("mbcs")
except LookupError:
    ascii = codecs.lookup("ascii")
    func = lambda name, enc=ascii: {True: enc}.get(name=="mbcs")
    codecs.register(func)

# Actual setup.
setup(
        name="Pythot",
        version="0.9.1",
        license="GPLv3",
        keywords="math mathematics education linear equation equations",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Environment :: X11 Applications :: Qt",
            "Intended Audience :: Education",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Natural Language :: French",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Topic :: Education",
            "Topic :: Scientific/Engineering :: Mathematics"
            ],
        packages=find_packages(),

        setup_requires=["pip"],
        install_requires=['sympy>=1.1'],

        package_data={
            '': ['*.qhc', '*.qch']
        },
        author="Christophe Riolo",
        author_email="riolo.christophe@gmail.com",
        description="Software for learning first degree linear equation with visual solving."
)

if pyqt5_failed:
    print("\nAutomated install of PyQt5 has failed. Try to install it manually.\n")
