# Python Dunder Methods Cheat Sheet

Dunder ("double underscore") methods, also called magic methods, let your classes hook into Python's built-in behavior: operators, `len()`, `print()`, `with` blocks, iteration, and more. You rarely call them directly. Python calls them for you.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

---

## Table of Contents

1. [Object Creation & Lifecycle](#1-object-creation--lifecycle)
2. [String Representation](#2-string-representation)
3. [Comparison](#3-comparison)
4. [Arithmetic Operators](#4-arithmetic-operators)
5. [In-Place & Reflected Operators](#5-in-place--reflected-operators)
6. [Unary & Conversion](#6-unary--conversion)
7. [Container Emulation](#7-container-emulation)
8. [Iteration](#8-iteration)
9. [Callable Objects](#9-callable-objects)
10. [Context Managers](#10-context-managers)
11. [Attribute Access](#11-attribute-access)
12. [Descriptors](#12-descriptors)
13. [Class Customization](#13-class-customization)
14. [Async Methods](#14-async-methods)
15. [Copying & Pickling](#15-copying--pickling)
16. [Quick Reference Table](#16-quick-reference-table)

---

## 1. Object Creation & Lifecycle

| Method | Triggered by | Purpose |
|---|---|---|
| `__new__(cls, ...)` | `MyClass()` | Creates the instance (runs before `__init__`) |
| `__init__(self, ...)` | `MyClass()` | Initializes the new instance |
| `__del__(self)` | Garbage collection | Cleanup when the object is destroyed |

```python
class Config:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} destroyed")
```

**Notes**
- Use `__init__` 99% of the time. `__new__` is for immutable types (`int`, `str`, `tuple` subclasses) and singletons.
- `__new__` must return an instance. Usually `return super().__new__(cls)`.
- Don't rely on `__del__` for important cleanup. Use context managers instead.

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

---

## 2. String Representation

| Method | Triggered by | Purpose |
|---|---|---|
| `__str__` | `str(obj)`, `print(obj)` | Human-readable output |
| `__repr__` | `repr(obj)`, REPL, debuggers | Unambiguous, developer-focused output |
| `__format__` | `f"{obj:spec}"`, `format(obj, spec)` | Custom format specs |
| `__bytes__` | `bytes(obj)` | Bytes representation |

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(1, 2)
print(p)        # (1, 2)
print(repr(p))  # Point(1, 2)
```

**Rule of thumb:** always define `__repr__`. Define `__str__` only if you want a prettier user-facing version. If `__str__` is missing, Python falls back to `__repr__`.

---

## 3. Comparison

| Method | Operator |
|---|---|
| `__eq__` | `==` |
| `__ne__` | `!=` |
| `__lt__` | `<` |
| `__le__` | `<=` |
| `__gt__` | `>` |
| `__ge__` | `>=` |
| `__hash__` | `hash(obj)`, use in sets/dict keys |
| `__bool__` | `bool(obj)`, `if obj:` |

```python
from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, major, minor):
        self.major, self.minor = major, minor

    def __eq__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        if not isinstance(other, Version):
            return NotImplemented
        return (self.major, self.minor) < (other.major, other.minor)

    def __hash__(self):
        return hash((self.major, self.minor))
```

**Notes**
- Return `NotImplemented` (not `False`) for unsupported types so Python can try the reflected operation.
- `@total_ordering` generates the other comparisons from `__eq__` + one of `__lt__`/`__le__`/`__gt__`/`__ge__`.
- If you define `__eq__` without `__hash__`, your class becomes unhashable. Define both if the object is immutable.
- `__bool__` falls back to `__len__` if not defined. Otherwise objects are truthy.

---

## 4. Arithmetic Operators

| Method | Operator |
|---|---|
| `__add__` | `+` |
| `__sub__` | `-` |
| `__mul__` | `*` |
| `__truediv__` | `/` |
| `__floordiv__` | `//` |
| `__mod__` | `%` |
| `__pow__` | `**` |
| `__matmul__` | `@` |
| `__and__` | `&` |
| `__or__` | `\|` |
| `__xor__` | `^` |
| `__lshift__` | `<<` |
| `__rshift__` | `>>` |
| `__divmod__` | `divmod()` |

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

print(Vector(1, 2) + Vector(3, 4))  # Vector(4, 6)
print(Vector(1, 2) * 3)             # Vector(3, 6)
```

---

## 5. In-Place & Reflected Operators

**Reflected (`__radd__`, `__rsub__`, `__rmul__`, ...)** run when the left operand doesn't know how to handle the right one.

```python
# 3 * Vector(1, 2)  ->  int.__mul__ fails -> Vector.__rmul__ is tried
def __rmul__(self, scalar):
    return self * scalar
```

**In-place (`__iadd__`, `__isub__`, `__imul__`, ...)** run for `+=`, `-=`, `*=`, etc. If not defined, Python falls back to the regular operator and rebinds the name.

```python
class Bag:
    def __init__(self):
        self.items = []

    def __iadd__(self, item):
        self.items.append(item)
        return self  # must return the result

b = Bag()
b += "apple"
b += "pear"
print(b.items)  # ['apple', 'pear']
```

Full families: `__radd__`, `__rsub__`, `__rmul__`, `__rtruediv__`, ... and `__iadd__`, `__isub__`, `__imul__`, `__itruediv__`, ...

---

## 6. Unary & Conversion

| Method | Triggered by |
|---|---|
| `__neg__` | `-obj` |
| `__pos__` | `+obj` |
| `__abs__` | `abs(obj)` |
| `__invert__` | `~obj` |
| `__int__` | `int(obj)` |
| `__float__` | `float(obj)` |
| `__complex__` | `complex(obj)` |
| `__index__` | Use as an index/slice, `bin()`, `hex()`, `oct()` |
| `__round__` | `round(obj, n)` |
| `__trunc__`, `__floor__`, `__ceil__` | `math.trunc/floor/ceil` |

```python
class Money:
    def __init__(self, cents):
        self.cents = cents

    def __float__(self):
        return self.cents / 100

    def __abs__(self):
        return Money(abs(self.cents))

    def __neg__(self):
        return Money(-self.cents)
```

`__index__` must return an `int` and lets your object work anywhere Python needs an integer (e.g. `my_list[obj]`).

---

## 7. Container Emulation

| Method | Triggered by |
|---|---|
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[key]` |
| `__setitem__` | `obj[key] = value` |
| `__delitem__` | `del obj[key]` |
| `__contains__` | `x in obj` |
| `__missing__` | `dict` subclass, when a key is not found |
| `__reversed__` | `reversed(obj)` |
| `__length_hint__` | Size estimate for iterators (`operator.length_hint`) |

```python
class Playlist:
    def __init__(self, songs):
        self._songs = list(songs)

    def __len__(self):
        return len(self._songs)

    def __getitem__(self, index):      # also handles slices
        return self._songs[index]

    def __setitem__(self, index, value):
        self._songs[index] = value

    def __delitem__(self, index):
        del self._songs[index]

    def __contains__(self, song):
        return song in self._songs

p = Playlist(["a", "b", "c"])
print(len(p), p[0], p[1:], "b" in p)  # 3 a ['b', 'c'] True
```

**Notes**
- With just `__len__` and `__getitem__` (integer indexes from 0), your object is already iterable and works with `reversed()`.
- `__missing__` is how `collections.defaultdict` works:

```python
class DefaultDict(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]
```

---

## 8. Iteration

| Method | Triggered by |
|---|---|
| `__iter__` | `iter(obj)`, `for x in obj` |
| `__next__` | `next(obj)` |

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self          # the object is its own iterator

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

print(list(Countdown(3)))  # [3, 2, 1]
```

**Iterable vs iterator**
- *Iterable*: has `__iter__` (returns an iterator). Can be looped repeatedly.
- *Iterator*: has `__iter__` (returns self) and `__next__`. Single use.

For reusable iteration, make `__iter__` a generator:

```python
class Playlist:
    def __iter__(self):
        yield from self._songs
```

---

## 9. Callable Objects

| Method | Triggered by |
|---|---|
| `__call__` | `obj(...)` |

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

double = Multiplier(2)
print(double(5))  # 10
```

Great for stateful functions, decorators with config, and strategy objects.

---

## 10. Context Managers

| Method | Triggered by |
|---|---|
| `__enter__` | Start of `with` block (return value goes to `as`) |
| `__exit__(exc_type, exc, tb)` | End of `with` block, even on error |

```python
import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Took {self.elapsed:.3f}s")
        return False   # False/None = re-raise exceptions, True = suppress them

with Timer():
    sum(range(1_000_000))
```

For simple cases, `contextlib.contextmanager` with a generator is shorter.

---

## 11. Attribute Access

| Method | Triggered by |
|---|---|
| `__getattr__(self, name)` | Only when normal lookup **fails** |
| `__getattribute__(self, name)` | **Every** attribute access |
| `__setattr__(self, name, value)` | `obj.name = value` |
| `__delattr__(self, name)` | `del obj.name` |
| `__dir__` | `dir(obj)` |
| `__slots__` | Class attribute: restricts attributes, saves memory |

```python
class Flexible:
    def __getattr__(self, name):
        return f"<no attribute '{name}'>"

    def __setattr__(self, name, value):
        print(f"Setting {name}")
        super().__setattr__(name, value)   # avoid infinite recursion!

f = Flexible()
f.x = 5          # Setting x
print(f.x)       # 5
print(f.missing) # <no attribute 'missing'>
```

**Gotchas**
- Inside `__setattr__` / `__getattribute__`, use `super()` or `object.__setattr__` to avoid infinite recursion.
- Prefer `__getattr__` over `__getattribute__`. The latter is easy to get wrong and slows everything down.

```python
class Point:
    __slots__ = ("x", "y")   # no __dict__, less memory, no random attributes
```

---

## 12. Descriptors

Objects that customize how attributes are read/written when stored on a **class**. This is how `@property`, methods, and `@classmethod` work.

| Method | Purpose |
|---|---|
| `__get__(self, obj, objtype)` | Reading the attribute |
| `__set__(self, obj, value)` | Writing the attribute |
| `__delete__(self, obj)` | Deleting the attribute |
| `__set_name__(self, owner, name)` | Called when the descriptor is assigned in a class body |

```python
class Positive:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(obj, self.name, value)

class Product:
    price = Positive()

    def __init__(self, price):
        self.price = price

Product(10)    # fine
Product(-5)    # ValueError
```

Reusable validation logic is the classic use case.

---

## 13. Class Customization

| Method | Purpose |
|---|---|
| `__init_subclass__(cls, **kwargs)` | Runs when a class is subclassed (plugin registries, validation) |
| `__class_getitem__(cls, item)` | `MyClass[int]` (generics-style syntax) |
| `__instancecheck__` / `__subclasscheck__` | Customize `isinstance()` / `issubclass()` (defined on a metaclass) |
| `__prepare__` | Metaclass hook: custom namespace for the class body |
| `__mro_entries__` | Customize base classes |

```python
class Plugin:
    registry = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin.registry.append(cls)

class CsvPlugin(Plugin): ...
class JsonPlugin(Plugin): ...

print(Plugin.registry)  # [<class 'CsvPlugin'>, <class 'JsonPlugin'>]
```

`__init_subclass__` covers most things people used to reach for metaclasses to do.

---

## 14. Async Methods

| Method | Triggered by |
|---|---|
| `__await__` | `await obj` |
| `__aiter__` | `async for x in obj` |
| `__anext__` | Each step of `async for` (raise `StopAsyncIteration` to end) |
| `__aenter__` | `async with obj` (start) |
| `__aexit__` | `async with obj` (end) |

```python
class AsyncResource:
    async def __aenter__(self):
        print("connecting...")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("closing...")

async def main():
    async with AsyncResource() as r:
        ...
```

---

## 15. Copying & Pickling

| Method | Triggered by |
|---|---|
| `__copy__` | `copy.copy(obj)` |
| `__deepcopy__(self, memo)` | `copy.deepcopy(obj)` |
| `__getstate__` | `pickle.dumps(obj)`, copying |
| `__setstate__(self, state)` | `pickle.loads(...)` |
| `__reduce__` / `__reduce_ex__` | Full control over pickling |
| `__sizeof__` | `sys.getsizeof(obj)` |

```python
class Connection:
    def __init__(self, url):
        self.url = url
        self.socket = open_socket(url)   # not picklable

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["socket"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.socket = open_socket(self.url)
```

---

## 16. Quick Reference Table

| Category | Methods |
|---|---|
| Lifecycle | `__new__`, `__init__`, `__del__` |
| Representation | `__str__`, `__repr__`, `__format__`, `__bytes__` |
| Comparison | `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, `__ge__`, `__hash__`, `__bool__` |
| Arithmetic | `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`, `__matmul__`, `__divmod__` |
| Bitwise | `__and__`, `__or__`, `__xor__`, `__lshift__`, `__rshift__`, `__invert__` |
| Reflected / in-place | `__radd__`..., `__iadd__`... |
| Unary / conversion | `__neg__`, `__pos__`, `__abs__`, `__int__`, `__float__`, `__complex__`, `__index__`, `__round__` |
| Containers | `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`, `__missing__`, `__reversed__` |
| Iteration | `__iter__`, `__next__` |
| Callable | `__call__` |
| Context managers | `__enter__`, `__exit__` |
| Attribute access | `__getattr__`, `__getattribute__`, `__setattr__`, `__delattr__`, `__dir__`, `__slots__` |
| Descriptors | `__get__`, `__set__`, `__delete__`, `__set_name__` |
| Class hooks | `__init_subclass__`, `__class_getitem__`, `__instancecheck__`, `__subclasscheck__` |
| Async | `__await__`, `__aiter__`, `__anext__`, `__aenter__`, `__aexit__` |
| Copy / pickle | `__copy__`, `__deepcopy__`, `__getstate__`, `__setstate__`, `__reduce__` |

---

## Tips

- **Don't call dunders directly.** Use `len(x)`, not `x.__len__()`.
- **Return `NotImplemented`** from binary operators when the other type isn't supported.
- **Always define `__repr__`.** It makes debugging far easier.
- **Eq + hash go together.** Mutable objects usually shouldn't be hashable.
- **Use `dataclasses`** to get `__init__`, `__repr__`, and `__eq__` for free.
- **Use `typing.NamedTuple` or `@dataclass(order=True)`** before hand-writing comparison methods.
