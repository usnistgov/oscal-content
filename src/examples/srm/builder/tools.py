import datetime, os, json, subprocess
from pathlib import Path

from faker import Faker
fake_it = Faker()

from oscalic.system_security_plan       import SystemSecurityPlan as SSP
from oscalic.component_definition       import ComponentDefinition as CDef
from oscalic.shared_responsibility      import SharedResponsibility as SRDef
from oscalic.control                    import StatementAssembly as Statement
from oscalic.control                    import ByComponentAssembly as ByComponent
from oscalic.control                    import ControlAssembly as Control
from oscalic                            import Template, Helper, Validation
from oscalic.common                     import SatisfiedAssembly, ResponsibilitiesAssembly, InheritedAssembly, ProvidedAssembly

class Identifier:
    uuid = None
    name = None

class Relation:
    source = Identifier
    target = Identifier


use_engine = "circo" # "fdp" # "circo" #"neato"


########################################################################

from pydantic import BaseModel, Field
from typing import List

class IdRecord(BaseModel):
    source: str = Field(default=None)
    document: str = Field(default=None)
    control: str = Field(default=None)
    statement: str = Field(default=None)
    relation: str = Field(default=None)
    uuid_name: str = Field(default=None)
    uuid: str = Field(default=None)
    a_uuid_name: str = Field(default=None)
    a_uuid: str = Field(default=None)

class IdCollection(BaseModel):
    records: List[IdRecord] = Field(default=[])
    
record_list = []
record_collection = IdCollection()

def add_record(record):
    global record_list
    record_list.append(record)

########################################################################

all_model_metadata = {
    'oscal_version': '1.1.1'
}

filler_word_list=['sample', 'security', 'content', 'response', 'explanation', 'identifying']

########################################################################
#%% Export YAML file
def save_yaml(ssp, filepath_yaml):
    if os.path.exists(filepath_yaml):
        os.remove(filepath_yaml)
    Path(filepath_yaml).write_text(Helper.to_yaml(ssp))

    return True

#%% Export JSON file
def save_json(ssp, filepath_json):
    ssp_output = ssp.dict(by_alias=True,exclude_unset=True)

    if os.path.exists(filepath_json):
        os.remove(filepath_json)
    out_file = open(filepath_json, "w")
    json.dump(ssp_output, out_file, sort_keys=False, indent=2)

    return True

def clean_output(dir):
    for filename in os.listdir(dir):
        ext = filename.split('.')[-1]
        if ext in ['json','xml','yaml','log']:
            os.remove(os.path.join(dir,filename))

def random_prose(input, length=10):
    words = input.split()
    result = fake_it.sentence(nb_words=length, ext_word_list=words)

    return result

def get_marker_uuid(marker):
    id = str(Helper.get_uuid())
    start = len(marker) - 1
    return marker.upper() + id[start:len(id)]

########################################################################
# source <- target
# provided <- inherited
# responsibility <- satisfied
# satisfied <- provided
# satisfied <- responsibility
# satisfied <- inherited

def check_node_exists(id, nodes):
    item_exists = [node for node in nodes if id in node.values()]
    if item_exists:
        return True
    return False

def check_edge_exists(source, target, edges):
    item_exists = [edge for edge in edges if source in edge.values() and target in edge.values()]
    if item_exists:
        return True
    return False


def get_related_uuids(target_name, source_name, source_uuid=None):
    rel = Relation
    rel.source.name = source_name
    rel.target.name = target_name

    rel.source.uuid = fake_it.uuid4()
    rel.target.uuid = fake_it.uuid4()

    if source_uuid:
        rel.source.uuid = source_uuid

    return rel


def get_components(document, statement_id=None):
    components = []

    if isinstance(document, list):
        document = document[0]

    print(document)
    for requirement in document.implemented_requirements:
        for statement in requirement.statements:
            if statement_id:
                if statement.statement_id == statement_id:
                    for component in statement.by_components:
                        components.append(component)
            else:
                for component in statement.by_components:
                    components.append(component)
    return components


def get_inherited_responses(sr, current_org_type=None, control_id=None, statement_id=None, marker=''):
    # Track Connections
    sr_org = {
        'csp': 'csp',
        'msp': 'csp',
        'app': 'msp'
    }

    sr_inherited_content = []
    sr_satisfied_content = []
    
    sr_components = get_components(sr.shared_responsibility.components[0]['control_implementations'], statement_id)

    for component in sr_components:

        ##### PROVIDED ##############################################
        if 'provided' in dir(component):
            inherited_uuid = get_marker_uuid(marker)
            # print(f"{inherited_uuid}:{component.provided[0]['uuid']}")
            sr_inherited_content.append({
                'uuid': inherited_uuid,
                'provided-uuid': component.provided[0]['uuid'],
                # 'satisfied-uuid': satisfied_uuid,
                'description': ''
                    + component.provided[0]['description']            
            })

            record = {
                'source': current_org_type,
                'document': 'ssp',
                'control': control_id,
                'statement': statement_id,
                'relation': 'inherited',
                'uuid_name': 'inherited-uuid',
                'uuid': inherited_uuid,
                'a_uuid_name': 'provided-uuid',
                'a_uuid': component.provided[0]['uuid']
            }
            add_record(IdRecord(**record))

            record = {
                'source': sr_org[current_org_type],
                'document': 'sr',
                'control': control_id,
                'statement': statement_id,
                'relation': 'provided',
                'a_uuid_name': '',
                'a_uuid': '',
                'uuid_name': 'provided-uuid',
                'uuid': component.provided[0]['uuid']
            }
            add_record(IdRecord(**record))
            # End Track Connections

        ##### RESPONSIBILITIES ##############################################
        if 'responsibilities' in dir(component):
            satisfied_uuid = get_marker_uuid(marker)
            sr_satisfied_content.append({
                'uuid': satisfied_uuid,
                'responsibility-uuid': component.responsibilities[0]['uuid'],
                'description': ''
                    + component.responsibilities[0]['description'] 
                    + ' (Random SATISFIED Content Follows) ' 
                    + random_prose(component.responsibilities[0]['description'])     
            })

            # Track Connections
            record = {
                'source': current_org_type,
                'document': 'ssp',
                'control': control_id,
                'statement': statement_id,
                'relation': 'satisfied',
                'uuid_name': 'satisfied-uuid',
                'uuid': satisfied_uuid,
                'a_uuid_name': 'responsibilities-uuid',
                'a_uuid': component.responsibilities[0]['uuid']
            }
            add_record(IdRecord(**record))

            record = {
                'source': sr_org[current_org_type],
                'document': 'sr',
                'control': control_id,
                'statement': statement_id,
                'relation': 'responsibilities',
                'a_uuid_name': '',
                'a_uuid': '',
                'uuid_name': 'responsibilities-uuid',
                'uuid': component.responsibilities[0]['uuid']
            }
            add_record(IdRecord(**record))
            # End Track Connections

    return (sr_inherited_content,sr_satisfied_content)

def build_ssp(filepath_template, metadata, controls=None, sr=None):
    current_org_type            = filepath_template.split('.')[2:-1][0]
    this_system_component_uuid  = get_marker_uuid(current_org_type)
    today                       = datetime.datetime.now()
    today_format                = '%Y-%m-%dT00:00:00.0000-04:00'
    today                       = today.strftime(today_format)

    ssp_data = {
        'uuid:component':       this_system_component_uuid,
        'uuid:document':        get_marker_uuid(current_org_type),
        'uuid:statement':       get_marker_uuid(current_org_type),
        'uuid:user':            get_marker_uuid(current_org_type),
        'uuid:party':           get_marker_uuid(current_org_type), 
        'uuid:by-component':    get_marker_uuid(current_org_type), 
        'uuid:information-type':get_marker_uuid(current_org_type), 
        'modified_date':        f"{today}"
    }
    ssp_data.update(metadata)
    ssp_data.update(all_model_metadata)

    ssp_content = Template.apply(filepath_template, ssp_data)
    ssp         = Helper.from_yaml(SSP, ssp_content)





    for control_id, group in controls:
        # if control_id == 'ac-2':
            # print(control_id.upper())

        statements = list()
        for index, row in group.iterrows():
            components = list()
            
            # 'implementation-status': {
            #     'state': row['state'],
            #     'remarks': ''
            # }

            ##### PROVIDED ##############################################
            provided_uuid = get_marker_uuid(current_org_type)
            provided_content = [{
                'uuid': provided_uuid,
                'description': row['export_provided'] 
                                    + ' (Random Content Follows) ' 
                                    + random_prose(row['export_provided']),
                'exportable': True
            }]

            # Track Connections
            record = {
                'source': current_org_type,
                'document': 'ssp',
                'control': control_id,
                'statement': row['statement_id'],
                'relation': 'provided',
                'uuid_name': 'provided-uuid',
                'uuid': provided_uuid,
                'a_uuid_name': '',
                'a_uuid': ''
            }
            add_record(IdRecord(**record))
            # End Track Connections

            ##### RESPONSIBILITIES ##############################################
            responsibilities_uuid = get_marker_uuid(current_org_type)
            responsibilities_content = [{
                'uuid': responsibilities_uuid,
                'provided-uuid': provided_uuid,
                'description': row['export_responsibility'],
                'exportable': True
            }]
            
            # Track Connections
            record = {
                'source': current_org_type,
                'document': 'ssp',
                'control': control_id,
                'statement': row['statement_id'],
                'relation': 'responsibilities',
                'uuid_name': 'responsibilities-uuid',
                'uuid': responsibilities_uuid,
                'a_uuid_name': 'provided_uuid',
                'a_uuid': provided_uuid
            }
            add_record(IdRecord(**record))
            # End Track Connections

            ##### SATISFIED ##############################################
            satisfied_uuid = get_marker_uuid(current_org_type)
            satisfied_content = [{
                'uuid': satisfied_uuid,
                'responsibility-uuid': responsibilities_uuid,
                'description': row['export_responsibility'] 
                                    + ' (Random Content Follows) ' 
                                    + random_prose(row['export_provided'])     
            }]

            # Track Connections
            record = {
                'source': current_org_type,
                'document': 'ssp',
                'control': control_id,
                'statement': row['statement_id'],
                'relation': 'satisfied',
                'uuid_name': 'satisfied-uuid',
                'uuid': satisfied_uuid,
                'a_uuid_name': 'responsibilities_uuid',
                'a_uuid': responsibilities_uuid
            }
            add_record(IdRecord(**record))
            # End Track Connections


            sr_inherited_content = []
            sr_satisfied_content = []
            if sr:
                #print(f"Get inherited for {row['statement_id']}")
                (sr_inherited_content, sr_satisfied_content) = get_inherited_responses(sr, current_org_type, control_id, row['statement_id'], current_org_type)

            
            if len(sr_satisfied_content) > 0:
                satisfied_content.extend(sr_satisfied_content)


            ##### INHERITED ##############################################
            inherited_content = None
            if '.csp.' not in filepath_template:
                inherited_uuid = get_marker_uuid(current_org_type)
                inherited_content = [{
                    'uuid': inherited_uuid,
                    'provided-uuid': provided_uuid,
                    # 'satisfied-uuid': satisfied_uuid,
                    'description': row['export_responsibility']                 
                }]
                
                if len(sr_inherited_content) > 0:
                    inherited_content.extend(sr_inherited_content)


                #print(IdCollection, dir(IdCollection))

                # Track Connections
                record = {
                    'source': current_org_type,
                    'document': 'ssp',
                    'control': control_id,
                    'statement': row['statement_id'],
                    'relation': 'inherited',
                    'uuid_name': 'inherited-uuid',
                    'uuid': inherited_uuid,
                    'a_uuid_name': 'provided-uuid',
                    'a_uuid': provided_uuid
                }
                add_record(IdRecord(**record))
                # End Track Connections
                

            #############################################################
            # Deprecated
            # export_content = {
            #     'provided': provided_content,
            #     'responsibilities': responsibilities_content
            # } 

            #############################################################
            component_content = {
                'component_uuid': this_system_component_uuid,
                'uuid': get_marker_uuid(current_org_type),
                'description': "DO NOT SHARE - " + row['description'],
                'provided': provided_content,
                'responsibilities': responsibilities_content,
                'satisfied': satisfied_content
                # 'export': export_content
            }

            if inherited_content:
                component_content['inherited'] = inherited_content

            component = ByComponent.construct(**component_content)
            components.append(component)

            #############################################################
            statement_content = {
                'statement_id': row['statement_id'],
                'uuid': get_marker_uuid(current_org_type),
                'by_components': components
            }
            statement = Statement.construct(**statement_content)
            statements.append(statement)

        control_content = {
            'uuid': get_marker_uuid(current_org_type),
            'control_id': row['control_id'],
            'statements': statements
        }


        control = Control.construct(**control_content)
        ssp.system_security_plan.control_implementation.implemented_requirements.append(control)

    return ssp




def build_sr(filepath_template, ssp):
    current_org_type= filepath_template.split('.')[2:-1][0]
    today           = datetime.datetime.now()
    today_format    = '%Y-%m-%dT00:00:00.0000-04:00'
    today           = today.strftime(today_format)

    sr_data = {
        'sr_title':        "Customer Responsibility Matrix",
        'uuid:document':    get_marker_uuid(current_org_type),
        'uuid:component':   get_marker_uuid(current_org_type), 
        'modified_date':    f"{today}",
    }
    sr_data.update(all_model_metadata)
    sr_data.update(ssp.system_security_plan.metadata.dict())
    sr_data.update(ssp.system_security_plan.metadata.dict())

    sr_content     = Template.apply(filepath_template, sr_data)
    sr             = Helper.from_yaml(SRDef, sr_content)

    # Loop through each requirement in the ssps and export the exportable.
    # for requirement in ssp.system_security_plan.control_implementation.implemented_requirements:
    #     for statements in requirement.statements:
    
    for component in get_components(ssp.system_security_plan.control_implementation):
        if 'provided' in dir(component):
            if not ('exportable' in component.provided[0] and \
            component.provided[0]['exportable'] == True):
                del component.provided

        if 'responsibilities' in dir(component):
            if not ('exportable' in component.responsibilities[0] and \
            component.responsibilities[0]['exportable'] == True):
                del component.responsibilities

        if 'satisfied' in dir(component):
            if not ('exportable' in component.satisfied[0] and \
            component.satisfied[0]['exportable'] == True):
                del component.satisfied

        if 'inherited' in dir(component) and component.inherited != None:
            if not ('exportable' in component.inherited[0] and \
            component.inherited[0]['exportable'] == True):
                del component.inherited

    sr.shared_responsibility.components=[{
        'uuid': get_marker_uuid(current_org_type),
        'name': 'Statement of Shared Responsibility',
        'description': 'This is a demonstration sr.',
        'control_implementations': [ssp.system_security_plan.control_implementation]
    }]

    return sr


##########################################################################################################


from github import Github
from dotenv import load_dotenv
from graphviz import Digraph,ENGINES
from nested_lookup import nested_lookup
from pathlib import Path

import matplotlib.colors as mc
import colorsys
import numpy as np

import os, sys, pypandoc
import base64


class Action:
    def __init__(self):
        load_dotenv()
        self.ghConn = None

        self.env = {
           'file_prefix': "Project",
           'artifact_name': "content",
           'output_path': "output",
           'markdown_name': "Project.workflows.md"
        }
        
        if 'file_prefix' in os.environ.keys():
            self.env['file_prefix'] = os.environ.get('file_prefix')

        if 'artifact_name' in os.environ.keys():
            self.env['artifact_name'] = os.environ.get('artifact_name')

        if 'output_path' in os.environ.keys():
            self.env['output_path'] = os.environ.get('output_path')

        if 'markdown_name' in os.environ.keys():
            mn = os.environ.get('markdown_name')
            if mn.endswith(".md"):
                self.env['markdown_name'] = mn
            else:
                self.env['markdown_name'] = f"{mn}.md"
        else:
            self.env['markdown_name'] = f"{self.env['file_prefix']}.workflows.md"

    def get_prefix(self):
        return f"{self.env['file_prefix']}"       

    def get_path(self):
        return f"{self.env['output_path']}"

    def get_path_and_prefix(self):
        prefix = self.env['file_prefix']
        path = self.env['output_path']

        return f"{path}/{prefix}"     

    def get_workflows(self, path='.github/workflows'):
        try:
            files = list(Path(path).iterdir())
        except:
            print(f"WARNING!!! Does not appear to have workflows.")
            files = []

        return files  
    
    def clean_uses(self, input):
        if str(input).rfind('@') > 0:
            (name,hash) = input.split('@')
            return name
        
        return str(input).replace('./.github/workflows/','')
    
    def clean_title(self, input):
        if str(input).rfind('-') > 0:
            result = f"{str(input).replace('-',' ').title()} ({input})"
            return result
        
        result = str(input).title()    
        result = result.replace('Oscal','OSCAL')
        result = result.replace('Jdk','JDK')
        result = result.replace('Xml','XML')

        return result   

    def make_table(self, node, width=300):
        return f"""
        <TABLE width='{width}'>
            <TR><td width='{width}'><b>{node['type'].upper()}</b> <i>{node['file_type']}</i></td></TR>
            <TR><td width='{width}'>{node['label']}</td></TR>
        </TABLE>
        """

    def make_width(self,input,factor=5,min=50):
        width = len(input) * factor

        if width < min:
            return min
            
        return width


    def b64(self, string):
        return str(base64.b64encode(string.encode('ascii')))

    def make_color(self, color, amount=.30):
        # Based on : https://gist.github.com/technic/8bf3932ad7539b762a05da11c0093ed5
        try:
            c = mc.cnames[color]
        except:
            c = color
        c = np.array(colorsys.rgb_to_hls(*mc.to_rgb(c)))
        (r, g, b) = colorsys.hls_to_rgb(c[0],amount,c[2])

        return mc.to_hex([r, g, b])

    def make_diagram(self, nodes_and_edges, title='Workflow Diagram', colors={'default':'#cccccc'}, filename='Overview', box_width=50):
        
        g = Digraph(format='svg')
        # g.graph_attr['size'] = '20000,20000'
        g.graph_attr.update({'nodesep': '6'})

        g.attr(scale='2', label=title, fontsize='16')

        g.attr('node', shape='box', style='filled', fontsize='16')

        all_sub_ed = []

        workflow_nodes_width = box_width
        other_nodes_width = box_width
        for node in nodes_and_edges['nodes']:
            current_width = self.make_width(node['label'])
            if ('belongs_to' in node or node['type'] == 'workflow') and current_width > workflow_nodes_width:
                workflow_nodes_width = current_width
            elif 'belongs_to' not in node and current_width > other_nodes_width:
                other_nodes_width = current_width


        for node in nodes_and_edges['nodes']:
            fillcolor=colors['default']
            if node['type'] in colors:
                fillcolor = colors[node['type']]

            if 'belongs_to' in node:
                #** GROUP THE WORKFLOW ITEMS   
                with g.subgraph(name=f"cluster_{node['belongs_to']}") as job_group:

                    sub_ed = []
                    for edge in nodes_and_edges['edges']:
                        if 'belongs_to' in edge and edge['belongs_to'] == node['belongs_to']:
                            entry = (edge['source'], edge['target'])
                            if entry not in all_sub_ed:
                                sub_ed.append(entry)
                                all_sub_ed.append(entry)
                    job_group.attr(
                        label="Workflow", 
                        penwidth="4", 
                        color=self.make_color(colors['workflow'],.4),
                        margin="250.0,250.0"
                        )

                    custom_color = self.make_color(colors[node['type']])
                    job_group.node(node['id'], 
                        label=f"<{self.make_table(node, workflow_nodes_width)}>",
                        fillcolor=fillcolor, 
                        penwidth="4",
                        color=self.make_color(fillcolor,.4))
                    job_group.attr('edge',arrowsize="1",weight="2",color=custom_color, penwidth="4")
                    job_group.edges(sub_ed)
                
            else:
                node_width = other_nodes_width
                if node['type'] == 'workflow':
                    node_width = workflow_nodes_width

                g.node(node['id'], label=f"<{self.make_table(node, node_width)}>", fillcolor=fillcolor, penwidth="4",color=self.make_color(fillcolor,.4))

        ed=[]
        

        for edge in nodes_and_edges['edges']:
            if 'belongs_to' not in edge:
                entry = (edge['source'], edge['target'])
                if entry not in ed:
                    line_color = colors['line']
                    line_weight = "2"

                    if 'style' in edge and edge['style'] in colors:
                        line_color = colors[edge['style']]

                        if edge['style'] == 'line_connect':
                            line_weight = "8"


                    g.attr('edge',arrowsize="2",weight=line_weight,color=line_color, penwidth=line_weight)
                    g.edge(edge['source'], edge['target'])
                    
                    # ed_content = (edge['source'], edge['target'])
                    # ed.append(ed_content)


        
        # g.edges(ed)

        # dot or fdp
        g.render(filename=f"{self.get_path_and_prefix()}{filename}", engine=use_engine)
        g = None

        return self.diagram_markdown(title, filename)
    
    def make_workflow_diagram(self, workflow, diagram, colors={'default':'#cccccc'}, filename='Workflow'):
        workflow_diagram = {"nodes": [],"edges": []}
        workflow_diagram['nodes'].append(workflow)

        for edge in diagram['edges']:
            if 'belongs_to' in edge and edge['belongs_to'] == workflow['id']:
                workflow_diagram['edges'].append(edge)
            elif 'used_by' in edge and edge['used_by'] == workflow['id']:
                workflow_diagram['edges'].append(edge)

        identifiers = nested_lookup('source',workflow_diagram['edges']) + nested_lookup('target',workflow_diagram['edges'])

        for node in diagram['nodes']:
            if node['id'] in identifiers:
                workflow_diagram['nodes'].append(node)

        result = self.make_diagram(workflow_diagram, colors=colors, filename=filename)
        return result
    
    def save_markdown(self, output):
        Path(f"{self.get_path()}/{self.env['markdown_name']}").write_text("\n".join(output))

    def diagram_markdown(self, title, filename):
        filename = f"{self.get_prefix()}{filename}"
        return f"\n\n---\n\n![Graphical Representation of {title}]({filename}.svg)"







