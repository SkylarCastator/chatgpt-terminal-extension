from datetime import datetime

from rich import box
from rich.align import Align
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn, SpinnerColumn
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

from rich.menu import Menu
from rich.menu import MenuItem

console = Console()

def make_layout() -> Layout:
    layout = Layout(name="root")

    layout.split(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=7)
    )

    layout["main"].split_row(
        Layout(name="side"),
        Layout(name="body", ratio=2, minimum_size=60),
    )
    layout["side"].split(Layout(name="box1"), Layout(name="box2"))

    return layout

def make_sponsor_message() -> Panel:
    sponsor_message = Table.grid(padding=1)
    sponsor_message.add_column(style="green", justify="right")
    sponsor_message.add_column(no_wrap=True)
    sponsor_message.add_row(
        "Twitter",
        "[u blue link=https://twitter.com/texturalize]https://twitter.com/texturalize",
    )
    sponsor_message.add_row(
        "CEO",
        "[u blue link=https://twitter.com/andrewhead]https://twitter.com/andrewhead",
    )
    sponsor_message.add_row(
        "Textualize", "[u blue link=https://textualize.com]https://textualize.com",
    )

    message = Table.grid(padding=1)
    message.add_column()
    message.add_column(no_wrap=True)
    message.add_row(sponsor_message)

    message_panel = Panel(
        Align.center(
            Group("\n", Align.center(sponsor_message)),
            vertical="middle",
        ),
        box=box.ROUNDED,
        padding=(1, 2),
        title="[b red]Thanks for trying out Rich!",
        border_style="bright_blue",
    )

    return message_panel


class Header:
    def __rich__(self) ->Panel:
        table = Table.grid(expand=True)
        table.add_column(justify="center", ratio=1)
        table.add_column(justify="right")

        table.add_row(
            Text("Chat GPT", style="bold blue"),
            Text(datetime.now().isoformat(timespec="seconds"), justify="right"),
        )

        return Panel(table, style="white on blue")


def make_syntax() -> Syntax:
    code = """\
def ratio_resolve(total: int, edges: List[Edge]) -> List[int]:
    sizes = [(edge.size or None) for edge in edges]
    # While any edges haven't been calculated
    while any(size is None for size in sizes):
        # Get flexible edges and index to map these back on to sizes list
        flexible_edges = [
            (index, edge)
            for index, (size, edge) in enumerate(zip(sizes, edges))
            if size is None
        ]
        # Remaining space in total
        remaining = total - sum(size or 0 for size in sizes)
        if remaining <= 0:
            # No room for flexible edges
            sizes[:] = [(size or 0) for size in sizes]
            break
        # Calculate number of characters in a ratio portion
        portion = remaining / sum((edge.ratio or 1) for _, edge in flexible_edges)
        # If any edges will be less than their minimum, replace size with the minimum
        for index, edge in flexible_edges:
            if portion * edge.ratio <= edge.minimum_size:
                sizes[index] = edge.minimum_size
                break
        else:
            # Distribute flexible space and compensate for rounding error
            # Since edge sizes can only be integers we need to add the remainder
            # to the following line
            _modf = modf
            remainder = 0.0
            for index, edge in flexible_edges:
                remainder, size = _modf(portion * edge.ratio + remainder)
                sizes[index] = int(size)
            break
    # Sizes now contains integers only
    return cast(List[int], sizes)
    """
    syntax = Syntax(code, "python", line_numbers=True)
    return syntax

def generate_footer():
    job_progress = Progress(
        "{task.description}",
        SpinnerColumn(),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    )
    job_progress.add_task("[green]Cooking")
    job_progress.add_task("[magenta]Baking", total=200)
    job_progress.add_task("[cyan]Mixing", total=400)

    total = sum(task.total for task in job_progress.tasks)
    overall_progress = Progress()
    overall_task = overall_progress.add_task("All Jobs", total=int(total))

    progress_table = Table.grid(expand=True)
    progress_table.add_row(
    Panel(
        overall_progress,
        title="Overall Progress",
        border_style="green",
        padding=(2, 2),
    ),
    Panel(job_progress, title="[b]Jobs", border_style="red", padding=(1, 2)),)
    return progress_table


if __name__ == "__main__":
    job_progress = Progress(
        "{task.description}",
        SpinnerColumn(),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    )
    job_progress.add_task("[green]Cooking")
    job_progress.add_task("[magenta]Baking", total=200)
    job_progress.add_task("[cyan]Mixing", total=400)

    total = sum(task.total for task in job_progress.tasks)
    overall_progress = Progress()
    overall_task = overall_progress.add_task("All Jobs", total=int(total))

    progress_table = Table.grid(expand=True)
    progress_table.add_row(
        Panel(
            overall_progress,
            title="Overall Progress",
            border_style="green",
            padding=(2, 2),
        ),
        Panel(job_progress, title="[b]Jobs", border_style="red", padding=(1, 2)),
    )

    layout = make_layout()
    layout["header"].update(Header())
    layout["body"].update(make_sponsor_message())
    layout["box2"].update(Panel(make_syntax(), border_style="green"))
    #layout["box1"].update(Panel(layout.tree, border_style="red"))
    layout["footer"].update(progress_table)
    
    menu = Menu()
    menu.add_item(MenuItem('Option 1', lambda: console.print('Option 1 selected')))
    menu.add_item(MenuItem('Option 2', lambda: console.print('Option 2 selected')))
    menu.add_item(MenuItem('Option 3', lambda: console.print('Option 3 selected')))
    layout["box1"].update(menu)
    menu.show()

    from time import sleep
    from rich.live import Live

    from prompt_toolkit import PromptSession
    session = PromptSession()

    with Live(layout, refresh_per_second=10, screen=True):
        while not overall_progress.finished:
            sleep(0.1)
            for job in job_progress.tasks:
                if not job.finished:
                    job_progress.advance(job.id)

            completed = sum(task.completed for task in job_progress.tasks)
            overall_progress.update(overall_task, completed=completed)
            

    #        try:
    #            text = session.prompt("> ")
    #            layout["box1"].update(Panel(text, title="Right Panel"))
    #            console.print(text)
    #        except KeyboardInterrupt:
    #            break
