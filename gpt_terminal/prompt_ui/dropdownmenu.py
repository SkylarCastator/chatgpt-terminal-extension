import platform


def dropdown_menu(options):
    if platform.system() != 'Windows':
        from simple_term_menu import TerminalMenu
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        return options[menu_entry_index]
    else:
        import questionary
        selected_option = questionary.select(
            "Select One",
            choices=options,
        ).ask()
        return selected_option
