'''
The reporter service is responsible for generating the project report.
'''
import sys
import os
from typing import List
sys.path.append(os.environ['PROJECT_PATH'])
from tools.linear.service import LinearClient
from models.linear import ProjectState, Project
from tqdm import tqdm

class Reporter:
    def __init__(self):
        self.linear_client = LinearClient()
    
    def trigger_report(self):
        self._generate_report()
    
    def _generate_report(self):
        current_projects = self._get_current_projects()
        for project in current_projects:
            print(f"Project: {project.name}")
            if project.project_updates:
                for update in project.project_updates.nodes:
                    print(f"Update: {update.body}")
                    break

    def _get_current_projects(self) -> List[Project]:
        projects = self.linear_client.list_projects()
        projects = [project for project in projects if project.state in [ProjectState.PLANNED, ProjectState.STARTED]]
        current_projects = []
        for project in tqdm(projects):
            current_projects.append(self.linear_client.fetch_project_by_id(project.id))
        return current_projects
    
    def _send_report(self):
        raise NotImplementedError("Service not implemented yet")
