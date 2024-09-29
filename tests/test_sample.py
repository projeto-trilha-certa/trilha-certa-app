import pytest


def plus_one(x):
    return x + 1


def system_exit_example():
    raise SystemExit(1)


def group_exception_raise():
    some_message = "Group message"

    raise ExceptionGroup(
        some_message,
        [
            RuntimeError(),
        ],
    )


"""
This test is simply to showcase how to make tests with pytest.

It will always fail and should be removed for when deploying in prod.
"""


class TestSampleClass:
    def test_answer(self):
        assert plus_one(3) == 5

    def test_mytest(self):
        with pytest.raises(SystemExit):
            system_exit_example()

    def test_exception_in_group(self):
        with pytest.raises(ExceptionGroup) as excinfo:
            group_exception_raise()
        assert excinfo.group_contains(RuntimeError)
        assert not excinfo.group_contains(TypeError)

    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
