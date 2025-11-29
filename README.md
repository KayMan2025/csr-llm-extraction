📄 **Clinical Study Report (CSR) LLM Extraction \& Summarization**

Python + Groq LLaMA 3.1 | End-to-End Data Extraction Pipeline



This project demonstrates how Large Language Models (LLMs) can extract structured information and generate clinically relevant summaries from CSR-like free text. It replicates real-world tasks used in clinical development, pharmacometrics, regulatory writing, and AI-assisted medical data workflows.



This is a portfolio project created to showcase skills relevant to roles such as Data Scientist (AI/ML), LLM Engineer, and positions at companies like Certara, JAX, Genentech, Pfizer, etc.



🚀 What This Tool Does



Given an input text file (e.g., sample\_csr.txt), the pipeline:



✔️ 1. Extracts structured clinical trial fields



The LLM parses CSR narrative text into machine-friendly JSON:



trial\_id



title



indication



phase



sample\_size



arms\_and\_treatments



primary\_endpoint



key\_results



serious\_adverse\_events



sponsor



location



This mirrors real extraction tasks needed for:



Clinical trial registries



Pharmacovigilance



Medical writing automation



Data standardization for modeling (PK/PD, survival, etc.)



✔️ 2. Generates dual-layer summaries



The system produces:



🔹 Plain-Language Summary



— Accessible to non-scientific readers, patients, caregivers.



🔹 Technical Summary for Clinicians



— Uses clinical terminology and meaningful endpoints (Mayo score, remission, AEs, etc.)



These summaries are useful for:



Study synopses



CSR-to-protocol automation



Patient engagement documents



Internal medical review



🧠 Example Output

{

&nbsp; "structured": {

&nbsp;   "trial\_id": "Not provided",

&nbsp;   "title": "Evaluating Drug X in Adults with Moderate to Severe Ulcerative Colitis",

&nbsp;   "indication": "Ulcerative colitis",

&nbsp;   "phase": "Phase II",

&nbsp;   "sample\_size": "120 patients",

&nbsp;   "arms\_and\_treatments": "Drug X 100 mg once daily vs. placebo",

&nbsp;   "primary\_endpoint": "Clinical remission at week 12 based on the Mayo score",

&nbsp;   "key\_results": "45% remission with Drug X vs. 20% with placebo",

&nbsp;   "serious\_adverse\_events": "Mild to moderate headache and nausea",

&nbsp;   "sponsor": "Example Pharma",

&nbsp;   "location": "20 sites in the US and Europe"

&nbsp; },

&nbsp; "summaries": {

&nbsp;   "summary": "..."

&nbsp; }

}



🏗️ Project Architecture

csr\_project/

├─ data/

│  └─ sample\_csr.txt

├─ src/

│  ├─ main.py                 # CLI orchestrator

│  ├─ llm\_client.py           # Groq API client wrapper

│  ├─ extract\_structured.py   # JSON field extraction

│  ├─ summarize\_csr.py        # Summary generation

│  ├─ prompts.py              # Prompt templates

│  ├─ config.py               # Field schema

│  └─ \_\_init\_\_.py

├─ README.md

├─ requirements.txt

├─ .gitignore

└─ .env   # <--- NOT committed



⚙️ Tech Stack

Component	Details

Language	Python 3.12

LLM Provider	Groq (ultra-fast inference)

Model	llama-3.1-8b-instant

CLI	argparse

Environment	python-dotenv, virtualenv



This stack closely matches real AI/ML workflows used in biotech and pharma.



🔧 Installation

1\. Clone the repo

git clone <your-repo-url>

cd csr\_project



2\. Create virtual environment

python -m venv .venv

.\\.venv\\Scripts\\activate

pip install -r requirements.txt



3\. Set up your .env file



Create a file named .env in the project root:



GROQ\_API\_KEY=your-groq-key-here





⚠️ This file is ignored by .gitignore to protect your secrets.



▶️ Run the Tool

python -m src.main --input data\\sample\_csr.txt





Produces combined structured + summarized output to the terminal.



🎯 Goals of This Project



Demonstrate applied LLM engineering on biomedical text



Show ability to build end-to-end data extraction pipelines



Implement prompt design, JSON post-processing, and error handling



Build a lightweight clinical NLP tool from scratch



Provide a real-world example aligned with clinical data workflows used in



modeling \& simulation



medical writing



regulatory submissions



pharmacovigilance



data standardization



📌 Next Extensions (optional future improvements)



Add R/Shiny or Streamlit UI



Add PDF ingestion



Add automatic schema validation



Add vector search / RAG for large CSRs



Add evaluation metrics (BLEU, RougeL, JSON correctness)



📫 Contact



Author: Kibrom M. Alula



LinkedIn: https://www.linkedin.com/in/kibrom-m-alula/



GitHub: https://github.com/KayMan2025

