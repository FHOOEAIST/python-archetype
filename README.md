# Python Archetype

This project contains a simple templating mechanism for creating clean tox-compatible python projects.

**Funfact**: This archetype project was created using the archetype. Archetype-inception :mind-blow:

## Requirements

The archetype project requires [Python](https://www.python.org/downloads/release/python-390/), [PIP](https://pip.pypa.io/en/stable/installing/) and [Tox](https://pypi.org/project/tox/).

### Compatibility

Currently, the archetype is tested for Python 3.7, 3.8 and 3.9. It could work out with other Python versions too, but this was not tested and happens on your own risk.


## Getting started

Clone the project using git, open a CLI in the cloned folder `python-archetype/src/archetype` and call:

```
python archetype.py
```

Afterwards you are prompted to input:
* a project name
* the target python version (e.g. 3.7, 3.8, 3.9, ...)
* the base folder for the created project (basefolder + project name = source of generated project)

Voila, you have created a clean python project.

To adapt or test the project have a look at the detailed description [here](./documentation/Tox.md)

## How to continue?

After the creation of the project follow the steps:

- Update pip if necessary.
- Install tox if necessary
- Fill in your requirements into: `requirements-to-freeze.txt`
- Call: `pip freeze -r requirements-to-freeze.txt > requirements.txt`
- Call: `tox`
- Ready to go

## Contributing

**First make sure to read our [general contribution guidelines](https://fhooeaist.github.io/CONTRIBUTING.html).**
   
## License

Copyright (c) 2020 the original author or authors.
DO NOT ALTER OR REMOVE COPYRIGHT NOTICES.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

## Research

If you are going to use this project as part of a research paper, we would ask you to reference this project by citing
it. 

<TODO zenodo doi>