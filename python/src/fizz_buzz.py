class FizzBuzz:

    def fizzBuzz(
        self,
        number,
    ) -> bool:
        if number % 5 == 0:
            return 'Buzz'

        if number % 3 == 0:
            return 'Fizz'

        return str(number)
