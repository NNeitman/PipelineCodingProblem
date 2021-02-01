import click, pandas, json, logging
from typing import Union, List

logger = logging.getLogger(__name__)

DataFrameType = type(pandas.DataFrame)

def transform_data_frames_for_export(*data_frames):
    def _clean_data_frames_for_export(data_frame):
        data_frame['first name'] = data_frame['first name'].str.strip()
        data_frame['last name'] = data_frame['last name'].str.strip()
        data_frame['email'] = data_frame['email'].str.strip()
        logger.debug('Cleaned data')
    
    all_in_one_df = pandas.concat(*data_frames)
    all_in_one_df[['first name','last name']] = all_in_one_df['full_name'].str.split(' ', expand=True)
    _clean_data_frames_for_export(all_in_one_df)
    del all_in_one_df['full_name']

    return all_in_one_df


def import_files_to_dataframe(files):
    def import_file_to_dataframe(filepath_or_buffer):
        try: 
            data_frame = pandas.read_csv(filepath_or_buffer)
            # Individually track ids on a per file basis, this will result in duplicate list_id values when there are multiple files
            data_frame['list_id'] = data_frame.index + 1
            return data_frame
        except Exception as e:
            logger.error(f"Error occurred parsing file ({filepath_or_buffer}): {e}")
            raise e from Exception
    
    data_frames = list(map(import_file_to_dataframe, files))
    return transform_data_frames_for_export(data_frames)

def import_files_to_export_format_json(files):
    data_frame = import_files_to_dataframe(files)

    json_data = json.dumps({ 'user_list_size': data_frame['list_id'].size, 'user_list': data_frame.to_dict('records')})

    return (json_data, data_frame['list_id'].size)


    