from controller.config import settings


def test_application_configuration_loads() -> None:
    assert settings.app_name == "outcome-first-controller"
    assert settings.environment == "development"
