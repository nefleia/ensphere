import click

from sphere import mapping
from sphere.decrypt import decrypt
from sphere.encrypt import encrypt


@click.group()
def cli():
    """Sphere CLI for encryption and decryption."""
    pass


@cli.command()
def encrypt_command():
    """Encrypt a string using the mapping."""
    mapping_data = mapping.get_mapping()
    text = click.prompt("Enter text to encrypt")
    result = encrypt(mapping_data, text)
    click.echo(result)


@cli.command()
def decrypt_command():
    """Decrypt a string using the mapping."""
    mapping_data = mapping.get_mapping()
    text = click.prompt("Enter text to decrypt")
    result = decrypt(mapping_data, text)
    click.echo(result)


if __name__ == "__main__":
    cli()
