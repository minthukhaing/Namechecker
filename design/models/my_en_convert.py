import models.mm_preprocess as p
import models.mm_transpitor as mm
import json
import asyncio
from aiofile import async_open

async def load_mappings():
    async with async_open('./models/mm_eng_mapping.json', 'r') as f:
        response_mm = await f.read()
   

    mapping_mm = json.loads(response_mm)
    return  mapping_mm

async def myan(txt):
    mapped_names = ''
    input_text=txt
    mapping_mm= await load_mappings()   
    word_dict=mapping_mm

    # Step 1: Preprocess
    normalized_text = p.normalize_text(input_text)
    processed_text = p.preprocess(normalized_text)
  
    word_list = processed_text.split(' ')
    mapped_names = ' '.join(p.get_map(word, word_dict) for word in word_list)
   
    input_code_point = ''.join(hex(ord(char)) for char in processed_text)
    output_text= ' '.join(word.capitalize() for word in mapped_names.split())
    #output_text = p.capitalize(mapped_names)
    #print("result str : "+ output_text)
    return output_text

