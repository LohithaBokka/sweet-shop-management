from app.models.user import User

def test_user_model_fields():
    user = User(
        username="sakhi",
        password="test123",
        role="admin"
    )

    assert user.username == "sakhi"
    assert user.password == "test123"
    assert user.role == "admin"
