# Type of Python

## About

- List
- Dict
- Tuple
- Union
- TypedDict
- NamedTuple
- Final

## Required

- python == 3.8
  ```bash
  conda create -n python38 python=3.8
  conda activate python38
  ```
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)

  - Install Pylance from marketplace of VScode.
  - Set up settings.json. Add following:

    ```json:settings.json
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic",
    ```
