class FizzBuzz:

    def fizzBuzz(
        self,
        number,
    ) -> bool:
        if number % 3 == 0:
            return 'Fizz'

        return str(number)
