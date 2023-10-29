import typing
from typing import Dict
from typing import List
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from transformers import GPT2Tokenizer, GPT2Model


# juierror/flan-t5-text2sql-with-schema-v2

tokenizer = AutoTokenizer.from_pretrained("juierror/flan-t5-text2sql-with-schema-v2")
model = AutoModelForSeq2SeqLM.from_pretrained("juierror/flan-t5-text2sql-with-schema-v2")

def get_prompt(tables, question) -> str :
    prompt = f"""convert question and table into SQL query. tables: {tables}. question: {question}"""
    return prompt

def prepare_input(question: str, tables: Dict[str, List[str]]) -> torch.Tensor :
    tables = [f"""{table_name}({",".join(tables[table_name])})""" for table_name in tables]
    tables = ", ".join(tables)
    prompt = get_prompt(tables, question)
    input_ids = tokenizer(prompt, max_length=512, return_tensors="pt").input_ids
    return input_ids

def inference(question: str, tables: Dict[str, List[str]]) -> str:
    input_data = prepare_input(question=question, tables=tables)
    input_data = input_data.to(model.device)
    outputs = model.generate(inputs=input_data, num_beams=10,  max_length=512, do_sample=True, top_k=25, temperature=0.7)
    result = tokenizer.decode(token_ids=outputs[0], skip_special_tokens=True)
    return result


def inference2(question_and_table: str) -> str:
    prompt = f"""convertion question and table into PSQL query. question and table: {question_and_table} """
    input_ids = tokenizer(prompt, max_length=512, return_tensors="pt").input_ids
    input_data = input_ids.to(model.device)
    outputs = model.generate(inputs=input_data, num_beams=10,  max_length=512, do_sample=True, top_k=25, temperature=1)
    result = tokenizer.decode(token_ids=outputs[0], skip_special_tokens=True)
    return result
    

print(inference("find total number of employee and the median salary (50th percentile) of employees from marketing department", {
    "people": ["id", "name", "address", "zip_code", "phone_number"],
    "employee": ["id", "people_id", "company", "department", "role", "salary"]
}))

