import re
import docx2txt
import nltk
from pdfminer.high_level import extract_text

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')

def extract_text_from_docx(docx_path):
    txt = docx2txt.process(docx_path)
    if txt:
        return txt.replace('\t', ' ')
    return None

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_names(txt):
    person_names = []

    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )

    return person_names

def extract_phone_number(txt):
    phone = re.findall(PHONE_REG, txt)
    if phone:
        return ''.join(phone[0])
    return None

def extract_fields_from_docx(docx_path):
    text = extract_text_from_docx(docx_path)
    names = extract_names(text)
    phone_number = extract_phone_number(text)

    return {'Names': names, 'Phone Number': phone_number}

def extract_fields_from_pdf(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    names = extract_names(text)
    phone_number = extract_phone_number(text)

    return {'Names': names, 'Phone Number': phone_number}

if __name__ == '__main__':
    docx_path = 'shiva.docx'
    pdf_path = 'ADUPA_NITHIN_SAI.pdf'

    # Extract fields from DOCX
    docx_fields = extract_fields_from_docx(docx_path)
    print("Fields from DOCX:")
    print(docx_fields)

    # Extract fields from PDF
    pdf_fields = extract_fields_from_pdf(pdf_path)
    print("\nFields from PDF:")
    print(pdf_fields)
