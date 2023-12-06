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

if __name__ == '__main__':
    pdf_path = 'ADUPA_NITHIN_SAI.pdf'
    docx_path = 'shiva.docx'

    pdf_text = extract_text_from_pdf(pdf_path)
    pdf_emails = extract_emails(pdf_text)

    if pdf_emails:
        print("Emails from PDF:")
        print(pdf_emails[0])

    docx_text = extract_text_from_docx(docx_path)
    docx_emails = extract_emails(docx_text)

    if docx_emails:
        print("\nEmails from DOCX:")
        print(docx_emails[0])
