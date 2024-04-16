# Sheeet

## Installation with pip (+git)
```bash
pip install git+https://github.com/magifind/sheeet.git
```

## Example usage

```python
from sheeet import Sheeet

sht = Sheeet('<your-sheet-url>')

sht.insert([{
    'name': 'John',
    'age': 23,
    'id': i,
} for i in range(10)])

print(sht.all())
```