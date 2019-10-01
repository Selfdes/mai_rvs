import redis


class AlreadyExistException(Exception):
    type = 1


class OneLessThatItWasException(Exception):
    type = 2


def processing(db: redis.Redis, number: int) -> int:
    if db.get(number):
        raise AlreadyExistException('Number already exists')
    elif db.get(number + 1):
        raise OneLessThatItWasException('Number is  one less then existing one')

    db.set(number, 'True')

    return number + 1
