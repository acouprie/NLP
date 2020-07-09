import os
import json
import re
import html

# constants
ROOT_FOLDER = "/projets/prevision/"
DATASET_ROOT_FOLDER = ROOT_FOLDER + "datasets/ukenvironmental/"
JSON_FILE_NAME = DATASET_ROOT_FOLDER + "all_sentences.json"

# Data cleaning
def cleanhtml(raw_html):
    string = html.unescape(raw_html)
    clean_annot = re.compile("<[^>]*>")
    cleantext = re.sub(clean_annot, '', string)
    #clean_n = re.compile("\\n")
    #cleantext = re.sub(clean_n, '', cleantext)
    return cleantext

# Extract and clean data to json file
if not os.path.isfile(JSON_FILE_NAME):
    data = {}
    json_file = open(JSON_FILE_NAME,"w")
    
    for i in range(1, 11):
        # ignore folder 2, 3 and 4
        if i in [2, 3, 4]:
            continue
        path = DATASET_ROOT_FOLDER + "DoD Issue " + str(i)
        doc_name = str(i) + "/"
        for filename in os.listdir(path):
            with open(os.path.join(path, filename), 'r') as file:
                # ignore contact and front files
                if "contact" in filename:
                    continue
                if "front" in filename:
                    continue
                file_id = doc_name + filename
                file_content = cleanhtml(file.read())
                data[file_id] = file_content
                
    json_data = json.dumps(data)
    json_file.write(json_data)
    json_file.close()
else:
    print("File already exist ... skipping")
