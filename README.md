# dffr

The package helps you to find a difference between two mutable Python types.

```python
from dffr.utils import find_diff

>>> find_diff({'a': 1}, {'a': 1, 'b': 2})
defaultdict(list, {'b': [2]})
```
