from .auth import auth_ns
from project.views.genres import genres_ns
from project.views.user import user_ns

__all__ = [
    'auth_ns',
    'genres_ns',
    'user_ns',
]
