from python_bottle_site.python_bottle_site import index

def test_smoke_index_render():
    try:
        component = index()
        assert component is not None
    except Exception as e:
        assert False, f"Smoke test failed: {e}"