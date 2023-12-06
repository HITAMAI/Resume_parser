import docx2txt
from pdfminer.high_level import extract_text
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

RESERVED_WORDS = [
    'school',
    'college',
    'univers',
    'academy',
    'faculty',
    'institute',
    'faculdades',
    'schola',
    'schule',
    'lise',
    'lyceum',
    'lycee',
    'polytechnic',
    'kolej',
    'ünivers',
    'okul',
]

def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_education(input_text):
    organizations = []

    for sent in nltk.sent_tokenize(input_text):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'ORGANIZATION':
                organizations.append(' '.join(c[0] for c in chunk.leaves()))

    education = set()
    for org in organizations:
        for word in RESERVED_WORDS:
            if org.lower().find(word) >= 0:
                education.add(org)

    return education

if __name__ == '__main__':
    docx_path = 'shiva.docx'
    docx_text = extract_text_from_docx(docx_path)
    education_information_docx = extract_education(docx_text)
    print("Education information from DOCX:")
    print(education_information_docx)

    pdf_path = 'ADUPA_NITHIN_SAI.pdf'  
    pdf_text = extract_text_from_pdf(pdf_path)
    education_information_pdf = extract_education(pdf_text)
    print("\nEducation information from PDF:")
    print(education_information_pdf)
