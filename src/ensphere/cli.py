import click

from ensphere.codebook import get_codebook
from ensphere.decrypt import decrypt
from ensphere.encrypt import encrypt


@click.group()
def cli():
    """CLI for encrypting and decrypting text using a codebook."""
    pass


@cli.command()
def encrypt_command():
    """Encrypt a string using the codebook."""
    try:
        codebook = get_codebook()
        text = click.prompt("Enter text to encrypt")
        result = encrypt(codebook, text)
        click.echo(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


@cli.command()
def decrypt_command():
    """Decrypt a string using the codebook."""
    try:
        codebook = get_codebook()
        text = click.prompt("Enter text to decrypt")
        result = decrypt(codebook, text)
        click.echo(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


if __name__ == "__main__":
    cli()
