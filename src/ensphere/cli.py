import click

from ensphere.codebook import get_codebook
from ensphere.decrypt import decrypt
from ensphere.encrypt import encrypt


def _validate_txt_file(ctx, param, value):
    """Validate that the file exists and is readable."""
    if value is not None:
        if not value.name.endswith(".txt"):
            raise click.BadParameter("Only .txt files are allowed")
    return value


@click.group()
def cli():
    """CLI for encrypting and decrypting text using a codebook."""
    pass


@cli.command()
@click.argument("text", required=False)
@click.option(
    "-f",
    "--file",
    type=click.File("r"),
    callback=_validate_txt_file,
    help="File path of the text to be encrypted. "
    "(only .txt files are allowed)",
)
def encrypt_command(text, file):
    """Encrypt a string using the codebook."""
    try:
        codebook = get_codebook()
        if file:
            text = file.read()
        elif text is None:
            text = click.prompt("Enter text to encrypt")
        result = encrypt(codebook, text)
        click.echo(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


@cli.command()
@click.argument("text", required=False)
def decrypt_command(text):
    """Decrypt a string using the codebook."""
    try:
        codebook = get_codebook()
        if text is None:
            text = click.prompt("Enter text to decrypt")
        result = decrypt(codebook, text)
        click.echo(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


if __name__ == "__main__":
    cli()
