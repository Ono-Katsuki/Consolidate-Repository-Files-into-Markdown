import os
import base64
import requests
from github import Github
from dotenv import load_dotenv
import mimetypes

def get_file_content(repo, file_path):
    try:
        content = repo.get_contents(file_path)
        return base64.b64decode(content.content).decode('utf-8')
    except Exception as e:
        print(f"Error reading file {file_path}: {str(e)}")
        return None

def get_file_extension(file_path):
    return os.path.splitext(file_path)[1].lower()

def is_binary_file(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and not mime_type.startswith('text')

def process_file(repo, file_path, output_file, depth):
    file_content = get_file_content(repo, file_path)
    if file_content is not None:
        ext = get_file_extension(file_path)
        output_file.write(f"{'#' * (depth + 2)} File: {os.path.basename(file_path)}\n\n")
        
        if is_binary_file(file_path):
            output_file.write(f"*This is a binary file ({ext}). Content not displayed.*\n\n")
        else:
            lang = get_language_for_markdown(ext)
            output_file.write(f"```{lang}\n")
            output_file.write(file_content)
            output_file.write("\n```\n\n")

def get_language_for_markdown(ext):
    language_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.html': 'html',
        '.css': 'css',
        '.java': 'java',
        '.cpp': 'cpp',
        '.c': 'c',
        '.rb': 'ruby',
        '.php': 'php',
        '.swift': 'swift',
        '.go': 'go',
        '.rs': 'rust',
        '.ts': 'typescript',
        '.sh': 'bash',
        '.yaml': 'yaml',
        '.json': 'json',
        '.md': 'markdown',
        '.sql': 'sql',
        '.xml': 'xml',
    }
    return language_map.get(ext, '')

def process_directory(repo, path, output_file, depth=0):
    contents = repo.get_contents(path)
    
    # Sort contents: directories first, then files
    dirs = [content for content in contents if content.type == "dir"]
    files = [content for content in contents if content.type != "dir"]
    
    # Process directories
    for content in sorted(dirs, key=lambda x: x.path):
        output_file.write(f"{'#' * (depth + 1)} Directory: {os.path.basename(content.path)}\n\n")
        process_directory(repo, content.path, output_file, depth + 1)
    
    # Process files
    for content in sorted(files, key=lambda x: x.path):
        process_file(repo, content.path, output_file, depth)

def get_user_repositories(g):
    user = g.get_user()
    repos = user.get_repos()
    return list(repos)

def display_repositories(repos):
    print("Your repositories:")
    for i, repo in enumerate(repos, 1):
        print(f"{i}. {repo.full_name}")

def get_user_choice(repos):
    while True:
        try:
            choice = int(input("Enter the number of the repository you want to convert: "))
            if 1 <= choice <= len(repos):
                return repos[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    load_dotenv()
    github_token = os.getenv('GITHUB_TOKEN')
    
    g = Github(github_token)
    
    repos = get_user_repositories(g)
    display_repositories(repos)
    selected_repo = get_user_choice(repos)
    
    output_filename = input("Enter the output Markdown filename: ")
    
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(f"# Repository: {selected_repo.full_name}\n\n")
        process_directory(selected_repo, "", output_file)
    
    print(f"Repository contents have been saved to {output_filename}")

if __name__ == "__main__":
    main()
