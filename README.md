# Pipeline Coding Problem Solution
Author: Nathan Neitman

# Usage

## Intallation
1. Have Python 3.X with pip installed and part of your PATH
2. `pip3 install -r requirements.txt && pip3 install -r requirements-test.txt`

## Examples

### Containerized CLI
- TODO

### Python CLI

#### Single File:
```sh 
python pipeline_data_reader/main.py your_file.csv
```
Example Output:
```
{
   "user_list_size": 3,
   "user_list": [
      {
         "list_id": 1,
         "first name": "John",
         "last name": "Doe",
         "email": "john.doe@gmail.com"
      },
      {
         "list_id": 2,
         "first name": "Jane",
         "last name": "Smith",
         "email": "jane.smith@yahoo.com"
      }
   ]
}
```

#### Multiple Files:
```sh 
pipeline_data_reader/main.py your_file.csv your_second_file.csv your_third_file.csv
```

Example Output:

**WARNING:** The `list_id`s are only unique per file given, so if there are multiple files there will be MULTIPLE OF THE SAME `list_id`

```
{
   "user_list_size": 3,
   "user_list": [
      {
         "list_id": 1,
         "first name": "John",
         "last name": "Doe",
         "email": "john.doe@gmail.com"
      },
      {
         "list_id": 2,
         "first name": "Jane",
         "last name": "Smith",
         "email": "jane.smith@yahoo.com"
      },
      {
         "list_id": 1, 
         "first name": "Mike",
         "last name": "List",
         "email": "mike.list@gmail.com"
      }
   ]
}
```

# TODO:
- Get CI/CD Working
- More thoroughly Test positive and negative cases
- Add Linter
- Provide better errors for malformed CSVs
- Handle potentially malformed data inputs
- Add piped input option
- Add option to pull files from remote server
- list ids are not very useful in their current state for outputs that come from multiple user list files, use something better (maybe UUID?)
- Prune up exports per module to be only the necessities