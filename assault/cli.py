import click

@click.command()
@click.option("--requests", "-r", default=500, help="Number of requests")
@click.option("--concurrency", "-c", default=1, help="Number of concurrent requests")
@click.option("--json", "-j", default=None, help="Path to output json file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    pass

if __name__ == '__main__':
    cli()