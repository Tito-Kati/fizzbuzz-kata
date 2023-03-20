import pytest
from src.fizz_buzz import FizzBuzz

class TestFizzBuzz:
    @pytest.fixture
    def fizzBuzz(self):
        return FizzBuzz()

    def test_returns_string_representation_of_number_1(self, fizzBuzz):
        assert fizzBuzz.fizzBuzz(1) == '1'

    def test_returns_string_representation_of_number_2(self, fizzBuzz):
        assert fizzBuzz.fizzBuzz(2) == '2'

    def test_returns_fizz_when_multiple_of_3_like_3_given(self, fizzBuzz):
        assert fizzBuzz.fizzBuzz(3) == 'Fizz'

    def test_returns_fizz_when_multiple_of_3_like_6_given(self, fizzBuzz):
        assert fizzBuzz.fizzBuzz(6) == 'Fizz'
