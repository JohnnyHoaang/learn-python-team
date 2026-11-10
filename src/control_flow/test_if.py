"""IF statement

@see: https://docs.python.org/3/tutorial/controlflow.html

There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is
short for ‘else if’, and is useful to avoid excessive indentation.

An if … elif … elif … sequence is a substitute for the switch or case statements found
in other languages.
"""


def test_if_statement():
    """IF statement"""

    number = 15
    conclusion = ''

    if number < 0:
        conclusion = 'Number is less than zero'
    elif number == 0:
        conclusion = 'Number equals to zero'
    elif number < 1:
        conclusion = 'Number is greater than zero but less than one'
    else:
        conclusion = 'Number bigger than or equal to one'

    assert conclusion == 'Number bigger than or equal to one'


def test_nested_if_statement():
    """Nested conditions can refine a decision."""

    score = 85
    result = ''

    if score >= 60:
        if score >= 80:
            result = 'Pass with distinction'
        else:
            result = 'Pass'
    else:
        result = 'Fail'

    assert result == 'Pass with distinction'


def test_multiple_elif_branches():
    """Multiple elif branches select the matching temperature range."""

    temperature = 22

    if temperature < 0:
        description = 'freezing'
    elif temperature < 15:
        description = 'cold'
    elif temperature < 25:
        description = 'mild'
    else:
        description = 'warm'

    assert description == 'mild'
    