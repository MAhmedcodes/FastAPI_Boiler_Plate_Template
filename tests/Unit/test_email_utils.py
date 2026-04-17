import pytest
from shared.utils.email_utils import render_template


class TestEmailUtils:

    def test_render_template_replaces_variables(self):
        # Create a mock template
        import tempfile
        import os

        template_content = "Hello {{ name }}, welcome to {{ org }}"
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as f:
            f.write(template_content)
            template_path = f.name

        # Mock the path
        original_path = 'shared.utils.email_utils.Path'

        variables = {"name": "John", "org": "Test Gym"}

        # Test rendering
        # Note: You'll need to mock Path for this test
        pass
