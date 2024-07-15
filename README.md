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

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/github-repo-to-markdown.git
   cd github-repo-to-markdown
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
python github_repo_to_markdown.py
```

Follow the prompts to enter the GitHub repository (in the format `owner/repo`) and the desired output filename.

## Output

The script will generate a single Markdown file containing:

- The entire directory structure of the repository
- The contents of all text-based files
- Placeholders for binary files

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
