#!/usr/bin/env python
import click

# Set color policy to ALWAYS_KEEP to preserve colors even when writing to a pipe
click.set_color_policy(click.ColorPolicy.ALWAYS_KEEP)

# Print some colored text
click.secho("This is RED text from the child process", fg="red")
click.secho("This is GREEN text from the child process", fg="green")
click.secho("This is BLUE text from the child process", fg="blue")
click.secho("This is YELLOW text from the child process", fg="yellow")
