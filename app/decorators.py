from functools import wraps
from flask import abort
from flask.ext.login import current_user

def admin_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.is_admin():
            abort(403)
        return func(*args, **kwargs)
    return decorated_function
