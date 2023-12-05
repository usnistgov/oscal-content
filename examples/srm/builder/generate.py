#%%#######################################################################
#%% Work with controls from: https://github.com/usnistgov/csv-synthetic-controls/

import os, subprocess
import pandas as pd
import tools as t
import pandas as pd


#%%#######################################################################

error_condition             = None
errors                      = list()

#%% Paths os.getcwd()
dir_output                  = os.path.join(os.getcwd(),'../latest')
dir_template                = os.path.join(os.getcwd(),'templates')
dir_template_support        = os.path.join(os.getcwd(),'templates_support')
dir_content                 = os.path.join(os.getcwd(),'content')

filename_output             = 'example'
filename_input              = 'NIST_800-53_Rev5_Simulated.csv'
filename_crm                = 'template.cdef.srm.yaml'
filename_validation_log     = 'validation.log'

filepath_csv                = os.path.join(dir_content, filename_input)
filepath_template_crm       = os.path.join(dir_template_support, filename_crm)
filepath_validation_log     = os.path.join(dir_output, filename_validation_log)

#%% Static Settings
sep                         = '*'*100
lb                          = "\n\n"
make_xml                    = False
validate_oscal_cli          = False
oscal_cli                   = 'Validate/oscal-cli-1.0.2'
crm                         = None

#%% Setup
df_content                  = pd.read_csv(filepath_csv)
grouped_controls_df         = df_content.groupby('control_id')

t.clean_output(dir_output)

#%% Load all templates
templates = ['template.ssp.csp.yaml','template.ssp.msp.yaml','template.ssp.app.yaml']
# for root, dirs, files in os.walk(dir_template):
#     for file in files:
#         if file.endswith(".yaml"):
#              templates.append(file)



#%%#######################################################################

org_metadata = {}


org_metadata['csp'] = {
    'version':              '0.0.1',
    'ssp_title':            'Cloud Service Provider System Security Plan',
    'ssp_system_name':      'Demonstration System representing a Cloud Service Provider',
    'ssp_reason':           'This SSP demonstrates prototype modeling for sharing of responsibility.'   
}

org_metadata['msp'] = {
    'version':              '0.0.1',
    'ssp_title':            'Managed Service Provider System Security Plan',
    'ssp_system_name':      'Demonstration System representing a Managed Service Provider',
    'ssp_reason':           'This SSP demonstrates prototype modeling for sharing of responsibility.'   
}

org_metadata['app'] = {
    'version':              '0.0.1',
    'ssp_title':            'Application Owner System Security Plan',
    'ssp_system_name':      'Demonstration System representing an Application Owner',
    'ssp_reason':           'This SSP demonstrates prototype modeling for sharing of responsibility.'       
}



#%%#######################################################################
#%% Build SSPs
for ssp_template in templates:
    current_org                 = ssp_template.split('.')[2:-1][0]
    filepath_template           = os.path.join(dir_template,ssp_template)
    filepath_yaml               = os.path.join(dir_output, f"{filename_output}.{'.'.join(ssp_template.split('.')[1:-1])}.yaml")
    filepath_json               = os.path.join(dir_output, f"{filename_output}.{'.'.join(ssp_template.split('.')[1:-1])}.json")
    filepath_crm_yaml           = os.path.join(dir_output, f"{filename_output}.{'.'.join(ssp_template.split('.')[1:-1])}.crm.yaml")
    filepath_crm_json           = os.path.join(dir_output, f"{filename_output}.{'.'.join(ssp_template.split('.')[1:-1])}.crm.json")
    
    print(f"Generating [{current_org}]: {filepath_template}")
    print(f"YAML: {filepath_yaml}")
    print(f"JSON: {filepath_json}\n\n")

    metadata = org_metadata[current_org]

    # Build Content
    print("Building SSP")
    if current_org == 'csp':
        crm = None

    ssp = t.build_ssp(filepath_template, metadata, grouped_controls_df, crm)

    # Export YAML file
    print(f"YAML: {filepath_yaml}")
    t.save_yaml(ssp, filepath_yaml)

    # Export JSON file
    print(f"JSON: {filepath_json}")
    t.save_json(ssp, filepath_json)



    if validate_oscal_cli:
        with open(filepath_validation_log, "a") as outfile:
            subprocess.run([oscal_cli, 'ssp', 'validate', filepath_yaml], stdout=outfile, stderr=outfile)

        with open(filepath_validation_log, "a") as outfile:
            subprocess.run([oscal_cli, 'ssp', 'validate', filepath_json], stdout=outfile, stderr=outfile)

    if make_xml:
        with open(filepath_validation_log, "a") as outfile:
            subprocess.run([oscal_cli,'ssp','convert','--to=xml',filepath_json,filepath_json+'.xml'], stdout=outfile, stderr=outfile)



    if current_org != 'app':
        crm = t.build_crm(filepath_template_crm, ssp)

        # Export YAML file
        print(f"CRM YAML: {filepath_crm_yaml}")
        t.save_yaml(crm, filepath_crm_yaml)

        # Export JSON file
        print(f"CRM JSON: {filepath_crm_json}")
        t.save_json(crm, filepath_crm_json)      



        if validate_oscal_cli:
            with open(filepath_validation_log, "a") as outfile:
                subprocess.run([oscal_cli, 'component-definition', 'validate', filepath_crm_yaml], stdout=outfile, stderr=outfile)

            with open(filepath_validation_log, "a") as outfile:
                subprocess.run([oscal_cli, 'component-definition', 'validate', filepath_crm_json], stdout=outfile, stderr=outfile)

        if make_xml:
            with open(filepath_validation_log, "a") as outfile:
                subprocess.run([oscal_cli,'ssp','convert','--to=xml',filepath_crm_json,filepath_crm_json+'.xml'], stdout=outfile, stderr=outfile)

    print("\n\n")

#%%#######################################################################
t.record_collection.records = t.record_list
record_content = t.record_collection.dict()['records']



#%%
df = pd.DataFrame(record_content)

for index, row in df.iterrows():
    if row['control'] == 'sc-5':
        print(f"{row['control']} : {row['uuid']} : {row['a_uuid']}")

df.to_csv('test.csv')

# %%
