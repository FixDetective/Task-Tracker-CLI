from argparse import ArgumentParser


def create_parser() -> ArgumentParser:
    parser: ArgumentParser = ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("desc_task", help="Task description", type=str)

    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id_task", help="Task ID", type=int)
    update_parser.add_argument("desc_task", help="Task description", type=str)

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id_task", help="Task ID", type=int)

    mark_in_progress_parser = subparsers.add_parser(
        "mark-in-progress", help="Mark a task as in progress"
    )
    mark_in_progress_parser.add_argument("id_task", help="Task ID", type=int)

    mark_done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
    mark_done_parser.add_argument("id_task", help="Task ID", type=int)

    list_parser = subparsers.add_parser("list_task", help="List all tasks")
    list_parser.add_argument(
        "status",
        nargs="?",
        choices=["done", "todo", "in-progress"],
        help="Filter tasks by status",
    )

    return parser
