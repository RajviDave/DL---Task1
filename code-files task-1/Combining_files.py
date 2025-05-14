import pandas as pd
import os

folder_path = '.'  # change to your actual folder
combined_abstracts = {}

for file in os.listdir(folder_path):
     if file.endswith('.xlsx'):
        df = pd.read_excel(os.path.join(folder_path, file))
        print("Available columns:", df.columns.tolist())
        researcher_name = df['Researcher'].iloc[0]
        
#        Combine all abstracts
        combined_text = ' '.join(df['Researcher'].dropna().astype(str))
        
        combined_abstracts[researcher_name] = combined_text

# # Save to Excel
# combined_df = pd.DataFrame(combined_abstracts.items(), columns=['Researcher', 'Combined_Abstract'])
# combined_df.to_excel('Combined_Abstracts.xlsx', index=False)


# import pandas as pd
# import os

# folder="."
# all_abstract={}

# for file in os.listdir(folder):
#     if file.endswith(".xlsx"):
#         df=pd.read_excel(os.path.join(folder,file))

#         researcher_name=df['Researcher Name'].iloc[0]

#         combine_text=" ".join(df['Abstract'].dropna())

#         all_abstract[researcher_name] = combine_text

# combined_df = pd.DataFrame(all_abstract.item(), columns=['Researcher', 'Combined_Abstract'])
# combined_df.to_excel('all_abstracts.xlsx', index=False)