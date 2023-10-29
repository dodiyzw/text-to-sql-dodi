# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM
# tokenizer = AutoTokenizer.from_pretrained("NumbersStation/nsql-llama-2-7B")
# model = AutoModelForCausalLM.from_pretrained("NumbersStation/nsql-llama-2-7B", torch_dtype=torch.bfloat16)

# text = """
# The two tables are: 

# "people": ["id", "name", "address", "zip_code", "phone_number"],
#     "employee": ["id", "people_id", "company", "department", "role", "salary"]

# -- Using valid PostgresQL, answer the following questions for the tables provided above.

# -- find total number of employee and the median salary (50th percentile) of employees from marketing department.

# SELECT"""

# input_ids = tokenizer(text, return_tensors="pt").input_ids

# generated_ids = model.generate(input_ids, max_length=500)
# print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
