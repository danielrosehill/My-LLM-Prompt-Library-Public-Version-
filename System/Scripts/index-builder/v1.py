import os

# Directory containing markdown files
DOC_FILES_DIR = '/home/daniel/Git/prompt-library-pub/Prompts'
OUTPUT_FILE = os.path.join(DOC_FILES_DIR, 'index.md')

def generate_index():
    with open(OUTPUT_FILE, 'w') as f:
        f.write("# Index\n\n")  # Title of the index

        for root, dirs, files in os.walk(DOC_FILES_DIR):
            for file in files:
                if file.endswith(".md") and file != "index.md":
                    # Get relative path for GitHub-friendly links
                    rel_path = os.path.relpath(os.path.join(root, file), DOC_FILES_DIR)
                    depth = rel_path.count(os.sep)
                    
                    # Write entry to index.md with proper indentation
                    f.write(f"{'  ' * depth}- [{file.replace('.md', '')}]({rel_path.replace(os.sep, '/')})\n")

if __name__ == "__main__":
    generate_index()