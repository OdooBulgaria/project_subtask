from openerp import models, fields, api, _
from datetime import datetime, timedelta
class project_subtask_new(models.Model):
    
    _name="project.subtask"
    _description="Project Management Module"
    _order="status"
    
    description=fields.Text("Description")
    subtask_ids=fields.Many2one("project.task","Subtask")
    status=fields.Boolean("Status")
    
    
    
class project_task(models.Model):
    _inherit="project.task"
    
    subtasks=fields.One2many("project.subtask","subtask_ids","Subtask") 