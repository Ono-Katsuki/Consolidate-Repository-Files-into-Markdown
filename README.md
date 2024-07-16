# GitHub Repository to Markdown Converter

This Python script allows you to convert an entire GitHub repository into a single Markdown file, preserving the directory structure and file contents.

## Features

- Converts all text-based files in a GitHub repository to Markdown format
- Preserves directory structure using Markdown headers
- Handles binary files by noting their presence without including content
- Applies appropriate syntax highlighting based on file extensions
- Sorts contents alphabetically, with directories appearing before files

## Prerequisites

- Python 3.6 or higher
- GitHub Personal Access Token

### How to Get a GitHub Personal Access Token

1. Log in to your GitHub account.
2. Click on your profile picture in the top-right corner and select "Settings".
3. Scroll down the left sidebar and click on "Developer settings".
4. In the left sidebar, click on "Personal access tokens", then select "Tokens (classic)".
5. Click "Generate new token" and select "Generate new token (classic)".
6. Give your token a descriptive name (e.g., "GitHub Repo to Markdown Converter").
7. Select an expiration period for the token (for security, choose a short duration).
8. Under "Select scopes", check the box next to "repo" to grant access to your repositories.
9. Click "Generate token" at the bottom of the page.
10. Copy the generated token immediately and store it securely. You won't be able to see it again!

**Note:** Treat your Personal Access Token like a password. Never share it or store it in a public place.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Ono-Katsuki/Consolidate-Repository-Files-into-Markdown.git
   cd Consolidate-Repository-Files-into-Markdown
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your GitHub token:
   ```
   GITHUB_TOKEN=your_github_personal_access_token_here
   ```

## Usage

Run the script using Python:

```
python main.py
```

The script will display a list of your repositories. Enter the number corresponding to the repository you want to convert.

## Output

The script will generate a single Markdown file containing:

- The entire directory structure of the repository
- The contents of all text-based files
- Placeholders for binary files

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
