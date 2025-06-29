# Quick and dirty prompt extraction from a documented prompt.
# If you want to edit the prompt, consider changing the .md documentation, updating the documentation accordingly ;) and extracting the prompt for trial purposes.
# This script extracts the text from within all <strong> html blocks and strips \ characters. 
# That means your prompt shouldn't have \ characters, as they will be removed :p
from bs4 import BeautifulSoup

def extract_strong_text(md_file_path, output_txt_path):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    strong_texts = [tag.get_text(strip=True) for tag in soup.find_all('strong')]
    # Extract text inside <strong> tags and strip backslashes
    strong_texts = [
        tag.get_text(strip=True).replace('\\', '')
        for tag in soup.find_all('strong')
    ]

    with open(output_txt_path, 'w', encoding='utf-8') as out:
        for line in strong_texts:
            out.write(line + '\n')

# Example usage
if __name__ == "__main__":
    input_md = "docs/Documentation.md"
    output_txt = "THAL.txt"
    extract_strong_text(input_md, output_txt)
