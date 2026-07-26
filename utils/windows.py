import os
import ctypes
from pathlib import Path

FILE_ATTRIBUTE_HIDDEN = 0x02

def is_hidden(path: Path) -> bool:
    
    if os.name != "nt":
        return 
    
    attrs = ctypes.windll.kernel32.GetFileAttributesW(str(path))

    if attrs == -1:
        raise FileNotFoundError(path)
    
    return bool(attrs & FILE_ATTRIBUTE_HIDDEN)

def hide(path : Path) -> None:
    
    if os.name != "nt":
        return
    
    attrs = ctypes.windll.kernel32.GetFileAttributesW(str(path))

    if attrs == -1:
        raise FileNotFoundError(path)
    
    if not attrs & FILE_ATTRIBUTE_HIDDEN:
        ctypes.windll.kernel32.SetFileAttributesW(
            str(path),
            attrs | FILE_ATTRIBUTE_HIDDEN,
        )

