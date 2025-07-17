from python_bottle_site.python_bottle_site import index

class Test_Index_Content:
    index_component = index()
    rendered_dict = index_component.render()
    sub_components = rendered_dict["children"]
    def test_smoke_index_render(self):
        assert self.index_component is not None
    def test_component_container_exists(self):
        assert self.rendered_dict["name"] == "RadixThemesContainer"
    def test_component_vstack_exists_in_container(self):
        vstack = next((child for child in self.sub_components if child["name"] == "RadixThemesFlex"), None)
        assert vstack is not None, "VStack should be present"

