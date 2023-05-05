import requests
import base64
import yaml

def trigger_pipeline(pipeline_id, organization_name, project_name):
    print(project_name)
    print(organization_name)
    print(pipeline_id)

    url = f"https://dev.azure.com/{organization_name}/{project_name}/_apis/pipelines/{pipeline_id}/runs?api-version=7.0"
    print(url)
    body = {
        "resources": {
            "repositories": {
                "self": {
                    "refName": "refs/heads/master"
                }
            }
        }
    }
    
    response = requests.post(url, headers=headers, json=body)
    
    if response.status_code == 200:
        
        print("triggered successfully!")
    else:
        print(f"failed{response.status_code}")


# provide the file raw github url 
yaml_url = "< >"
# provide the ado token here.
ado_pat = "< >"

headers = {
    "Authorization": "Basic " + base64.b64encode(f":{ado_pat}".encode("ascii")).decode("ascii"),"Content-Type": "application/json"
}
print(headers)
response = requests.get(yaml_url)
yaml_content = response.content.decode("utf-8")

parsed_yaml = yaml.load(yaml_content, Loader=yaml.FullLoader)
print(parsed_yaml)
for resource in parsed_yaml["resources"]:
    
    pipeline_id = resource["pipelineID"]
    organization_name = resource["organization"]
    project_name = resource["resourceType"]

    trigger_pipeline(pipeline_id, organization_name, project_name)