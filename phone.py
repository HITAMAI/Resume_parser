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

if __name__ == '__main__':
    docx_path = 'shiva.docx'
    pdf_path = 'ADUPA_NITHIN_SAI.pdf'

    docx_text = extract_text_from_docx(docx_path)
    names = extract_names(docx_text)
    phone_number = extract_phone_number(docx_text)

    if names:
        print(f"Name: {names[0]}")

    if phone_number:
        print(f"Phone Number: {phone_number}")

    pdf_text = extract_text_from_pdf(pdf_path)
    names = extract_names(pdf_text)
    phone_number = extract_phone_number(pdf_text)

    if names:
        print(f"Name: {names[0]}")

    if phone_number:
        print(f"Phone Number: {phone_number}")
