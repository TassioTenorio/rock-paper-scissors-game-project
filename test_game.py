import pytest
from rock_paper_scissors_game import determine_winner


@pytest.mark.parametrize(
    'user, computer, expected',
    [
        ('Rock', 'Scissors', 'user'),
        ('Rock', 'Paper', 'computer'),
        ('Paper', 'Rock', 'user'),
        ('Paper', 'Scissors', 'computer'),
        ('Scissors', 'Paper', 'user'),
        ('Scissors', 'Rock', 'computer'),
        ('Rock', 'Rock', 'tie'),
        ('Paper', 'Paper', 'tie'),
        ('Scissors', 'Scissors', 'tie')
    ]
)
def test_determine_winner(user, computer, expected):
    assert determine_winner(user, computer) == expected
    
    
def test_invalid_user_input(monkeypatch):
    inputs = iter(['abc', '1'])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert user() == 'Rock'

from rock_paper_scissors_game import determine_winner, user