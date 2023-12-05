# SRM Builder

Python code to create oscal content for evaluating the SRM.

From project root:

```
cd examples/srm/builder
```

#### Initialize Virtual Environment (For New Environment)

```
python3 -m venv .nist-srm-builder
```

#### Activate Environment (Windows)

```
.nist-srm-builder\Scripts\activate.bat
```

#### Activate Environment (macOS)

```
source .nist-srm-builder/bin/activate
```

#### Install Requirements

```
pip install -e ../OSCALic
pip3 install -r requirements.txt
```

### Running the Command Line Interface (CLI)

#### Available Commands

Generate SRM content.

```
python3 generate.py
```

Build visualization.

```
output_path=../generated python3 graph.py
```