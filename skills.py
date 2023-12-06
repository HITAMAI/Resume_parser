import re
import docx2txt
from pdfminer.high_level import extract_text

EMAIL_REG = re.compile(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None

def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)

def extract_skills(resume_text):
    # You may read the database from a CSV file or some other database
    SKILLS_DB = [
        'machine learning',
        'data science',
        'python',
        'word',
        'excel',
        'english',
        'java',
        'sql',
        'communication',
        'teamwork',
        'problem solving',
    ]

    found_skills = set()

    for skill in SKILLS_DB:
        if skill.lower() in resume_text.lower():
            found_skills.add(skill)

    return found_skills

if __name__ == '__main__':
    pdf_path = 'ADUPA_NITHIN_SAI.pdf'
    docx_path = 'shiva.docx'

    # Extract skills from PDF
    pdf_text = extract_text_from_pdf(pdf_path)
    pdf_skills = extract_skills(pdf_text)

    if pdf_skills:
        print("Skills from PDF:")
        print(pdf_skills)

    # Extract skills from DOCX
    docx_text = extract_text_from_docx(docx_path)
    docx_skills = extract_skills(docx_text)

    if docx_skills:
        print("\nSkills from DOCX:")
        print(docx_skills)
