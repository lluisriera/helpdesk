from odoo import models, api, fields, _

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    project_id = fields.Many2one(
        comodel_name='project.project',
        string='Project')
    task_id = fields.Many2one(
        comodel_name='project.task',
        string='Task')

    # Si busco la tarea sin indicar el proyecto completar el campo del proyecto
    # (onchange en tarea que complete el projecto)
    @api.onchange('task_id')
    def _onchange_task_id(self):
        if self.task_id and self.task_id.project_id:
            self.project_id = self.task_id.project_id
        else:
            self.project_id = False

    # si busco primero el proyecto solo permitir seleccionar tareas de ese proyecto
    # (onchange a project que devuelva un domain)
    @api.onchange('project_id')
    def _onchange_project_id(self):
        if self.project_id:
            domain = {'task_id': [('project_id', '=', self.project_id.id)]}
        else:
            domain = {}
        return {'domain': domain}
