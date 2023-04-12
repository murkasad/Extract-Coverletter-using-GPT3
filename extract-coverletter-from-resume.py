from PyPDF2 import PdfReader
import openai
openai.api_key="paste your open-ai api key here"


def convert_pdf(resume):
    
    reader = PdfReader(resume)
    page = reader.pages[0]
    text = page.extract_text()
    return text

def extract_letter(filename):
    
    company_name = "NPower Canada"
    role = "Data Analyst"
    contact_person = "Hiring Manager"
    your_name = "Murk Asad"
    job_desc = "this role will allow me to work on technically challenging problems and create impactful solutions while working with an innovative team. " 

    text=convert_pdf(filename)

    prompt = ("Write a cover letter to " + contact_person + " from " + your_name +" for a " + role 
                    + " job at " + company_name +"." + " I am excited about the job because " +job_desc +"."
                    + "Some details from my experience and skill are here in my resume: "+ text)

    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=500,
    temperature=0.4
    )

    cover_letter=response["choices"][0]["text"]

    keep_index = cover_letter.find("Dear") #remove all irrelevant stuff before "Dear Hiring manager"
    updated_letter = cover_letter[keep_index:]

    print(updated_letter)

if __name__=="__main__":
    filename="MurkAsadResume.pdf"
    extract_letter(filename)