import reflex as rx
from rxconfig import config
from python_bottle_site.pages import dashboard

# from .pages import table
class State(rx.State):
    """The app state."""

@rx.page(route="/reflex", title="Portfolio")
def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="bottom-right"),
        rx.vstack(
            rx.heading("Welcome to my portfolio", size="9"),
            rx.text(
                "It's built using only python and is using Relfex as a framework",
                "Look here is another page",
                size="5",
            ),
            rx.link(
                rx.button("Check out the dashboard I made!"),
                href="/dashboard",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        
    )


app = rx.App()
# app.add_page(index)
