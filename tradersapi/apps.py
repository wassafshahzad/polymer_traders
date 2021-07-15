from django.apps import AppConfig


class TradersapiConfig(AppConfig):
    name = "tradersapi"

    def ready(self) -> None:
        import tradersapi.signals
