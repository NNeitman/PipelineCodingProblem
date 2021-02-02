import click, sys, logging
from os import path
from services.pipeline import import_files_to_export_format_json 
from errors import NoFileGivenError, PIPELINE_ERROR_MESSSAGE_BASE

logger = logging.getLogger(__name__)

def _validate_files(files):
    files_that_do_not_exist = list(filter(lambda file: not path.exists(file), files))

    if len(files_that_do_not_exist) > 0:
        logger.error(f'File(s) do not exist: {files_that_do_not_exist}')
        raise FileNotFoundError(files_that_do_not_exist)

    if len(files) == 0:
        raise NoFileGivenError()

    return True


@click.command()
@click.argument('source_files', nargs=-1) # n-many args
def main(source_files) -> None: 
    try: 
        _validate_files(source_files)
        results, result_count = import_files_to_export_format_json(source_files)

        logger.info(f"{result_count} records imported from ({len(source_files)}) file(s)")
        click.echo(results)
    except FileNotFoundError as e:
        logger.error(f"{PIPELINE_ERROR_MESSSAGE_BASE}: {e}")
        click.echo(f"{PIPELINE_ERROR_MESSSAGE_BASE}: {e}", err=True)
        raise FileNotFoundError from e
    except Exception as e:
        logger.error(f"{PIPELINE_ERROR_MESSSAGE_BASE}: {e}")
        click.echo(f"{PIPELINE_ERROR_MESSSAGE_BASE}: {e}", err=True)
        raise Exception from e


if __name__ == '__main__':
    main()