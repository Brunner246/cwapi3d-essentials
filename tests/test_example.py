class User:
    def __init__(self, email):
        self.email = email


class RegistrationResult:
    def __init__(self, success, user):
        self.success = success
        self.user = user


def register_user(email, password):
    if email and password:
        return RegistrationResult(success=True, user=User(email=email))
    return RegistrationResult(success=False, user=None)


def test_user_registration():
    # Arrange
    user_data = {"email": "test@example.com", "password": "secure123"}

    # Act
    result = register_user(**user_data)

    # Assert
    assert result.success is True
    assert result.user.email == user_data["email"]
