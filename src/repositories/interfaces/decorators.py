from functools import wraps

from fastapi.responses import JSONResponse
from pydantic.error_wrappers import ValidationError


def schema_validator(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValidationError as e:
            return JSONResponse({
                'data': [],
                "errors": [e.errors()],
                "message": "Schema error"
            }, status_code=422)
    return wrap
