from shared.utils.email_utils import render_template
import tempfile


class TestEmailUtils:

    def test_render_template_replaces_variables(self):
        content = "Hello {{ name }}, welcome to {{ org }}"

        with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".html") as f:
            f.write(content)
            path = f.name

        result = render_template(path, {
            "name": "John",
            "org": "Test Org"
        })

        assert "John" in result
        assert "Test Org" in result
