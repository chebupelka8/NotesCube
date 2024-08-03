from functools import wraps
from typing import Callable, Any

from fastapi import HTTPException


def require_return(error: BaseException):
    """if the function returns None, the decorator will raise the passed exception"""

    def inner(func: Callable):

        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            if (returing := await func(*args, **kwargs)) is None:
                raise error
            
            return returing
        
        return wrapper
    return inner


def require_return_else_HTTPException(detail: str, status_code: int = 404):
    """if the function returns None, the decorator will raise HTTPException"""
    
    return require_return(HTTPException(status_code, detail))
