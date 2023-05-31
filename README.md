# Mecsimcalc v0.1.1 documentation

This library is designed to provide a set of functions for handling and converting various types of data, such as base64 encoded data, Pandas DataFrames, and Pillow images.

- [GitHub Repository](https://github.com/MecSimCalc/MecSimCalc-utils)
- [PyPi Page](https://pypi.org/project/mecsimcalc/)

## General

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">input_to_file</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/general_utils.py#LL7C1-L31C61" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

```python
def input_to_file(input_file, metadata = False)
```

#### Description:

Converts a base64 encoded string into a file object and metadata

#### Arguments:

| Argument         | Type                | Description                                                |
| ---------------- | ------------------- | ---------------------------------------------------------- |
| **`input_file`** | **str**             | Base64 encoded string, prefixed with metadata              |
| **`metadata`**   | **bool** (optional) | Flag to return metadata with the file. (Defaults to False) |

#### Raises:

| Exception        | Description                                                                        |
| ---------------- | ---------------------------------------------------------------------------------- |
| **`ValueError`** | If the input string doesn't contain ';base64,' to separate metadata and file data. |

#### Returns:

| Return Type             | Description                                                              | Condition         |
| ----------------------- | ------------------------------------------------------------------------ | ----------------- |
| **`io.BytesIO`**        | The decoded file data (The thing you get when you open a file in Python) | metadata is False |
| **`(io.BytesIO, str)`** | The decoded file data and its metadata                                   | metadata is True  |

#### Example:

```python
>>> input_file = inputs['file']
>>> file, metadata = input_to_file(input_file, metadata = True)
>>> print(metadata)
data:image/jpeg;base64,
>>> type(file)
<class '_io.BytesIO'>
```

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">metadata_to_filetype</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/general_utils.py#LL34C1-L50C21" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

```python
def metadata_to_filetype(metadata):
```

#### Description:

Extracts the file type from the metadata

#### Arguments:

| Argument       | Type    | Description                                                                                    |
| -------------- | ------- | ---------------------------------------------------------------------------------------------- |
| **`metadata`** | **str** | The metadata string in the form "Data:\<MIME type>;base64,"(returned from **`input_to_file`**) |

#### Returns:

| Return Type | Description                 |
| ----------- | --------------------------- |
| **`str`**   | The file type (e.g. "jpeg") |

#### Example:

```python
>>> input_file = inputs['file']
>>> file, metadata = input_to_file(input_file, metadata = True)
>>> print(metadata)
data:image/jpeg;base64,
>>> download_file_type = metadata_to_filetype(metadata)
>>> print(download_file_type)
jpeg
```

## Text

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">string_to_file</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/text_utils.py#LL4C1-L34C85" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

```python
def string_to_file(
    text
    filename= "myfile",
    download_text = "Download File",
)
```

#### Description:

Generates a downloadable text file containing the given text

#### Arguments:

| Argument            | Type               | Description                                                              |
| ------------------- | ------------------ | ------------------------------------------------------------------------ |
| **`text`**          | **str**            | Text to be downloaded                                                    |
| **`filename`**      | **str** (optional) | Name of the download file. (Defaults to "myfile")                        |
| **`download_text`** | **str** (optional) | Text to be displayed as the download link. (Defaults to "Download File") |

#### Raises:

| Exception       | Description                        |
| --------------- | ---------------------------------- |
| **`TypeError`** | If the input text is not a string. |

#### Returns:

| Return Type | Description        |
| ----------- | ------------------ |
| **`str`**   | HTML download link |

#### Example:

#### Python

```python
>>> download_link = string_to_file("Hello World!")
>>> return {"download": download_link}
```

#### Jinja2

```python
# outputs.downloadLink is the html download link generated by the function
{{ outputs.download }}
```

## Spreadsheets

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">file_to_dataframe</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/spreadsheet_utils.py#LL9C1-L34C1" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

```python
def file_to_dataframe(file_data):
```

#### Description:

Converts a base64 encoded file data into a pandas DataFrame

#### Arguments:

| Argument        | Type           | Description                                       |
| --------------- | -------------- | ------------------------------------------------- |
| **`file_data`** | **io.BytesIO** | Decoded file data (e.g. from **`input_to_file`**) |

#### Raises:

| Exception                   | Description                                                                                                 |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **`pd.errors.ParserError`** | If the file data cannot be converted to a DataFrame (i.e. file is not an Excel or CSV file or is corrupted) |

#### Returns:

| Return Type        | Description                      |
| ------------------ | -------------------------------- |
| **`pd.DataFrame`** | DataFrame created from file data |

#### Example:

```python
>>> input_file = inputs['file']
>>> decoded_file = input_to_file(input_file)
>>> df = file_to_dataframe(decoded_file)
>>> print(df)
   A  B  C
0  a  b  c
1  d  e  f
```

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">input_to_dataframe</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/spreadsheet_utils.py#LL35C1-L57C44" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

```python
def input_to_dataframe(file):
```

#### Description:

Converts a base64 encoded file data into a pandas DataFrame

#### Arguments:

| Argument            | Type     | Description                                                          |
| ------------------- | -------- | -------------------------------------------------------------------- |
| **`input_file`**    | **str**  | Base64 encoded file data                                             |
| **`get_file_type`** | **bool** | If True, the function also returns the file type (Defaults to False) |

#### Returns:

| Return Type               | Description                                      | Condition              |
| ------------------------- | ------------------------------------------------ | ---------------------- |
| **`pd.DataFrame`**        | DataFrame created from file data                 | get_file_type is False |
| **`(pd.DataFrame, str)`** | Tuple containing the DataFrame and the file type | get_file_type is True  |

#### Example:

```python
>>> input_file = inputs['file']
>>> df, file_type = input_to_dataframe(input_file, get_file_type = True)
>>> print(df)
   A  B  C
0  a  b  c
1  d  e  f
>>> print(file_type)
csv
```

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">print_dataframe</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/spreadsheet_utils.py#LL60C1-L119C39" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

```python
def print_dataframe(
    df,
    download = False,
    download_text = "Download Table",
    download_file_name = "mytable",
    download_file_type = "csv",
):
```

#### Description:

Creates an HTML table and a download link for a given DataFrame

#### Arguments:

| Argument                 | Type                | Description                                                             |
| ------------------------ | ------------------- | ----------------------------------------------------------------------- |
| **`df`**                 | **pd.DataFrame**    | DataFrame to be converted                                               |
| **`download`**           | **bool** (optional) | If True, function returns a download link (Defaults to False)           |
| **`download_text`**      | **str** (optional)  | Text to be displayed as the download link (Defaults to "Download File") |
| **`download_file_name`** | **str** (optional)  | Name of file when downloaded (Defaults to "myfile")                     |
| **`download_file_type`** | **str** (optional)  | File type of downloaded file (Defaults to "csv")                        |

#### Returns:

| Return Type           | Description                      | Condition         |
| --------------------- | -------------------------------- | ----------------- |
| **`str`**             | HTML table                       | download is False |
| **`Tuple[str, str]`** | (HTML table, HTML download link) | download is True  |

#### Example:

#### Python Code:

```python
>>> input_file = inputs['file']
>>> df = input_to_dataframe(input_file)
>>> table, download = print_dataframe(df, download = True, download_file_name = "FunkyTable", download_text = "Download My Funky Table HERE!", download_file_type = "xlsx")
>>> return {
        "table":table,
        "download":download,
    }
```

#### Output using Jinja2 Template:

```python
# outputs.table is the HTML table
Displaying Table
{{ outputs.table }}

# outputs.download is the download link
Downloading Table
{{ outputs.download }}
```

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">table_to_dataframe</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/table_utils.py#LL4C1-L26C54" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

## Tables

```python
def table_to_dataframe(column_headers, rows) -> pd.DataFrame:
```

#### Description:

Create a DataFrame from given rows and column headers

#### Arguments:

| Argument             | Type                | Description                                                                     |
| -------------------- | ------------------- | ------------------------------------------------------------------------------- |
| **`column_headers`** | **List[str]**       | List of column headers                                                          |
| **`rows`**           | **List[List[str]]** | List of rows to be converted into a DataFrame. Each column is a list of strings |

#### Returns:

| Return Type        | Description                             |
| ------------------ | --------------------------------------- |
| **`pd.DataFrame`** | DataFrame created from headers and rows |

#### Example:

```python
>>> column_headers = ["A", "B", "C"]
>>> rows = [["a", "b", "c"], ["d", "e", "f"]]
>>> df = table_to_dataframe(column_headers, rows)
>>> print(df)
   A  B  C
0  a  b  c
1  d  e  f

```

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">print_table</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/table_utils.py#LL29C1-L44C58" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

```python
print_table(column_headers, rows):
```

#### Description:

Creates an HTML table from given rows and column headers

#### Arguments:

| Argument             | Type                | Description                                                                 |
| -------------------- | ------------------- | --------------------------------------------------------------------------- |
| **`column_headers`** | **List[str]**       | List of column headers                                                      |
| **`rows`**           | **List[List[str]]** | List of rows to be converted into a table. Each column is a list of strings |

#### Returns:

| Return Type | Description                              |
| ----------- | ---------------------------------------- |
| **`str`**   | HTML table created from rows and headers |

#### Example:

#### Python Code:

```python
>>> column_headers = ["A", "B", "C"]
>>> rows = [["a", "b", "c"], ["d", "e", "f"]]
>>> table = print_table(column_headers, rows)
>>> return {
        "table":table,
    }
```

#### Output using Jinja2 Template:

```python
# outputs.table is the HTML table
Displaying Table
{{ outputs.table }}
```

## Images

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">file_to_PIL</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/image_utils.py#LL13C1-L30C88" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

```python
def file_to_PIL(file):
```

#### Description:

Transforms a file into a Pillow Image object

#### Arguments:

| Argument   | Type    | Description                                     |
| ---------- | ------- | ----------------------------------------------- |
| **`file`** | **str** | Decoded file data (returned from input_to_file) |

#### Raises:

| Exception Type   | Description                             |
| ---------------- | --------------------------------------- |
| **`ValueError`** | If the file does not contain image data |

#### Returns:

| Return Type | Description         |
| ----------- | ------------------- |
| **`Image`** | Pillow Image object |

#### Example:

#### Python Code:

```python
>>> input_file = inputs['file']
>>> decoded_file = input_to_file(input_file)
>>> image = file_to_PIL(decoded_file)
>>> return {
        "image":image,
    }
```

#### Output using Jinja2 Template:

```python
# outputs.image is the Pillow Image object
Displaying Image
{{ outputs.image }}
```

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">input_to_PIL</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/image_utils.py#LL33C1-L57C15" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

```python
def input_to_PIL(input_file, get_file_type=False):
```

#### Description:

Converts a base64 encoded file data into a pillow image

#### Arguments:

| Argument            | Type     | Description                                                          |
| ------------------- | -------- | -------------------------------------------------------------------- |
| **`input_file`**    | **str**  | Base64 encoded file data                                             |
| **`get_file_type`** | **bool** | If True, the function also returns the file type (Defaults to False) |

#### Returns:

| Return Type                       | Description              | Condition              |
| --------------------------------- | ------------------------ | ---------------------- |
| **`PIL.Image.Image`**             | Pillow Image object      | get_file_type is False |
| **`Tuple[PIL.Image.Image, str]`** | (pillow image, metadata) | get_file_type is True  |

#### Example:

```python
>>> input_file = inputs['file']
>>> img, file_type = input_to_PIL(input_file, get_file_type=True)
>>> print(file_type)
jpeg
>>> type(img)
<class 'PIL.JpegImagePlugin.JpegImageFile'>
```

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">print_img</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/image_utils.py#LL60C1-L126C32" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

```python
def print_img(
    img,
    width = 200,
    height = 200,
    original_size = False,
    download = False,
    download_text = "Download Image",
    download_file_name= "myimg",
    download_file_type = "png",
):
```

#### Description:

Transforms a Pillow image into an HTML image, with an optional download link

#### Arguments:

| Argument                 | Type                | Description                                                                        |
| ------------------------ | ------------------- | ---------------------------------------------------------------------------------- |
| **`img`**                | **PIL.Image.Image** | Pillow image                                                                       |
| **`width`**              | **int** (optional)  | Output width of the image in pixels (Defaults to 200)                              |
| **`height`**             | **int** (optional)  | Output height of the image in pixels (Defaults to 200)                             |
| **`original_size`**      | **bool** (optional) | If True, the HTML image will be displayed in its original size (Defaults to False) |
| **`download`**           | **bool** (optional) | If True, function returns a download link (Defaults to False)                      |
| **`download_text`**      | **str** (optional)  | The text to be displayed on the download link (Defaults to "Download Image")       |
| **`download_file_name`** | **str** (optional)  | The name of the image file when downloaded (Defaults to "myimg")                   |
| **`download_file_type`** | **str** (optional)  | The file type of the image when downloaded (Defaults to "png")                     |

#### Returns:

| Return Type           | Description                 | Condition         |
| --------------------- | --------------------------- | ----------------- |
| **`str`**             | HTML image                  | download is False |
| **`Tuple[str, str]`** | (HTML image, download link) | download is True  |

#### Example:

#### Python Code:

```python
>>> input_file = inputs['file']
>>> img, metadata = input_to_PIL(input_file)
>>> image, download = print_img(img,, original_size = True, download = True, download_text = "Download Image Here", download_file_name = "myimage", download_file_type = "jpeg")
>>> return {
        "image":image,
        "download":download,
    }
```

#### Output using Jinja2 Template:

```python
# outputs.image is the HTML image
Displaying Image
{{ outputs.image }}

# outputs.download is the download link
Downloading Image
{{ outputs.download }}
```

## Plots

<div style="display: flex; justify-content: space-between; align-items: center;">
  <h3 style="margin: 5px; padding: 0;">print_plot</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/plotting_utils.py#LL8C1-L63C35" style="font-size: larger; margin-bottom: 2em; margin: 5px; padding: 0;"><strong>[Source]</strong></a>
</div>

```python
def print_plot(
    plot_obj,
    width = 500,
    dpi= 100,
    download= False,
    download_text = "Download Plot",
    download_file_name = "myplot",
)
```

#### Description:

Converts a matplotlib.pyplot.axis or matplotlib.figure into an HTML image tag and optionally provides a download link for the image

#### Arguments:

| Argument                 | Type                | Description                                                                 |
| ------------------------ | ------------------- | --------------------------------------------------------------------------- |
| **`plot_obj`**           | **axes or figure**  | Matplotlib figure                                                           |
| **`width`**              | **int** (optional)  | Output width of the image in pixels (Defaults to 500)                       |
| **`dpi`**                | **int** (optional)  | Output dpi of the image in pixels (Defaults to 100)                         |
| **`download`**           | **bool** (optional) | If True, function returns a download link (Defaults to False)               |
| **`download_text`**      | **str** (optional)  | The text to be displayed on the download link (Defaults to "Download Plot") |
| **`download_file_name`** | **str** (optional)  | The name of the image file when downloaded (Defaults to "myplot")           |

#### Returns:

| Return Type           | Description                      | Condition         |
| --------------------- | -------------------------------- | ----------------- |
| **`str`**             | HTML image                       | download is False |
| **`Tuple[str, str]`** | (HTML image, HTML download link) | download is True  |

#### Example:

#### Python Code:

```python
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> x = np.linspace(0, 2 * np.pi, 400)
>>> y = np.sin(x)
>>> fig, ax = plt.subplots()
>>> ax.plot(x, y)
>>> ax.set_title('A single plot')
>>> image, download = print_plot(fig, width = 500, dpi = 100, download = True, download_text = "Download Sin Function Plot", download_file_name = "sin(x)")
>>> return {
        "image":image,
        "download":download,
    }
```

#### Output using Jinja2 Template:

```python
# outputs.image is the HTML image
Displaying Image
{{ outputs.image }}

# outputs.download is the download link
Downloading Image
{{ outputs.download }}
```
