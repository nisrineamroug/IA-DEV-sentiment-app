from ui.app import call_api


def test_ui_module_exposes_client():
    assert callable(call_api)
