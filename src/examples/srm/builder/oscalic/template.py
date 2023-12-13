import chevron

from pathlib import Path

class Template:
    def apply(template_file, template_data):
        template = Path(template_file).read_text()

        args = {
            'template': template,
            'data': template_data
        }

        content = chevron.render(**args)

        return content