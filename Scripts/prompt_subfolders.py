import os

 
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

 
target_dir = os.path.join(base_dir, 'By_Category')
 
subfolders = ["Full Prompts", "Prompt Snippets", "Prompt Skeletons"]
 
for root, dirs, files in os.walk(target_dir):
 
    relative_depth = len(os.path.relpath(root, base_dir).split(os.sep))
    
 
    if relative_depth == 3:
   
        for subfolder in subfolders:
            subfolder_path = os.path.join(root, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)
            print(f"Created: {subfolder_path}")

print("Subfolder creation complete!")
