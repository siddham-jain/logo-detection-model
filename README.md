# Logo Detection ML model- VideoVerse Assignment

This repo contains code for the assignment.

Approach doc link :- [link](https://github.com/siddham-jain/logo-detection-model/blob/master/Logo%20Detection%20Pipeline%20-%20Approach.md)

## Setup Instructions
Assuming you have Python installed in your system. If not use

For Linux:-
```bash
sudo apt install python3
```

For Mac:-
```bash
brew install python
```

For Windows
```bash
choco install python
```
After installation:- 

1. Clone this repository:

    ```bash
    git clone https://github.com/siddham-jain/logo-detection-model
    cd logo-detection-model
    ```

2. Create a virtual environment and install the dependencies

    ```bash
    python3 -m venv <your_env_name>
    source <your_env_name>/bin/activate
    pip install -r requirements.txt
    ```
## Usage Instructions

1. Run the pipeline using
```bash
python3 main.py <path_to_your_video_file>
```
2. Output file will be generated as ```output.json``` in the directory

## Example Output
```json
{
    "Pepsi_pts": [
        {
            "timestamp": 0.2,
            "distance_from_center": 193.478,
            "size": {
                "width": 79.146,
                "height": 75.144
            }
            // rest of the detected frames
    ],
    "CocaCola_pts": [
        {
            "timestamp": 0.2,
            "distance_from_center": 180.646,
            "size": {
                "width": 89.274,
                "height": 252.274
            }
        },
        // rest of the detected frames
    ]
}
```
## Error handling
If your IDE is crashing while trying to run this script try trimming your video according to your system requirements
