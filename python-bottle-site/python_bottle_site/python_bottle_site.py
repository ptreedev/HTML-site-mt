"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="bottom-right"),
        rx.vstack(
            rx.heading("Welcome to Pages", size="9"),
            rx.text(
                "It's a page for viewing pages",
                "Look here is another page",
                size="5",
            ),
            rx.link(
                rx.button("Check out this page!"),
                href="another_page.py",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
