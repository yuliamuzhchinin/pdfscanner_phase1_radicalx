import pdfplumber
import re

pdf = pdfplumber.open("resume1.pdf")
p0 = pdf.pages[0]
text = p0.extract_text(x_tolerance = 1, y_tolerance = 1, layout = True)
text = text.casefold()
cleaned_text = re.sub(r'^\s+', '', text, flags=re.MULTILINE)

def extract_sections(text):
    # Define regular expressions for identifying section headers
    section_headers = {
        'experience': re.compile(r'^experience', re.IGNORECASE | re.MULTILINE),
        'education': re.compile(r'^education', re.IGNORECASE | re.MULTILINE),
        'skills': re.compile(r'^skills', re.IGNORECASE | re.MULTILINE),
        "other": re.compile(r'^\s*([^\s]+)\s*', re.IGNORECASE | re.MULTILINE),
        'reference': re.compile(r'^reference', re.IGNORECASE | re.MULTILINE),
        'languages': re.compile(r'^languages', re.IGNORECASE | re.MULTILINE),
        'projects': re.compile(r'^projects', re.IGNORECASE | re.MULTILINE)
    }

    # Initialize a dictionary to store the extracted content for each section
    sections = {key: '' for key in section_headers}
    sections_list = []
    # Find the starting index of each section
    for section, pattern in section_headers.items():
        match = pattern.search(text)
        if match:
            sections[section] = match.start()
    filtered_sections = {x: y for x, y in sections.items() if y != ''}
    sections_list= list(filtered_sections.values())
    sections_list.sort()

    # Extract content for each section
    for section, start_index in filtered_sections.items():
        # Loop through each coordinate in the list
        if sections_list[-1] == start_index:
            end_val = len(input_string)
        else:
            end_val = None
            for idx in sections_list:
                # Check if the current coordinate is bigger than the assigned value
                if idx > start_index:
                    if end_val is None or int(idx) < end_val:
                        end_val = idx
        end_index = end_val
        sections[section] = text[start_index:end_index].strip()

    return sections

input_string = cleaned_text

result = extract_sections(input_string)

# Print the sections
for header, section in result.items():
    print(f"--- {header} ---\n{section}\n")