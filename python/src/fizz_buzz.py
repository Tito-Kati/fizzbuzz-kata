class FizzBuzz:

    def fizzBuzz(
        self,
        number,
    ) -> str:
        string = ""

        if number % 3 == 0:
            string += 'Fizz'

        if number % 5 == 0:
            string += 'Buzz'

        return string or str(number)
