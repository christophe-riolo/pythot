from setuptools import setup, find_packages

# Checking install of PyQt5
pyqt5_failed = False
try:
    import PyQt5
except ModuleNotFoundError:
    import pip
    pyqt5_failed = pip.main(['install', 'PyQt5'])

# Actual setup.
setup(
        name="Pythot",
        version="1.0.1b",
        license="GPLv3",
        keywords="math mathematics education linear equation equations",
        classifiers=[
            "Development Status :: 4 - Beta",
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
        scripts=['bin/pythot'],

        setup_requires=["pip"],
        install_requires=['sympy>=1.1'],

        package_data={
            'pythot': ['doc/*.qhc', 'doc/*.qch']
        },
        author="Christophe Riolo",
        author_email="riolo.christophe@gmail.com",
        description="Software for learning first degree linear equation with visual solving."
)

if pyqt5_failed:
    print("\nAutomated install of PyQt5 has failed. Try to install it manually.\n")
