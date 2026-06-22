import asyncio
import importlib

import pytest


def test_get_current_user_returns_user(monkeypatch):
    monkeypatch.setenv("TENANT_ID", "test-tenant-id")
    monkeypatch.setenv("CLIENT_ID", "test-client-id")

    auth = importlib.reload(importlib.import_module("modules.auth"))

    class DummyKey:
        key = "dummy-signing-key"

    monkeypatch.setattr(auth.jwks_client, "get_signing_key_from_jwt", lambda token: DummyKey())
    monkeypatch.setattr(
        auth,
        "decode",
        lambda token, signingKey, algorithms, audience, issuer: {"preferred_username": "alice"},
    )

    user = asyncio.run(auth.getCurrentUser("fake-token"))

    assert user.username == "alice"
    assert user.disabled is False


def test_get_current_active_user_rejects_disabled():
    import modules.auth as auth

    disabled_user = auth.User(username="bob", disabled=True)

    with pytest.raises(auth.HTTPException) as excinfo:
        asyncio.run(auth.getCurrentActiveUser(disabled_user))

    assert excinfo.value.status_code == auth.status.HTTP_400_BAD_REQUEST


def test_user_authenticated_returns_true():
    import modules.auth as auth

    user = auth.User(username="carol", disabled=False)
    assert asyncio.run(auth.userAuthenticated(user)) is True
