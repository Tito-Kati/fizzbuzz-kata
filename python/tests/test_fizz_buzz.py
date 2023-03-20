from src.fizz_buzz import FizzBuzz


class TestFizzBuzz:

    def test_returns_string_representation_of_number_1(
        self,
    ):
        # Given
        fizzBuzz = FizzBuzz()
        # When

        # Then
        assert fizzBuzz.fizzBuzz(1) == '1'

    def test_returns_string_representation_of_number_2(
        self,
    ):
        # Given
        fizzBuzz = FizzBuzz()
        # When

        # Then
        assert fizzBuzz.fizzBuzz(2) == '2'

    def test_returns_fizz_when_3_given(
        self,
    ):
        # Given
        fizzBuzz = FizzBuzz()
        # When

        # Then
        assert fizzBuzz.fizzBuzz(3) == 'Fizz'
