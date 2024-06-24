from markdown_pdf import MarkdownPdf, Section

from chatgpt import ChatGPT


API_KEY = "YOUR API KEY"

def main() -> None:
    """Creates the answer pdf with the answers from ChatGPT."""
    input_file = input('Questions file: ')
    output_file = input('Output file: ')
    chatgpt = ChatGPT(API_KEY)
    pdf = MarkdownPdf(toc_level=1)

    try:
        with open(input_file, 'r') as file:
            questions = file.read().split('\n')
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        return
    except Exception as e:
        print(f"An error occured while reading the file: {e}")
        return
    
    for i, question in enumerate(questions, start=1):
        if question.strip():    # skip empty lines
            try:
                answer = chatgpt.response(question)
                section = Section(f"### {question}\n{answer}")
                pdf.add_section(section)
                print(f"Processed question {i}/{len(questions)}")
            except Exception as e:
                print(f"An error occured while processing the question '{question}': {e}")

    try:
        pdf.save(output_file)
        print(f"PDF saved successfully as {output_file}")
    except Exception as e:
        print(f"An error occured while saving the PDF: {e}")
        

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occured: {e}")