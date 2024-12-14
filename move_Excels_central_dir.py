import os
import shutil
import re

def move_uuid_xlsx_files(source_directory, target_directory):
    os.makedirs(target_directory, exist_ok=True)
    
    uuid_pattern = re.compile(r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}\.xlsx")

    for root, _, files in os.walk(source_directory):
        for file in files:
            if uuid_pattern.match(file):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(target_directory, file)
                
                shutil.move(source_path, destination_path)
                print(f"Moved: {source_path} -> {destination_path}")

if __name__ == "__main__":

    source_directory = "/Users/aryamanshetty"  
    target_directory = "/Users/aryamanshetty/Coding-Aryaman/labs/bulkjob/scripts/all_excels"

    move_uuid_xlsx_files(source_directory, target_directory)
