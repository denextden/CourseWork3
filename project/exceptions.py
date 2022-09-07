class BaseServiceError(Exception):
    code = 500


class ItemNotFound(BaseServiceError):
    code = 404


# class ItemNotFound(Exception):
#     ...
#
#
# class UserNotFound(ItemNotFound):
#     pass
#
# class WrongPassword(ItemNotFound):
#     pass