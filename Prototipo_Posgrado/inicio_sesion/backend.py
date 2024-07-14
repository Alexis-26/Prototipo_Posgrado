import reflex as rx

class FormInputState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data


def form_input1():
    return rx.vstack(
        rx.form.root(
            rx.vstack(
                rx.input(
                    name="input",
                    default_value="search",
                    placeholder="Input text here...",
                    type="password",
                    required=True,
                ),
                
            on_submit=FormInputState.handle_submit,
            reset_on_submit=True,
            width="100%",
        ),
        rx.divider(width="100%"),
        rx.heading("Results"),
        rx.text(FormInputState.form_data.to_string()),
        width="100%",
    )
    )