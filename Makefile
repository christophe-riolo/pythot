VERSION = 0.7.1
DATE = 12/09/2017
RESOURCE_FILE = resources.qrc
RESOURCE = pythot/resources_rc.py
UI_FILES = window.ui operation.ui about.ui help.ui
UI = $(UI_FILES:%.ui=pythot/%.py)
README = README.rst
HELP_FILES = pythot/doc/doc.qch pythot/doc/doc.qhc

test:
	python -m pythot.tests

run: all
	python -m pythot

all: version ui resources help

ui: $(UI)

resources: $(RESOURCE)

help: $(HELP_FILES)

# version updating -------------------------------
version:
	sed -E -i "s/Pythot v[[:digit:]]+(.[[:digit:]]+)*/Pythot v$(VERSION)/" about.ui
	sed -E -i "s#[[:digit:]]{2}/[[:digit:]]{2}/[[:digit:]]{4}#$(DATE)#" about.ui
	sed -E -i "s/version [[:digit:]]+(.[[:digit:]]+)*/version $(VERSION)/" README.rst

# UI compiling -----------------------------------
pythot/%.py: %.ui
	pyuic5 --from-imports -o $@ $<

# Resources compiling ----------------------------
$(RESOURCE): $(RESOURCE_FILE)
	pyrcc5  -o $(RESOURCE) $(RESOURCE_FILE)

# Help files compiling ---------------------------
pythot/doc/doc.qhc: help/project.qhcp pythot/doc/doc.qch
	qcollectiongenerator -o $@ $<

pythot/doc/doc.qch: help/project.qhp
	qhelpgenerator -o $@ $<

help/project.qhcp help/project.qhp: $(README)
	mkdir -p help
	python2 rst2qhc.py $< -o help \
	    --namespace math.pythot \
	    --customfilter "Pythot $(VERSION)"\
	    --create-qhcp\
	    --filterattributes pythot:0.7

# Cleaning ---------------------------------------
clean:
	rm -f $(RESOURCE) $(UI)
	rm -R help
