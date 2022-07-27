# mbmutils

Simpmle common utilities.

## Installation

```
pip install mbmutils
```

## f-Functions

The `f`-functions are simple string utilities of common actions. They have the
standard pattern of:

> return string after|before|between the keys

These all use the "first found" index. Meaning if there are more than one
instance of the key found, they use the first. Because of this there are functions
that look from the front (`f_left | f_right`) and functions that look from the
back (`f_left_back | f_right_back`).

| function     | Description                                                         |
|--------------|---------------------------------------------------------------------|
| f_right      | return everything to the `right` of the key                         |
| f_left       | return everything to the `left` of the key                          |
| f_right_back | return everything to the `right` of the key, starting from the back |
| f_left_back  | return everything to the `left` of the key, starting from the back  |
| f_between          | return everything between the keys          |

You will also find a `not_found` parameter to these functions. This
allows you to define what is returned if the key is not found in the string.

### Examples

```python

from mbmutils import mu

my_string = "hello there fancy world!"

print({mu.f_right(my_string, ' fancy ')})
# -> world!

print({mu.f_left(my_string, ' fancy ')})
# -> hello there 

print({mu.f_left(my_string, 'will not find')})
# -> None 

print({mu.f_left(my_string, 'will not find',
                 not_found="not here")})
# -> not here 
```

## Path functions

There are also a few _path-finding_ functions that search for a path
containing the `partial_path` provided. These will search the current path
and then begin looking upward from there.

There are 2 functions: 1 for files and the other for directories.

```python

from mbmutils import mu

# assuming current folder is
# /path/to/python/code
mu.find_folder_path('data')
# will return the first valid:
#   -> path/to/python/code/data
#   -> path/to/python/data
#   -> path/to/data
#   -> path/data

# again, assuming current folder is
# /path/to/python/code
mu.find_folder_path('my_file.json')
# will return the first valid:
#   -> path/to/python/code/my_file.json
#   -> path/to/python/my_file.json
#   -> path/to/my_file.json
#   -> path/my_file.json

```