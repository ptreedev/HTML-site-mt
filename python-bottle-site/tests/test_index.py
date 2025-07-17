from python_bottle_site.python_bottle_site import index

def test_smoke_index_render():
    component = index()
    assert component is not None
    
