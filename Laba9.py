class ValueTooSmallError(BaseException):
    def message_error(self):
        return 'Значение слишком маленькое'
class NumberChecker:
    def __init__(self, min_val, max_val):
        self.min_value = min_val
        self.max_value = max_val
    def min_value_check(self, number):
        if number <= self.min_value:
            raise ValueTooSmallError
        return number
    def max_value_check(self, number):
        if number >= self.max_value:
            raise ValueTooSmallError
        return number
class Test:
    def first_test(self, checker, number):
        try:
            num = checker.min_value_check(number)
            return num
        except ValueTooSmallError as e:
            print(e.message_error())
    def vtoroy_test(selfself, checker, number):
        try:
            num = checker.min_value_check(number)
            return num
        except ValueTooSmallError as e:
            print(e.message_error())

if __name__ == "__main__":
    checker = NumberChecker(1, 10)
    test = Test()
    test.first_test(checker, 8)
    test.first_test(checker, 0)

