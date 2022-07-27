from __future__ import annotations

import os
import re
import sys
from pathlib import Path

# not exported
from typing import Optional


def _find(pathname: str, match_func=os.path.isfile) -> Optional[str]:
    cwd_parts = list(Path(os.getcwd()).parts)
    while len(cwd_parts) > 0:
        search_dir_str = "/".join(cwd_parts).replace('//', '/')
        search_dir = Path(search_dir_str)
        candidate = search_dir / pathname.strip("/")
        if match_func(candidate):
            return candidate.as_posix()
        cwd_parts.pop()
    return None


def find_file_path(partial_path: str):
    return _find(partial_path, match_func=os.path.isfile)


def find_folder_path(partial_path: str):
    final_path = _find(partial_path, match_func=os.path.isdir)
    if final_path is None:
        return None
    if final_path[-1] != '/':
        final_path += '/'
    return final_path


def get_folder_path(folder_name: str = "data") -> str | None:
    """Will search upward for first directory with a /data folder.
    includes trailing slash
    """
    return find_folder_path(folder_name)


def get_full_path(partial_path: str = None) -> str | None:
    return find_file_path(partial_path)


def f_between(string: str, look_for_left: str, look_for_right: str, not_found=None) -> str | None:
    """ Returns string found between the tokens.

    - Both tokens are required in the string, otherwise `None` is returned.
    """
    if string is None or len(string) < 1: return not_found
    if look_for_left is None or len(look_for_left) < 1: return not_found
    if look_for_right is None or len(look_for_right) < 1: return not_found

    right_part = f_right(string, look_for_left)
    found_part = f_left(right_part, look_for_right)

    return found_part if found_part is not None else not_found


def f_left(string: str, look_for: str, not_found=None) -> str | None:
    if string is None or len(string) < 1: return not_found
    if look_for is None or len(look_for) < 1: return not_found
    if look_for not in string: return not_found

    return string.split(look_for)[0]


def f_left_back(string: str, look_for: str, not_found=None) -> str | None:
    if string is None or len(string) < 1: return not_found
    if look_for is None or len(look_for) < 1: return not_found
    if look_for not in string: return not_found

    return look_for.join(string.split(look_for)[:-1])


def f_replace_for(string: str, look_for: str, replace_with: str) -> str:
    """ Replaces one string with another"""
    return string.replace(look_for, replace_with)


def f_right(string: str, look_for: str, not_found=None) -> str | None:
    if string is None or len(string) < 1: return not_found
    if look_for is None or len(look_for) < 1: return not_found
    if look_for not in string: return not_found

    return look_for.join(string.split(look_for)[1:])


def f_right_back(string: str, look_for: str, not_found=None) -> str | None:
    if string is None or len(string) < 1: return not_found
    if look_for is None or len(look_for) < 1: return not_found
    if look_for not in string: return not_found

    return string.split(look_for)[-1]


def list_index_of(the_list: list, find_val) -> int:
    """simple wrapper for `index` function on a list where -1 means not found.

    Exceptions will still be raised for invalid parameters."""
    try:
        return the_list.index(find_val)
    except ValueError:
        return -1


if __name__ == '__main__':
    print(f"Hello {f_right_back('Hello there crazy World', ' ')}!")
