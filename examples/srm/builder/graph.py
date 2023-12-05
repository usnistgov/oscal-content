#%% Load Libraries
import tools as t
from tools import Action, check_edge_exists, use_engine
from pathlib import Path

import yaml
import re, os
import pandas as pd

act = Action()

# Create Graph
colors = {
    'default':          '#cc0000',

    # Identifiers
    'uuid':             '#a6e6fc',
    'ref-uuid':         '#c3fca6',

    # Responses
    'provided':         '#c3fca6', #'#a6e6fc',
    'inherited':        '#62d8ff',
    'responsibilities': '#c0a6fc',
    'satisfied':        '#6296ff',

    # Document
    'model':            '#f89f9b',
    'control':          '#FFC355',
    'statement':        '#FBE29d',

    'line':             '#999999',
    'line_alt':         '#cccccc',
    'line_csp':         '#c5029e',
    'line_msp':         '#7880be',
    'line_app':         '#f8baec',
    'line_connect':     '#ff9900'
}

show_document_level     = True
show_control_level      = True
show_statement_level    = True
show_edges              = True
link_documents          = True
link_responses          = False
plot_associations       = False

show_documents          = ['ssp'] #,'crm']
show_responses          = ['provided', 'inherited', 'responsibilities', 'satisfied']
show_controls           = ['sc-5']

#%% Generate
output = []
diagram = {"nodes": [],"edges": []}
files = ['test.csv']

df_rels = pd.read_csv(files[0])

#%%
df_rels.head(10)

if show_document_level:
    if 'ssp' in show_documents:
        diagram['nodes'].append({
            "id": "root_ssp_csp", 
            "label": 'SSP: CSP', 
            "type":"model", 
            "file_type":"OSCAL"
        })

        diagram['nodes'].append({
            "id": "root_ssp_msp", 
            "label": 'SSP: MSP', 
            "type":"model", 
            "file_type":"OSCAL"
        })

        diagram['nodes'].append({
            "id": "root_ssp_app", 
            "label": 'SSP: APP', 
            "type":"model", 
            "file_type":"OSCAL"
        })

    if 'crm' in show_documents:
        diagram['nodes'].append({
            "id": "root_crm_csp", 
            "label": 'CRM: CSP', 
            "type":"model", 
            "file_type":"OSCAL"
        })

        diagram['nodes'].append({
            "id": "root_crm_msp", 
            "label": 'CRM: MSP', 
            "type":"model", 
            "file_type":"OSCAL"
        })


# Controls
for index, row in df_rels.iterrows():
    if row['document'] in show_documents:
        if len(show_controls) == 0 or (len(show_controls) > 0 and row['control'].lower() in show_controls):
            if row['uuid'] not in diagram['nodes']:
                label = row['control'].upper()

                control_rel = act.b64(f"{row['source']}{row['document']}{row['control']}")

                if show_control_level:
                    diagram['nodes'].append({
                        "id": control_rel, 
                        "label": label, 
                        "type":"control", 
                        "file_type":"ctl"
                    })

                if show_edges:
                    source = f"root_{row['document']}_{row['source']}"
                    target = control_rel

                    if not check_edge_exists(source, target, diagram['edges']):
                        diagram['edges'].append({
                            "source": source,
                            "target": target,
                            "used_by": row['source'],
                            "rel": row['document'],
                            "style": f"line_{row['source']}"
                            })
        
# Statements
for index, row in df_rels.iterrows():
    if row['document'] in show_documents:
        if len(show_controls) == 0 or (len(show_controls) > 0 and row['control'].lower() in show_controls):
            if row['uuid'] not in diagram['nodes']:
                label = row['statement'].upper()

                control_rel = act.b64(f"{row['source']}{row['document']}{row['control']}")
                statement_rel = act.b64(f"{row['source']}{row['document']}{row['statement']}")

                if show_statement_level:
                    diagram['nodes'].append({
                        "id": statement_rel, 
                        "label": label, 
                        "type":"statement", 
                        "file_type":"stmt"
                    })

                if show_edges and not check_edge_exists(control_rel, statement_rel, diagram['edges']):
                        diagram['edges'].append({
                            "source": control_rel,
                            "target": statement_rel,
                            "used_by": row['source'],
                            "rel": row['document'],
                            "style": f"line_{row['source']}"
                            }) 

#%% Add statement response nodes

for index, row in df_rels.iterrows():
    if len(show_controls) == 0 or (len(show_controls) > 0 and row['control'].lower() in show_controls):
        if row['document'] in show_documents:
            if row['uuid'] not in diagram['nodes']:
                if row['relation'].lower() in show_responses:

                    label = f"{row['statement']}:{row['relation']}:{row['source']}<br/>{row['uuid'][0:9]}:{str(row['a_uuid'])[0:9]}".upper()
                    diagram['nodes'].append({
                        "id": row['uuid'], 
                        "label": label, 
                        "type":row['relation'].lower(), 
                        "file_type":row['document']
                    })

if plot_associations:
    for index, row in df_rels.iterrows():
        if len(show_controls) == 0 or (len(show_controls) > 0 and row['control'].lower() in show_controls):
            if row['document'] in show_documents:
                if row['a_uuid'] not in diagram['nodes'] and isinstance(row['a_uuid'], str):
                    if row['relation'].lower() in show_responses:

                        label = f"{row['statement']}:{row['relation']}:{row['source']}<br/>{row['uuid'][0:9]}:{str(row['a_uuid'])[0:9]}".upper()
                        diagram['nodes'].append({
                            "id": row['a_uuid'], 
                            "label": label, 
                            "type":row['relation'].lower(), 
                            "file_type":row['document']
                        })


#%%
for index, row in df_rels.iterrows():
    if len(show_controls) == 0 or (len(show_controls) > 0 and row['control'].lower() in show_controls):
        if show_edges:
            if row['document'] in show_documents:
                if row['relation'].lower() in show_responses:
                    statement_rel = act.b64(f"{row['source']}{row['document']}{row['statement']}")

                    # if check_edge_exists(statement_rel, row['uuid'], diagram['edges']):
                    diagram['edges'].append({
                        "source": statement_rel,
                        "target": row['uuid'],
                        "used_by": row['source'],
                        "rel": row['document'],
                        "style": f"line_{row['source']}"
                        }) 

                    # Within document references.
                    if link_responses:
                        if isinstance(row['a_uuid'], str) and row['document'] == 'ssp': # and row['uuid'][0:3] == row['a_uuid'][0:3]:
                            # if check_edge_exists(row['a_uuid'], row['uuid'], diagram['edges']) or False:
                            diagram['edges'].append({
                                "source": row['uuid'],
                                "target": row['a_uuid'],
                                "used_by": row['source'],
                                "rel": row['document'],
                                "style": 'line_alt'
                                }) 


# for index, row in df_rels.iterrows():
# # Link Documents
if link_documents:
    if row['document'] in show_documents:
        for index, row in df_rels.iterrows():
            if row['relation'].lower() in show_responses:            
                if len(show_controls) == 0 or (len(show_controls) > 0 and row['control'].lower() in show_controls):
                    if isinstance(row['a_uuid'], str) and row['uuid'][0:3] != row['a_uuid'][0:3]:
                        # print(f"{row['document']} : {row['source']} : {row['uuid']} : {row['a_uuid']}")
                        # if check_edge_exists(row['a_uuid'], row['uuid'], diagram['edges']):
                        diagram['edges'].append({
                            "source": row['a_uuid'],
                            "target": row['uuid'],
                            "used_by": row['source'],
                            "rel": row['document'],
                            "style": f"line_connect"
                            }) 

#%%
output.append(act.diagram_markdown(title="OSCAL Document Relationships", filename=f"UUID_Relationships.dot"))

#%%
mkdn = 'Project.workflows.md'
if os.path.isfile(mkdn):
    os.unlink(mkdn)

#%%
if len(show_controls) < 3:
    t.use_engine = "fdp" # "fdp" # "circo" # "neato"
    # ['circo', 'dot', 'fdp', 'neato', 'osage', 'patchwork', 'sfdp', 'twopi']

act.make_diagram(diagram, colors=colors, filename=f"UUID_Relationships.dot", title="OSCAL Document Relationships")
act.save_markdown(output)
