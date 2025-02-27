#!/usr/bin/env python
"""
Demonstration of the Click color policy feature for parent-child process communication.

This script demonstrates the specific use case mentioned in the feature request:
A parent process runs a child process, captures its stdout, and preserves the colors
when displaying the output.

Usage:
  python parent_child_demo.py
"""

import click
import subprocess
import sys


def create_child_script():
    """Create a temporary script for the child process."""
    with open("child_script.py", "w") as f:
        f.write("""#!/usr/bin/env python
import click

# Set color policy to ALWAYS_KEEP to preserve colors even when writing to a pipe
click.set_color_policy(click.ColorPolicy.ALWAYS_KEEP)

# Print some colored text
click.secho("This is RED text from the child process", fg="red")
click.secho("This is GREEN text from the child process", fg="green")
click.secho("This is BLUE text from the child process", fg="blue")
click.secho("This is YELLOW text from the child process", fg="yellow")
""")


@click.command()
@click.option("--keep-colors", is_flag=True, help="Force keeping colors in output")
def main(keep_colors):
    """Demonstrate the color policy feature with parent-child processes."""
    # Create the child script
    create_child_script()
    
    # Set color policy in parent process if requested
    if keep_colors:
        click.set_color_policy(click.ColorPolicy.ALWAYS_KEEP)
        click.echo("Parent process color policy set to ALWAYS_KEEP")
    else:
        click.echo("Parent process using default AUTO color policy")
    
    # Run the child process and capture its output
    click.echo("\nRunning child process and capturing its output...")
    result = subprocess.run(
        [sys.executable, "child_script.py"], 
        capture_output=True, 
        text=True
    )
    
    # Display the captured output
    click.echo("\nOutput from child process:")
    click.echo(result.stdout)
    
    # Explain what happened
    click.echo("\nExplanation:")
    if keep_colors:
        click.echo("- The child process set its color policy to ALWAYS_KEEP")
        click.echo("- The parent process also set its color policy to ALWAYS_KEEP")
        click.echo("- Colors are preserved throughout the pipe chain")
    else:
        click.echo("- The child process set its color policy to ALWAYS_KEEP")
        click.echo("- The parent process used the default AUTO policy")
        click.echo("- With AUTO policy, the parent would normally strip colors when")
        click.echo("  writing to a non-terminal, but the child's ALWAYS_KEEP setting")
        click.echo("  ensures colors are preserved through the pipe")
    
    click.echo("\nTo see the difference:")
    click.echo("1. Run without arguments: python parent_child_demo.py")
    click.echo("2. Run with --keep-colors: python parent_child_demo.py --keep-colors")
    click.echo("3. Try piping the output: python parent_child_demo.py | cat")


if __name__ == "__main__":
    main() 