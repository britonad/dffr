[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/vald-phoenix/dffr/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/vald-phoenix/dffr.svg?branch=master)](https://travis-ci.org/vald-phoenix/dffr?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/vald-phoenix/dffr/badge.svg?branch=master)](https://coveralls.io/github/vald-phoenix/dffr?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a4b5c4f0bd3c4eb9ac4a93e5ecb3c2fa)](https://www.codacy.com/app/vald-phoenix/dffr?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vald-phoenix/dffr&amp;utm_campaign=Badge_Grade)
[![Documentation Status](https://readthedocs.org/projects/dffr/badge/?version=latest)](https://dffr.readthedocs.io/en/latest/?badge=latest)

# dffr
The package helps you to find a difference between two mutable Python types.

## Kick start
Just simply install the package from PyPi:
```bash
pip install dffr
```

## Next steps
Associate the package from a Python console:
```python
>>> from dffr.utils import find_diff
>>> find_diff({'a': 1}, {'a': 1, 'b': 2})
defaultdict(<class 'list'>, {'b': [2]})
```
