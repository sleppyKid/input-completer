from typing import Iterable, Optional
import readline


class ListAutoCompleter:
    def __init__(
            self,
            options: Iterable[str],
            default: Optional[str] = None,
            case_sensitive=False,
            input_text: str = 'Use TAB to autocomplete text\nDefault item is ({}):',
            selected_text: str = '({}) is selected\n',
            error_text: str = '({}) is not found\n',
            custom_delims: str = '\t\n;',
            enum=False,
            sort=True
    ):
        if sort:
            self.options = sorted(list(set(options)))
        else:
            self.options = dict.fromkeys(options)

        self.default = None
        if default in self.options:
            self.default = default

        self.case_sensitive = case_sensitive

        self.input_text = '\n' + input_text + ' '
        self.selected_text = selected_text
        self.error_text = error_text
        self.enumerate = enum

        readline.set_completer_delims(custom_delims)
        readline.set_completer(self.completer)
        readline.parse_and_bind("tab: complete")

    def completer(self, text, state):
        if not self.case_sensitive:
            text = text.lower()

        _, display_options = self.check_options(text)

        try:
            return display_options[state]
        except IndexError:
            return None

    def check_options(self, text):
        options = []
        displayed_options = []
        for index, option in enumerate(self.options):
            case_option = option if self.case_sensitive else option.lower()
            displayed_option = f"{index}: {option}" if self.enumerate else option

            if self.case_sensitive and option.startswith(text):
                options.append(option)
                displayed_options.append(displayed_option)
                continue
            elif option.lower().startswith(text.lower()):
                options.append(option)
                displayed_options.append(displayed_option)
                continue

            if self.enumerate and displayed_option.startswith(text):
                options.append(option)
                displayed_options.append(displayed_option)

        return options, displayed_options

    def run(self):
        while True:
            cmd = input(self.input_text.format(self.default))

            if cmd in ['exit', 'quit']:
                exit()

            elif cmd == '' and self.default:
                print(self.selected_text.format(self.default))
                return self.default

            selected_options, _ = self.check_options(cmd)

            if selected_options:
                print(self.selected_text.format(selected_options[0]))
                return selected_options[0]
            else:
                print(self.error_text.format(cmd))
