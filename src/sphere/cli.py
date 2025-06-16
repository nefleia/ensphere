import click

from sphere import coodbook
from sphere.decrypt import decrypt
from sphere.encrypt import encrypt


@click.group()
def cli():
    """Sphere CLI for encryption and decryption."""
    pass


@cli.command()
def encrypt_command():
    """Encrypt a string using the mapping."""
    try:
        codebook = coodbook.get_codebook()
        text = click.prompt("Enter text to encrypt")
        result = encrypt(codebook, text)
        click.echo(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


@cli.command()
def decrypt_command():
    try:
        """Decrypt a string using the mapping."""
        codebook = coodbook.get_codebook()
        text = click.prompt("Enter text to decrypt")
        result = decrypt(codebook, text)
        click.echo(result)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


if __name__ == "__main__":
    cli()
