import reflex as rx
from rxconfig import config

class User(rx.Base):
    name: str
    email: str
    gender: str


class State(rx.State):
    users: list[User] = [
        User(
            name="Danilo Sousa",
            email="danilo@example.com",
            gender="Male",
        ),
        User(
            name="Zahra Ambessa",
            email="zahra@example.com",
            gender="Female",
        ),
        User(
            name="Test User",
            email="test@test.com",
            gender="Male",
        )
    ]


def show_user(user: User):
    return rx.table.row(
        rx.table.cell(user.name),
        rx.table.cell(user.email),
        rx.table.cell(user.gender),
    )

@rx.page(route="/dashboard")
def table() -> rx.Component: 
    return rx.container(
        rx.vstack(
            rx.heading("ANOTHER PAGE?"),
            rx.text("This is an example table using reflex"),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Name"),
                        rx.table.column_header_cell("Email"),
                        rx.table.column_header_cell("Gender"),
                    ),
                ),
                rx.table.body(
                    rx.foreach(State.users, show_user)
                ),
                variant="surface",
                size="3",
            ),
        ),
    )

# page = rx.page(route="/table")(table)
