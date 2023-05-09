# Mecsimcalc 0.0.3 documentation

This library is designed to provide a set of functions for handling and converting various types of data, such as base64 encoded data, Pandas DataFrames, and Pillow images.

- [GitHub Repository](https://github.com/MecSimCalc/MecSimCalc-utils)
- [PyPi Page](https://pypi.org/project/mecsimcalc/)

## General

<div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
  <h3 style={{ margin: 5, padding: 0 }}>decode_file_data</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/MecSimCalc.py#LL8C1-L29C61" style={{ fontSize: 'larger', marginBottom: '2em', margin: 5, padding: 0 }}><strong>[Source]</strong></a>
</div>



```python
def decode_file_data(encoded_data, metadata = False)
```

#### Description:

Converts a base64 encoded file into a file object and metadata

#### Arguments:

| Argument           | Type                | Description                                                     |
| ------------------ | ------------------- | --------------------------------------------------------------- |
| **`encoded_data`** | **str**             | Base64 encoded file data                                        |
| **`metadata`**     | **bool** (optional) | If True, function returns file and metadata (Defaults to False) |

#### Returns:

| Return Type             | Description                   | Condition         |
| ----------------------- | ----------------------------- | ----------------- |
| **`io.BytesIO`**        | The decoded file data         | metadata is False |
| **`(io.BytesIO, str)`** | The decoded file and metadata | metadata is True  |

#### Example:

```python
>>> inputFile = inputs['file']
>>> file, metadata = decode_file_data(inputFile, metadata = True)
>>> print(metadata)
data:image/jpeg;base64,
>>> print(file)
<_io.BytesIO object at 0x0000000000000000>
```

## Tables/DataFrames

<div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
  <h3 style={{ margin: 5, padding: 0 }}>file_data_to_dataframe</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/MecSimCalc.py#LL32C1-L52C14" style={{ fontSize: 'larger', marginBottom: '2em', margin: 5, padding: 0 }}><strong>[Source]</strong></a>
</div>

```python
def file_data_to_dataframe(file_data):
```

#### Description:

Converts a file object into a pandas DataFrame

#### Arguments:

| Argument        | Type           | Description                                          |
| --------------- | -------------- | ---------------------------------------------------- |
| **`file_data`** | **io.BytesIO** | Decoded file data (e.g. from **`decode_file_data`**) |

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
>>> inputFile = inputs['file']
>>> file, metadata = decode_file_data(inputFile, metadata = True)
>>> df = file_data_to_dataframe(file)
>>> print(df)
   A  B  C
```

<div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
  <h3 style={{ margin: 5, padding: 0 }}>input_to_dataframe</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/MecSimCalc.py#LL55C1-L67C44" style={{ fontSize: 'larger', marginBottom: '2em', margin: 5, padding: 0 }}><strong>[Source]</strong></a>
</div>

```python
def input_to_dataframe(file):
```

#### Description:

Converts a base64 encoded file data into a pandas DataFrame

#### Arguments:

| Argument   | Type    | Description              |
| ---------- | ------- | ------------------------ |
| **`file`** | **str** | Base64 encoded file data |

#### Returns:

| Return Type        | Description                      |
| ------------------ | -------------------------------- |
| **`pd.DataFrame`** | DataFrame created from file data |

#### Example:

```python
>>> inputFile = inputs['file']
>>> df = input_to_dataframe(inputFile)
>>> print(df)
   A  B  C
```

<div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
  <h3 style={{ margin: 5, padding: 0 }}>dataframe_to_output</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/MecSimCalc.py#LL70C1-L95C1" style={{ fontSize: 'larger', marginBottom: '2em', margin: 5, padding: 0 }}><strong>[Source]</strong></a>
</div>

```python
def dataframe_to_output(
    df,
    DownloadText = "Download File",
    DownloadFileName = "myfile",
):
```

#### Description:

Creates an HTML table and a download link for a given DataFrame

#### Arguments:

| Argument               | Type               | Description                                                             |
| ---------------------- | ------------------ | ----------------------------------------------------------------------- |
| **`df`**               | **pd.DataFrame**   | DataFrame to be converted                                               |
| **`DownloadText`**     | **str** (optional) | Text to be displayed as the download link (Defaults to "Download File") |
| **`DownloadFileName`** | **str** (optional) | Name of file when downloaded (Defaults to "myfile")                     |

#### Returns:

| Return Type | Description |
|**`Tuple[str, str]`**| (HTML table, download link)|

#### Example:

#### Python Code:

```python
>>> inputFile = inputs['file']
>>> df = input_to_dataframe(inputFile)
>>> table, download = dataframe_to_output(df, DownloadFileName = "mytable", DownloadText = "Download Table")
>>> return {
        "table":table,
        "download"download,
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

## Images


<div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
  <h3 style={{ margin: 5, padding: 0 }}>input_to_PIL</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/MecSimCalc.py#LL97C1-L113C25" style={{ fontSize: 'larger', marginBottom: '2em', margin: 5, padding: 0 }}><strong>[Source]</strong></a>
</div>

```python
def input_to_PIL(file):
```

#### Description:

Converts a base64 encoded file data into a pillow image

#### Arguments:

| Argument   | Type    | Description              |
| ---------- | ------- | ------------------------ |
| **`file`** | **str** | Base64 encoded file data |

#### Returns:

| Return Type                       | Description              |
| --------------------------------- | ------------------------ |
| **`Tuple[PIL.Image.Image, str]`** | (pillow image, metadata) |


<div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
  <h3 style={{ margin: 5, padding: 0 }}>print_img</h3>
  <a href="https://github.com/MecSimCalc/MecSimCalc-utils/blob/main/mecsimcalc/MecSimCalc.py#LL115C1-L168C31" style={{ fontSize: 'larger', marginBottom: '2em', margin: 5, padding: 0 }}><strong>[Source]</strong></a>
</div>

```python
def print_img(
    img,
    metadata,
    WIDTH = 200,
    HEIGHT = 200,
    OriginalSize = False,
    DownloadText = "Download Image",
    ImageName= "myimg",
):
```

#### Description:

Converts a pillow image into an HTML image and a download link

#### Arguments:

| Argument           | Type                | Description                                                                        |
| ------------------ | ------------------- | ---------------------------------------------------------------------------------- |
| **`img`**          | **PIL.Image.Image** | Pillow image                                                                       |
| **`metadata`**     | **str**             | Image metadata                                                                     |
| **`WIDTH`**        | **int** (optional)  | Output width of the image in pixels (Defaults to 200)                              |
| **`HEIGHT`**       | **int** (optional)  | Output height of the image in pixels (Defaults to 200)                             |
| **`OriginalSize`** | **bool** (optional) | If True, the HTML image will be displayed in its original size (Defaults to False) |
| **`DownloadText`** | **str** (optional)  | The text to be displayed on the download link (Defaults to "Download Image")       |
| **`ImageName`**    | **str** (optional)  | The name of the image file when downloaded (Defaults to "myimg")                   |

#### Returns:

| Return Type           | Description                 |
| --------------------- | --------------------------- |
| **`Tuple[str, str]`** | (HTML image, download link) |

#### Example:

#### Python Code:

```python
>>> inputFile = inputs['file']
>>> img, metadata = input_to_PIL(inputFile)
>>> image, download = print_img(img, metadata, OriginalSize = True, DownloadText = "Download Image Here", ImageName = "myimage")
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
