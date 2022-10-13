#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment


def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("mos.html.jinja2")

    html = template.render(
        page_title="MOS1",
        form_url="http://localhost:8888",
        form_id=1,
        questions=[
            {
                "title": "audio1",
                "audio_path": "audio/a1.wav",
                "name": "q1"
            },
            {
                "title": "audio2",
                "audio_path": "audio/a2.wav",
                "name": "q2"
            },
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
