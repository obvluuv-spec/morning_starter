# App & Website Launcher

A simple Python script that automatically opens multiple websites in a specified web browser and launches local applications. All websites and application paths are managed through a single configuration file.

## Features

- Open multiple websites in a specified browser.
- Launch local applications using their file paths.
- Manage websites and applications through `application.txt`.
- Automatically add `https://` to website addresses when no protocol is specified.
- Skip applications whose paths do not exist.
- Configure delays between launch operations.

## Requirements

- Python 3.x
- An installed web browser
- Local applications that can be launched from their executable paths

No additional Python packages are required. The script uses Python's standard library.

## Installation

1. Clone the repository:```
   git clone https://github.com/obvluuv-spec/morning_starter.git
   ```
2. Navigate to the project directory:```
   cd YOUR-REPOSITORY
   ```
3. Create an `application.txt` file in the project directory.
4. Set the path to your preferred browser in the Python script.

## Configuration

### Browser Path

Set the `browser_path` variable to the location of your browser executable.

Example for Google Chrome on Windows:

```
browser_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
```

The path may vary depending on your installation.

### Application and Website List

Add your websites and application paths to `application.txt`.

Example:

```
website: https://www.google.com
website: https://github.com
website: https://www.youtube.com

app: "C:\Windows\System32\notepad.exe"
app: "C:\Windows\System32\calc.exe"
```

**Configuration syntax:**

- `website:` defines a website to open.
- `app:` defines a local application to launch.
- Each entry must be on a separate line.
- Quotation marks around application paths are optional.
- Entries are processed in the order in which they appear within their respective categories.

You can add as many websites and applications as needed.

## Usage

Run the Python script from your terminal:

```
python main.py
```

Replace `main.py` with the actual filename of your script if necessary.

The script performs the following steps:

1. Reads the configuration from `application.txt`.
2. Opens each configured website in the selected browser.
3. Waits three seconds between website launches.
4. Starts the configured applications after opening the websites.
5. Waits ten seconds between application launches.
6. Skips applications whose specified paths do not exist.

## Project Structure

```
morning_starter/
├── main.py
├── application.txt
└── README.md
```

- `main.py` — Main Python script.
- `application.txt` — Configuration file containing website URLs and application paths.
- `README.md` — Project documentation.

## Customization

You can adjust the delays between launch operations directly in the script:

```
time.sleep(3)   # Delay between websites
time.sleep(10)  # Delay between applications
```

You can also change the browser executable path and modify `application.txt` whenever you want to update your launch list.

## Limitations

- File paths must be valid for your operating system.
- The browser executable must exist at the specified location.
- Invalid URLs and website connection errors are not explicitly handled.
- Applications with missing paths are skipped.
- The script does not currently provide a graphical user interface.


If you find this project useful, feel free to star the repository or contribute improvements.
